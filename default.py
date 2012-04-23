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

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id')

contexts = []
actions = []
userkeymap = []
defaultkeymap = []
gen_file = None
bg_img = os.path.join(ADDON.getAddonInfo('path'), 'bg.png')


class KeyListener(xbmcgui.WindowDialog):
  def __init__(self):
    w = 256
    h = 128
    x = self.getWidth()/2 - w/2
    y = self.getHeight()/2 - h/2
    self.addControl(xbmcgui.ControlImage(x, y, w, h, bg_img))
    self.addControl(xbmcgui.ControlLabel(x, y, w, h, 'Press button', 'font13', '0xFFFF0000', alignment=6))
  
  def onAction(self, action):
    self.key = action.getButtonCode()
    self.close()

def record_key():
  dialog = KeyListener()
  dialog.doModal()
  ret = dialog.key
  del dialog
  return str(ret)

def node_main():
  confirm_discard = False
  while True:
    idx = xbmcgui.Dialog().select("Keymap config", ["Edit", "Save"])
    if idx == 0:
      confirm_discard = True
      node_edit()
    elif idx == 1:
      node_save()
      break
    elif idx == -1 and confirm_discard:
      if xbmcgui.Dialog().yesno("Keymap config", "Discard changes?") == 1:
        break
    else:
      break


def node_edit():
  while True:
    idx = xbmcgui.Dialog().select("Select context", contexts)
    if idx == -1: break
    context = contexts[idx]
    
    while True:
      actions = get_actions(context)
      labels = [ "%s  -  %s" % (a, k) for  a, k in actions ]
      
      idx = xbmcgui.Dialog().select("Select action", labels)
      if idx == -1:
        break
      action, oldkey = actions[idx]
      newkey = record_key()
      
      print("%s setting action <%s> to key <%s>. oldkey <%s>" % (ADDON_ID, action, newkey, oldkey)  )
      
      if (context, action, oldkey) in userkeymap:
        userkeymap.remove((context, action, oldkey))
      userkeymap.append((context, action, newkey))


def node_save():
  io.write_keymap(userkeymap, gen_file)


def get_actions(context):
  ret = []
  
  for c,a,k in userkeymap:
    if c == context:
      ret.append((a, k))
  
  for c,a,k in defaultkeymap:
    if c == context:
      exists = [e for e in ret if e[0] == a]
      if not exists:
        ret.append((a, k))
  
  for a in actions:
    exists = [e for e in ret if e[0] == a]
    if not exists:
      ret.append((a, 'none'))
  
  ret.sort()
  return ret


if (__name__ == "__main__"):
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
  
  contexts = list(set([ c for c,a,k in defaultkeymap ]))
  actions = list(set([ a for c,a,k in defaultkeymap ] + io.actions))
  contexts.sort()
  
  node_main()

sys.modules.clear()

