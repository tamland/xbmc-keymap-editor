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
    "highlight"         , "Highlight Item",
    #"parentdir"         , "NAV_BACK",       # backward compatibility
    #"close"             , "NAV_BACK", # backwards compatibility
    "parentfolder"      , "Parent Directory",
    "back"              , "Back",
    "previousmenu"      , "Previous Menu",
    "info"              , "Show Info",
    "contextmenu"       , "Context Menu",
    "firstpage"         , "First Page",
    "lastpage"          , "Last Page",
    "nextletter"        , "Next Letter",
    "prevletter"        , "Previous Letter",
  ]],
  
  ["Playback", [
    "play"              , "Play",
    "pause"             , "Pause",
    "playpause"         , "Play/Pause",
    "stop"              , "Stop",
    "skipnext"          , "Next",
    "skipprevious"      , "Previous",
    "fastforward"       , "Fast Forward",
    "rewind"            , "Rewind",
    "smallstepback"     , "Small Step Back",
    "stepforward"       , "Step Forward",
    "stepback"          , "Step Back",
    "bigstepforward"    , "Big Step Forward",
    "bigstepback"       , "Big Step Back",
    "osd"               , "Show OSD",
    "showtime"          , "Show current play time",
    "playlist"          , "Show Playlist",
    "fullscreen"        , "Toggle Fullscreen",
    "aspectratio"       , "Change Aspect Ratio",
    "showvideomenu"     , "Go to DVD Video Menu",
  ]],
  
  ["Audio", [
    "mute"              , "Mute",
    "volumeup"          , "Volume Up",
    "volumedown"        , "Volume Down",
    "audionextlanguage" , "Next Language",
    "audiodelay"        , "Delay",
    "audiodelayminus"   , "Delay Minus",
    "audiodelayplus"    , "Delay Plus",
    "audiotoggledigital", "Toggle Digital/Analog",
  ]],
  
  ["Pictures", [
    "nextpicture"       , "Next Picture",
    "previouspicture"   , "Previous Picture",
    "rotate"            , "Rotate Picture",
    "rotateccw"         , "Rotate Picture CCW",
    "zoomout"           , "Zoom Out",
    "zoomin"            , "Zoom In ",
    "zoomnormal"        , "Zoom level Normal",
    "zoomlevel1"        , "Zoom level 1",
    "zoomlevel2"        , "Zoom level 2",
    "zoomlevel3"        , "Zoom level 3",
    "zoomlevel4"        , "Zoom level 4",
    "zoomlevel5"        , "Zoom level 5",
    "zoomlevel6"        , "Zoom level 6",
    "zoomlevel7"        , "Zoom level 7",
    "zoomlevel8"        , "Zoom level 8",
    "zoomlevel9"        , "Zoom level 9",
  ]],
  
  ["Subtitle", [
    "showsubtitles"     , "Show Subtitles",
    "nextsubtitle"      , "Next Subtitle",
    "subtitledelay"     , "Delay",
    "subtitledelayminus", "Delay Minus",
    "subtitledelayplus" , "Delay Plus",
    "subtitlealign"     , "Align",
    #"subtitleshiftup"   , "SUBTITLE_VSHIFT_UP", #?
    #"subtitleshiftdown" , "SUBTITLE_VSHIFT_DOWN", #?
  ]],
  
  ["PVR", [
    "channelup"             , "Channel Up",
    "channeldown"           , "Channel Down",
    "previouschannelgroup"  , "Previous channel group",
    "nextchannelgroup"      , "Next channel group",
  ]],
  
  ["Item Actions", [
    "queue"             , "Queue item",
    "delete"            , "Delete item",
    "copy"              , "Copy item",
    "move"              , "Move item",
    "moveitemup"        , "Move item up",
    "moveitemdown"      , "Move item down",
    "rename"            , "Rename item",
    "scanitem"          , "Scan item",
    "togglewatched"     , "Toggle watched status",
    #"increaserating"    , "INCREASE_RATING", #unused
    #"decreaserating"    , "DECREASE_RATING", #unused
  ]],
  
  ["System", [
    "togglefullscreen"  , "Toggle Fullscreen",
    "minimize"          , "Minimize",
    "shutdown"          , "Shutdown",
    "reboot"            , "Reboot",
    "hibernate"         , "Hibernate",
    "Suspend"           , "Suspend",
    "restartapp"        , "Restart XBMC",
    "quit"              , "Quit XBMC",
  ]],
  
  ["Virtual Keyboard", [
    "enter"             , "Enter",
    "shift"             , "Shift",
    "symbols"           , "Symbols",
    "backspace"         , "Backspace ",
    "number0"           , "0",
    "number1"           , "1",
    "number2"           , "2",
    "number3"           , "3",
    "number4"           , "4",
    "number5"           , "5",
    "number6"           , "6",
    "number7"           , "7",
    "number8"           , "8",
    "number9"           , "9",
    "red"               , "Teletext Red",
    "green"             , "Teletext Green",
    "yellow"            , "Teletext Yellow",
    "blue"              , "Teletext Blue",
  ]],
  
  ["Other", [
    "codecinfo"         , "Show codec info",
    "screenshot"        , "Take screenshot",
    "reloadkeymaps"     , "Reload keymaps",
    "increasepar"       , "Increase PAR",
    "decreasepar"       , "Decrease PAR",
    "nextresolution"    , "Change resolution",
    "nextcalibration"   , "Next calibration",
    "resetcalibration"  , "Reset calibration",
    "showpreset"        , "Show current visualisation preset",
    "presetlist"        , "Show visualisation preset list",
    "nextpreset"        , "Next visualisation preset",
    "previouspreset"    , "Previous visualisation preset",
    "lockpreset"        , "Lock current visualisation preset ",
    "randompreset"      , "Switch to a new random preset",
  ]],
  
  #["Analog", [
  #  "scrollup"          , "SCROLL_UP",
  #  "scrolldown"        , "SCROLL_DOWN",
  #  "cursorleft"        , "CURSOR_LEFT",
  #  "cursorright"       , "CURSOR_RIGHT",
  #  "analogmove"        , "ANALOG_MOVE",
  #  "analogfastforward" , "ANALOG_FORWARD",
  #  "analogrewind"      , "ANALOG_REWIND",
  #  "analogseekforward" , "ANALOG_SEEK_FORWARD",
  #  "analogseekback"    , "ANALOG_SEEK_BACK",
  #  "leftclick"         , "MOUSE_LEFT_CLICK",
  #  "rightclick"        , "MOUSE_RIGHT_CLICK",
  #  "middleclick"       , "MOUSE_MIDDLE_CLICK",
  #  "doubleclick"       , "MOUSE_DOUBLE_CLICK",
  #  "wheelup"           , "MOUSE_WHEEL_UP",
  #  "wheeldown"         , "MOUSE_WHEEL_DOWN",
  #  "mousedrag"         , "MOUSE_DRAG",
  #  "mousemove"         , "MOUSE_MOVE",
  #]]
  
  #"verticalshiftup"   , "VSHIFT_UP",
  #"verticalshiftdown" , "VSHIFT_DOWN",
  #"increasevisrating" , "VIS_RATE_PRESET_PLUS",
  #"decreasevisrating" , "VIS_RATE_PRESET_MINUS",
  #"nextscene"         , "NEXT_SCENE",
  #"previousscene"     , "PREV_SCENE",
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
  #"guiprofile"        , "GUIPROFILE_BEGIN",
  #"volampup"          , "VOLAMP_UP",
  #"volampdown"        , "VOLAMP_DOWN",
  #"mplayerosd"        , "SHOW_MPLAYER_OSD", #?
  #"hidesubmenu"       , "OSD_HIDESUBMENU", #depricated
  #"osdleft"           , "OSD_SHOW_LEFT",
  #"osdright"          , "OSD_SHOW_RIGHT",
  #"osdup"             , "OSD_SHOW_UP",
  #"osddown"           , "OSD_SHOW_DOWN",
  #"osdselect"         , "OSD_SHOW_SELECT",
  #"osdvalueplus"      , "OSD_SHOW_VALUE_PLUS",
  #"osdvalueminus"     , "OSD_SHOW_VALUE_MIN",
]

_windows = [
  "global"                   , "Global",
  "home"                     , "Home",
  "programs"                 , "Programs",
  "video"                    , "WINDOW_VIDEOS",
  "music"                    , "WINDOW_MUSIC",
  "pictures"                 , "WINDOW_PICTURES",
  "filemanager"              , "WINDOW_FILES",
  "files"                    , "WINDOW_FILES", # backward compat
  "settings"                 , "WINDOW_SETTINGS_MENU",
  "videos"                   , "WINDOW_VIDEO_NAV",
  "videolibrary"             , "WINDOW_VIDEO_NAV",
  "tv"                       , "WINDOW_PVR", # backward compat
  "pvr"                      , "WINDOW_PVR",
  "pvrguideinfo"             , "WINDOW_DIALOG_PVR_GUIDE_INFO",
  "pvrrecordinginfo"         , "WINDOW_DIALOG_PVR_RECORDING_INFO",
  "pvrtimersetting"          , "WINDOW_DIALOG_PVR_TIMER_SETTING",
  "pvrgroupmanager"          , "WINDOW_DIALOG_PVR_GROUP_MANAGER",
  "pvrchannelmanager"        , "WINDOW_DIALOG_PVR_CHANNEL_MANAGER",
  "pvrguidesearch"           , "WINDOW_DIALOG_PVR_GUIDE_SEARCH",
  "pvrchannelscan"           , "WINDOW_DIALOG_PVR_CHANNEL_SCAN",
  "pvrupdateprogress"        , "WINDOW_DIALOG_PVR_UPDATE_PROGRESS",
  "pvrosdchannels"           , "WINDOW_DIALOG_PVR_OSD_CHANNELS",
  "pvrosdguide"              , "WINDOW_DIALOG_PVR_OSD_GUIDE",
  "pvrosddirector"           , "WINDOW_DIALOG_PVR_OSD_DIRECTOR",
  "pvrosdcutter"             , "WINDOW_DIALOG_PVR_OSD_CUTTER",
  "pvrosdteletext"           , "WINDOW_DIALOG_OSD_TELETEXT",
  "systeminfo"               , "WINDOW_SYSTEM_INFORMATION",
  "testpattern"              , "WINDOW_TEST_PATTERN",
  "screencalibration"        , "WINDOW_SCREEN_CALIBRATION",
  "guicalibration"           , "WINDOW_SCREEN_CALIBRATION", # backward compat
  "picturessettings"         , "WINDOW_SETTINGS_MYPICTURES",
  "programssettings"         , "WINDOW_SETTINGS_MYPROGRAMS",
  "weathersettings"          , "WINDOW_SETTINGS_MYWEATHER",
  "musicsettings"            , "WINDOW_SETTINGS_MYMUSIC",
  "systemsettings"           , "WINDOW_SETTINGS_SYSTEM",
  "videossettings"           , "WINDOW_SETTINGS_MYVIDEOS",
  "networksettings"          , "WINDOW_SETTINGS_SERVICE", # backward compat
  "servicesettings"          , "WINDOW_SETTINGS_SERVICE",
  "appearancesettings"       , "WINDOW_SETTINGS_APPEARANCE",
  "pvrsettings"              , "WINDOW_SETTINGS_MYPVR",
  "tvsettings"               , "WINDOW_SETTINGS_MYPVR",  # backward compat
  "scripts"                  , "WINDOW_PROGRAMS", # backward compat
  "videofiles"               , "WINDOW_VIDEO_FILES",
  "videoplaylist"            , "WINDOW_VIDEO_PLAYLIST",
  "loginscreen"              , "WINDOW_LOGIN_SCREEN",
  "profiles"                 , "WINDOW_SETTINGS_PROFILES",
  "skinsettings"             , "WINDOW_SKIN_SETTINGS",
  "addonbrowser"             , "WINDOW_ADDON_BROWSER",
  "yesnodialog"              , "WINDOW_DIALOG_YES_NO",
  "progressdialog"           , "WINDOW_DIALOG_PROGRESS",
  "virtualkeyboard"          , "WINDOW_DIALOG_KEYBOARD",
  "volumebar"                , "WINDOW_DIALOG_VOLUME_BAR",
  "submenu"                  , "WINDOW_DIALOG_SUB_MENU",
  "favourites"               , "WINDOW_DIALOG_FAVOURITES",
  "contextmenu"              , "WINDOW_DIALOG_CONTEXT_MENU",
  "infodialog"               , "WINDOW_DIALOG_KAI_TOAST",
  "numericinput"             , "WINDOW_DIALOG_NUMERIC",
  "gamepadinput"             , "WINDOW_DIALOG_GAMEPAD",
  "shutdownmenu"             , "WINDOW_DIALOG_BUTTON_MENU",
  "mutebug"                  , "WINDOW_DIALOG_MUTE_BUG",
  "playercontrols"           , "WINDOW_DIALOG_PLAYER_CONTROLS",
  "seekbar"                  , "WINDOW_DIALOG_SEEK_BAR",
  "musicosd"                 , "WINDOW_DIALOG_MUSIC_OSD",
  "addonsettings"            , "WINDOW_DIALOG_ADDON_SETTINGS",
  "visualisationsettings"    , "WINDOW_DIALOG_ADDON_SETTINGS", # backward compat
  "visualisationpresetlist"  , "WINDOW_DIALOG_VIS_PRESET_LIST",
  "osdvideosettings"         , "WINDOW_DIALOG_VIDEO_OSD_SETTINGS",
  "osdaudiosettings"         , "WINDOW_DIALOG_AUDIO_OSD_SETTINGS",
  "videobookmarks"           , "WINDOW_DIALOG_VIDEO_BOOKMARKS",
  "filebrowser"              , "WINDOW_DIALOG_FILE_BROWSER",
  "networksetup"             , "WINDOW_DIALOG_NETWORK_SETUP",
  "mediasource"              , "WINDOW_DIALOG_MEDIA_SOURCE",
  "profilesettings"          , "WINDOW_DIALOG_PROFILE_SETTINGS",
  "locksettings"             , "WINDOW_DIALOG_LOCK_SETTINGS",
  "contentsettings"          , "WINDOW_DIALOG_CONTENT_SETTINGS",
  "songinformation"          , "WINDOW_DIALOG_SONG_INFO",
  "smartplaylisteditor"      , "WINDOW_DIALOG_SMART_PLAYLIST_EDITOR",
  "smartplaylistrule"        , "WINDOW_DIALOG_SMART_PLAYLIST_RULE",
  "busydialog"               , "WINDOW_DIALOG_BUSY",
  "pictureinfo"              , "WINDOW_DIALOG_PICTURE_INFO",
  "accesspoints"             , "WINDOW_DIALOG_ACCESS_POINTS",
  "fullscreeninfo"           , "WINDOW_DIALOG_FULLSCREEN_INFO",
  "karaokeselector"          , "WINDOW_DIALOG_KARAOKE_SONGSELECT",
  "karaokelargeselector"     , "WINDOW_DIALOG_KARAOKE_SELECTOR",
  "sliderdialog"             , "WINDOW_DIALOG_SLIDER",
  "addoninformation"         , "WINDOW_DIALOG_ADDON_INFO",
  "musicplaylist"            , "WINDOW_MUSIC_PLAYLIST",
  "musicfiles"               , "WINDOW_MUSIC_FILES",
  "musiclibrary"             , "WINDOW_MUSIC_NAV",
  "musicplaylisteditor"      , "WINDOW_MUSIC_PLAYLIST_EDITOR",
  "teletext"                 , "WINDOW_DIALOG_OSD_TELETEXT",
  "selectdialog"             , "WINDOW_DIALOG_SELECT",
  "musicinformation"         , "WINDOW_DIALOG_MUSIC_INFO",
  "okdialog"                 , "WINDOW_DIALOG_OK",
  "movieinformation"         , "WINDOW_DIALOG_VIDEO_INFO",
  "textviewer"               , "WINDOW_DIALOG_TEXT_VIEWER",
  "fullscreenvideo"          , "WINDOW_FULLSCREEN_VIDEO",
  "fullscreenlivetv"         , "WINDOW_FULLSCREEN_LIVETV",
  "visualisation"            , "WINDOW_VISUALISATION",
  "slideshow"                , "WINDOW_SLIDESHOW",
  "filestackingdialog"       , "WINDOW_DIALOG_FILESTACKING",
  "karaoke"                  , "WINDOW_KARAOKELYRICS",
  "weather"                  , "WINDOW_WEATHER",
  "screensaver"              , "WINDOW_SCREENSAVER",
  "videoosd"                 , "WINDOW_DIALOG_VIDEO_OSD",
  "videomenu"                , "WINDOW_VIDEO_MENU",
  "videotimeseek"            , "WINDOW_VIDEO_TIME_SEEK",
  "musicoverlay"             , "WINDOW_DIALOG_MUSIC_OVERLAY",
  "videooverlay"             , "WINDOW_DIALOG_VIDEO_OVERLAY",
  "startwindow"              , "WINDOW_START",
  "startup"                  , "WINDOW_STARTUP_ANIM",
  "peripherals"              , "WINDOW_DIALOG_PERIPHERAL_MANAGER",
  "peripheralsettings"       , "WINDOW_DIALOG_PERIPHERAL_SETTINGS",
  "extendedprogressdialog"   , "WINDOW_DIALOG_EXT_PROGRESS",
  "mediafilter"              , "WINDOW_DIALOG_MEDIA_FILTER"
]

from collections import OrderedDict

def _to_dict():
  ret = OrderedDict()
  for elem in _actions:
    category = elem[0]
    actions = elem[1][0::2]
    names = elem[1][1::2]
    ret[category] = OrderedDict(zip(actions, names))
  
  actions = [ "activatewindow(%s)" % id for id in _windows[2::2] ] #dont include "global"
  names = [ "Activate Window %s" % name for name in _windows[3::2] ]
  ret["Windows"] = OrderedDict(zip(actions, names))
  return ret

ACTIONS = _to_dict() # map the action list to a CategoryStr -> ActionKey -> ActionStr dict
WINDOWS = OrderedDict(zip(_windows[0::2], _windows[1::2]))

import xbmcaddon
tr = xbmcaddon.Addon().getLocalizedString
