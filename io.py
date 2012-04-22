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
import xml.etree.cElementTree as etree
from elementtree.SimpleXMLWriter import XMLWriter


def read_keymap(filename):
  ret = []
  with open(filename, 'r') as xml:
    tree = etree.iterparse(xml)
    for _, keymap in tree:
      for context in keymap:
        for device in context:
          for mapping in device:
            key = mapping.get('id') or mapping.tag
            action = mapping.text
            if action:
              ret.append((context.tag.lower(), action.lower(), key.lower()))
  return ret


def write_keymap(keymap, filename):
  contexts = list(set([ c for c,a,k in keymap ]))
  actions  = list(set([ a for c,a,k in keymap ]))
  
  w = XMLWriter(filename, "utf-8")
  doc = w.start("keymap")
  
  for context in contexts:
    w.start(context)
    w.start("keyboard")
    for c,a,k in keymap:
      if c==context:
        w.element("key", a, id=k)
    w.end()
    w.end()
  w.end()
  w.close(doc)


actions = [
  'left',
  'right',
  'up',
  'down',
  'select',
  'pageup',
  'pagedown',
  'highlight',
  'parentdir',
  'previousmenu',
  'info',
  'pause',
  'stop',
  'skipnext',
  'skipprevious',
  'fullscreen',
  'aspectratio',
  'stepforward',
  'stepback',
  'bigstepforward',
  'bigstepback',
  'smallstepback',
  'osd',
  'playdvd',
  'showvideomenu',
  'showsubtitles',
  'nextsubtitle',
  'codecinfo',
  'nextpicture',
  'previouspicture',
  'zoomout',
  'zoomin',
  'increasepar',
  'decreasepar',
  'queue',
  'playlist',
  'zoomnormal',
  'zoomlevel1',
  'zoomlevel2',
  'zoomlevel3',
  'zoomlevel4',
  'zoomlevel5',
  'zoomlevel6',
  'zoomlevel7',
  'zoomlevel8',
  'zoomlevel9',
  'nextcalibration',
  'resetcalibration',
  'analogmove',
  'rotate',
  'close',
  'subtitledelayminus',
  'subtitledelayplus',
  'audiodelayminus',
  'audiodelayplus',
  'audionextlanguage',
  'nextresolution',
  'number0',
  'number1',
  'number2',
  'number3',
  'number4',
  'number5',
  'number6',
  'number7',
  'number8',
  'number9',
  'fastforward',
  'rewind',
  'play',
  'delete',
  'copy',
  'move',
  'rename',
  'hidesubmenu',
  'screenshot',
  'xbmc.shutdown()',
  'volumeup',
  'volumedown',
  'mute',
  'backspace',
  'scrollup',
  'scrolldown',
  'analogfastforward',
  'analogrewind',
  'analogseekforward',
  'analogseekback',
  'moveitemup',
  'moveitemdown',
  'contextmenu',
  'shift',
  'symbols',
  'cursorleft',
  'cursorright',
  'showtime',
  'showpreset',
  'presetlist',
  'nextpreset',
  'previouspreset',
  'lockpreset',
  'randompreset',
  'increaserating',
  'decreaserating',
  'togglewatched',
  'nextletter',
  'prevletter',
  'jumpsms2-9',
  'filtersms2-9',
  'xbmc.activatewindow(myvideos)',
  'xbmc.activatewindow(mymusic)',
  'xbmc.activatewindow(mypictures)',
  'xbmc.activatewindow(home)'
]
