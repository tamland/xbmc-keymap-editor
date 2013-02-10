'''
    This program is free software, you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    [at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http,//www.gnu.org/licenses/>.
'''
_actions = [
  ["Navigation", [
    "left"              , "Move Left",
    "right"             , "Move Right",
    "up"                , "Move Up",
    "down"              , "Move Down",
    "pageup"            , "Page Up",
    "pagedown"          , "Page Down",
    "select"            , "Select Item",
    "highlight"         , "HIGHLIGHT_ITEM",
    "parentdir"         , "NAV_BACK",       # backward compatibility
    "close"             , "NAV_BACK", # backwards compatibility
    "parentfolder"      , "PARENT_DIR",
    "back"              , "NAV_BACK",
    "previousmenu"      , "PREVIOUS_MENU",
    "info"              , "SHOW_INFO",
    "contextmenu"       , "CONTEXT_MENU",
    "firstpage"         , "FIRST_PAGE",
    "lastpage"          , "LAST_PAGE",
    "nextletter"        , "NEXT_LETTER",
    "prevletter"        , "PREV_LETTER",
  ]],
  
  ["Playback", [
    "play"              , "Play",
    "pause"             , "Pause",
    "playpause"         , "Play/Pause",
    "stop"              , "Stop",
    "skipnext"          , "Next Item",
    "skipprevious"      , "Prev Item",
    
    "fastforward"       , "PLAYER_FORWARD",
    "rewind"            , "PLAYER_REWIND",
    
    "stepforward"       , "STEP_FORWARD",
    "stepback"          , "STEP_BACK",
    "smallstepback"     , "SMALL_STEP_BACK",
    "bigstepforward"    , "BIG_STEP_FORWARD",
    "bigstepback"       , "BIG_STEP_BACK",
    
    "fullscreen"        , "SHOW_GUI",
    "togglefullscreen"  , "TOGGLE_FULLSCREEN",
    
    "osd"               , "SHOW_OSD",
    "showvideomenu"     , "SHOW_VIDEOMENU",
    
    "nextpicture"       , "NEXT_PICTURE",
    "previouspicture"   , "PREV_PICTURE",

    "playlist"          , "SHOW_PLAYLIST",
    "queue"             , "QUEUE_ITEM",
    "aspectratio"       , "ASPECT_RATIO",
  ]],
  
  ["Audio", [
    "mute"              , "MUTE",
    "volumeup"          , "VOLUME_UP",
    "volumedown"        , "VOLUME_DOWN",
    "audionextlanguage" , "AUDIO_NEXT_LANGUAGE",
    "audiodelay"        , "AUDIO_DELAY",
    "audiodelayminus"   , "AUDIO_DELAY_MIN",
    "audiodelayplus"    , "AUDIO_DELAY_PLUS",
    "audiotoggledigital", "TOGGLE_DIGITAL_ANALOG",
  ]],
  
  ["Subtitle", [
    "showsubtitles"     , "Show_SUBTITLES",
    "nextsubtitle"      , "NEXT_SUBTITLE",
    "subtitledelay"     , "SUBTITLE_DELAY",
    "subtitledelayminus", "SUBTITLE_DELAY_MIN",
    "subtitledelayplus" , "SUBTITLE_DELAY_PLUS",
    "subtitlealign"     , "SUBTITLE_ALIGN",
    "subtitleshiftup"   , "SUBTITLE_VSHIFT_UP",
    "subtitleshiftdown" , "SUBTITLE_VSHIFT_DOWN",
  ]],
  
  
  ["PVR", [
    "channelup"             , "CHANNEL_UP",
    "channeldown"           , "CHANNEL_DOWN",
    "previouschannelgroup"  , "PREVIOUS_CHANNELGROUP",
    "nextchannelgroup"      , "NEXT_CHANNELGROUP",
  ]],
  
  ["Item actions", [
    "delete"            , "DELETE_ITEM",
    "copy"              , "COPY_ITEM",
    "move"              , "MOVE_ITEM",
    "moveitemup"        , "MOVE_ITEM_UP",
    "moveitemdown"      , "MOVE_ITEM_DOWN",
    "rename"            , "RENAME_ITEM",
    "scanitem"          , "SCAN_ITEM",
    "togglewatched"     , "TOGGLE_WATCHED",
    "increaserating"    , "INCREASE_RATING",
    "decreaserating"    , "DECREASE_RATING",
  ]],
  
  ["Common keys", [
    "enter"             , "ENTER",
    "shift"             , "SHIFT",
    "symbols"           , "SYMBOLS",
    "red"               , "TELETEXT_RED",
    "green"             , "TELETEXT_GREEN",
    "yellow"            , "TELETEXT_YELLOW",
    "blue"              , "TELETEXT_BLUE",
    "backspace"         , "BACKSPACE",
    "number0"           , "REMOTE_0",
    "number1"           , "REMOTE_1",
    "number2"           , "REMOTE_2",
    "number3"           , "REMOTE_3",
    "number4"           , "REMOTE_4",
    "number5"           , "REMOTE_5",
    "number6"           , "REMOTE_6",
    "number7"           , "REMOTE_7",
    "number8"           , "REMOTE_8",
    "number9"           , "REMOTE_9",
  ]],
  
  
  ["Other", [
    "codecinfo"         , "SHOW_CODEC",
    "screenshot"        , "TAKE_SCREENSHOT",
    "reloadkeymaps"     , "RELOAD_KEYMAPS",
    "nextresolution"    , "CHANGE_RESOLUTION",
    
    "zoomout"           , "ZOOM_OUT",
    "zoomin"            , "ZOOM_IN",
    "zoomnormal"        , "ZOOM_LEVEL_NORMAL",
    "zoomlevel1"        , "ZOOM_LEVEL_1",
    "zoomlevel2"        , "ZOOM_LEVEL_2",
    "zoomlevel3"        , "ZOOM_LEVEL_3",
    "zoomlevel4"        , "ZOOM_LEVEL_4",
    "zoomlevel5"        , "ZOOM_LEVEL_5",
    "zoomlevel6"        , "ZOOM_LEVEL_6",
    "zoomlevel7"        , "ZOOM_LEVEL_7",
    "zoomlevel8"        , "ZOOM_LEVEL_8",
    "zoomlevel9"        , "ZOOM_LEVEL_9",
    
    "rotate"            , "ROTATE_PICTURE_CW",
    "rotateccw"         , "ROTATE_PICTURE_CCW",
    
    "nextcalibration"   , "CALIBRATE_SWAP_ARROWS",
    "resetcalibration"  , "CALIBRATE_RESET",
  ]],
  
   
  ["OSD", [
    "mplayerosd"        , "SHOW_MPLAYER_OSD",
    "hidesubmenu"       , "OSD_HIDESUBMENU",
    "showtime"          , "SHOW_OSD_TIME",
    "osdleft"           , "OSD_SHOW_LEFT",
    "osdright"          , "OSD_SHOW_RIGHT",
    "osdup"             , "OSD_SHOW_UP",
    "osddown"           , "OSD_SHOW_DOWN",
    "osdselect"         , "OSD_SHOW_SELECT",
    "osdvalueplus"      , "OSD_SHOW_VALUE_PLUS",
    "osdvalueminus"     , "OSD_SHOW_VALUE_MIN",
  ]],
  
  
  ["Analog", [
    "scrollup"          , "SCROLL_UP",
    "scrolldown"        , "SCROLL_DOWN",
    "cursorleft"        , "CURSOR_LEFT",
    "cursorright"       , "CURSOR_RIGHT",
    "analogmove"        , "ANALOG_MOVE",
    "analogfastforward" , "ANALOG_FORWARD",
    "analogrewind"      , "ANALOG_REWIND",
    "analogseekforward" , "ANALOG_SEEK_FORWARD",
    "analogseekback"    , "ANALOG_SEEK_BACK",
    "leftclick"         , "MOUSE_LEFT_CLICK",
    "rightclick"        , "MOUSE_RIGHT_CLICK",
    "middleclick"       , "MOUSE_MIDDLE_CLICK",
    "doubleclick"       , "MOUSE_DOUBLE_CLICK",
    "wheelup"           , "MOUSE_WHEEL_UP",
    "wheeldown"         , "MOUSE_WHEEL_DOWN",
    "mousedrag"         , "MOUSE_DRAG",
    "mousemove"         , "MOUSE_MOVE",
  ]]
  
  
  
  #"verticalshiftup"   , "VSHIFT_UP",
  #"verticalshiftdown" , "VSHIFT_DOWN",
 #
  #"showpreset"        , "VIS_PRESET_SHOW",
  #"presetlist"        , "VIS_PRESET_LIST",
  #"nextpreset"        , "VIS_PRESET_NEXT",
  #"previouspreset"    , "VIS_PRESET_PREV",
  #"lockpreset"        , "VIS_PRESET_LOCK",
  #"randompreset"      , "VIS_PRESET_RANDOM",
  #"increasevisrating" , "VIS_RATE_PRESET_PLUS",
  #"decreasevisrating" , "VIS_RATE_PRESET_MINUS",
  #
  #"nextscene"         , "NEXT_SCENE",
  #"previousscene"     , "PREV_SCENE",
  #
  #"jumpsms2"          , "JUMP_SMS2",
  #"jumpsms3"          , "JUMP_SMS3",
  #"jumpsms4"          , "JUMP_SMS4",
  #"jumpsms5"          , "JUMP_SMS5",
  #"jumpsms6"          , "JUMP_SMS6",
  #"jumpsms7"          , "JUMP_SMS7",
  #"jumpsms8"          , "JUMP_SMS8",
  #"jumpsms9"          , "JUMP_SMS9",
  #"filter"            , "FILTER",
  #"filterclear"       , "FILTER_CLEAR",
  #"filtersms2"        , "FILTER_SMS2",
  #"filtersms3"        , "FILTER_SMS3",
  #"filtersms4"        , "FILTER_SMS4",
  #"filtersms5"        , "FILTER_SMS5",
  #"filtersms6"        , "FILTER_SMS6",
  #"filtersms7"        , "FILTER_SMS7",
  #"filtersms8"        , "FILTER_SMS8",
  #"filtersms9"        , "FILTER_SMS9",
  #
  #"guiprofile"        , "GUIPROFILE_BEGIN",
  #
  #"increasepar"       , "INCREASE_PAR",
  #"decreasepar"       , "DECREASE_PAR",
  #"volampup"          , "VOLAMP_UP",
  #"volampdown"        , "VOLAMP_DOWN",

]

from collections import OrderedDict

def _to_dict():
  ret = OrderedDict()
  for elem in _actions:
    category = elem[0]
    actions = elem[1][0::2]
    names = elem[1][1::2]
    ret[category] = OrderedDict(zip(actions, names))
  return ret
  
ACTIONS = _to_dict()
