'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
import os
import sys
import xbmc
import xbmcgui
import xbmcaddon
import io
from collections import OrderedDict
from xbmcgui import Dialog, WindowXMLDialog
from actions import ACTIONS

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')

contexts = []
userkeymap = []
defaultkeymap = []
gen_file = None


class KeyListener(WindowXMLDialog):
  def onInit( self ):
    try:
      self.getControl( 401 ).addLabel( "Press a key" )
    except:
      self.getControl( 401 ).setLabel( "Press a key" )
    try:
      self.getControl( 402 ).addLabel( "Press the key you want to assign, now!" )
    except: 
      self.getControl( 402 ).setLabel( "Press the key you want to assign, now!" )
                                                        
  def onAction(self, action):
    self.key = action.getButtonCode()
    self.close()

def node_main():
  confirm_discard = False
  while True:
    idx = Dialog().select("Keymap config", ["Edit", "Save"])
    if idx == 0:
      confirm_discard = True
      node_edit()
    elif idx == 1:
      node_save()
      break
    elif idx == -1 and confirm_discard:
      if Dialog().yesno("Keymap config", "Discard changes?") == 1:
        break
    else:
      break

def record_key():
  dialog = KeyListener("DialogKaiToast.xml", "")
  dialog.doModal()
  ret = dialog.key
  del dialog
  return str(ret)

def node_edit():
  while True:
    idx = Dialog().select("Select Window to manage shortcuts", contexts)
    if idx == -1:
      break
    context = contexts[idx]
    
    while True:
      categories = ACTIONS.keys()
      idx = Dialog().select("Select category", categories)
      if idx == -1:
        break
      category = categories[idx]
      
      while True:
        actions = get_actions(context, category)
        labels = [ "%s - %s" % (name, key) for  action, key, name in actions ]
        idx = Dialog().select("Select the action to assign a key", labels)
        if idx == -1:
          break
        action, oldkey, _ = actions[idx]
        newkey = record_key()
        
        if (context, action, oldkey) in userkeymap:
          userkeymap.remove((context, action, oldkey))
        userkeymap.append((context, action, newkey))

def node_save():
  io.write_keymap(userkeymap, gen_file)

def get_actions(context, category):
  actions = OrderedDict([(action, "") for action in ACTIONS[category].keys()])
  for c, a, k in defaultkeymap:
    if c == context:
      if actions.get(a):
        actions[a] = k
  for c, a, k in userkeymap:
    if c == context:
      if actions.get(a):
        actions[a] = k
  names = ACTIONS[category]
  ret = [ (action, key, names[action]) for action, key in actions.iteritems() ]
  return ret
  
def clean_text(text):
  text = text.replace("xbmc.","")
  text = text.replace("activatewindow(","open ")
  text = text.replace(")","")
  text = text.replace("shutdown(","shutdown")
  findstring = ["codec","level","zoom","volume","toggle","shift","delay","subtitle","small","skip","show","scroll","reset","random","previous","play","parent","page","number","item","move","lock","last","hide","first","filters","increase","decrease","cursor","channel","big","step","next","delay","seek","fast","analog","video","music","files","context","gui","osd","my","settings","addon","fullscreen","movie","login","playlist","tv","numeric","audio","picture","player","pvr","screen","shutdown","virtual","visualisation"]
  for item in findstring: 
    text = text.replace(item,item + " ")
  text = text.replace("gui de","guide")
  text = text.replace("picture s","pictures")
  text = text.replace("play er","player ")
  text = text.replace("play list","playlist")
  text = text.replace("screen shot","screenshot")
  text = text.replace("channel s","channels")
  text = text.replace("subtitle s","subtitles")
  text = text.replace("my video s","my videos")
  text = text.replace("preset ","preset")
  text = text.replace("subtitlesh","subtitle sh")
  return text

if __name__ == "__main__":
  default = xbmc.translatePath('special://xbmc/system/keymaps/keyboard.xml')
  user = xbmc.translatePath('special://userdata/keymaps')
  gen_file = os.path.join(user, 'gen.xml')
  
  if not os.path.exists(user):
    os.makedirs(user)
  else:
    #make sure there are no user defined keymaps
    for f in os.listdir(user):
      if f.endswith('.xml'):
        if f != os.path.basename(gen_file):
          src = os.path.join(user, f)
          dst = os.path.join(user, f+'.bak')
          os.rename(src, dst)
  
  defaultkeymap = io.read_keymap(default)
  print "defaultkeymap: " + str(defaultkeymap)
  userkeymap = io.read_keymap(gen_file) if os.path.exists(gen_file) else []
  
  contexts = list(set([ clean_text(c) for c,a,k in defaultkeymap ]))
  contexts.sort()
  
  node_main()

sys.modules.clear()

