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
from actions import WINDOWS

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')
tr = ADDON.getLocalizedString

userkeymap = []
defaultkeymap = []
gen_file = None

class KeyListener(WindowXMLDialog):
  def onInit(self):
    try:
      self.getControl(401).addLabel(tr(30001))
      self.getControl(402).addLabel(tr(30002))
    except:
      self.getControl(401).setLabel(tr(30001))
      self.getControl(402).setLabel(tr(30002))
  
  def onAction(self, action):
    self.key = action.getButtonCode()
    self.close()

def node_main():
  confirm_discard = False
  while True:
    idx = Dialog().select(tr(30000), [tr(30003), tr(30005)])
    if idx == 0:
      confirm_discard = True
      node_edit()
    elif idx == 1:
      node_save()
      break
    elif idx == -1 and confirm_discard:
      if Dialog().yesno(tr(30000), tr(30006)) == 1:
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
    idx = Dialog().select(tr(30007), WINDOWS.values())
    if idx == -1:
      break
    window = WINDOWS.keys()[idx]
    
    while True:
      idx = Dialog().select(tr(30008), ACTIONS.keys())
      if idx == -1:
        break
      category = ACTIONS.keys()[idx]
      
      while True:
        actions = get_actions(window, category)
        labels = [ "%s - %s" % (name, key) for  action, key, name in actions ]
        idx = Dialog().select(tr(30009), labels)
        if idx == -1:
          break
        action, oldkey, _ = actions[idx]
        newkey = record_key()
        
        if (window, action, oldkey) in userkeymap:
          userkeymap.remove((window, action, oldkey))
        userkeymap.append((window, action, newkey))

def node_save():
  io.write_keymap(userkeymap, gen_file)

def get_actions(window, category):
  actions = OrderedDict([(action, "") for action in ACTIONS[category].keys()])
  for w, a, k in defaultkeymap:
    if w == window:
      if a in actions.keys():
        actions[a] = k
  for w, a, k in userkeymap:
    if w == window:
      if a in actions.keys():
        actions[a] = k
  names = ACTIONS[category]
  ret = [ (action, key, names[action]) for action, key in actions.iteritems() ]
  return ret


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
  userkeymap = io.read_keymap(gen_file) if os.path.exists(gen_file) else []
  
  node_main()

sys.modules.clear()
