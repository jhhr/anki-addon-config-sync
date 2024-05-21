from aqt.gui_hooks import sync_will_start, media_sync_did_start_or_stop

from .funcs import readConfigs, saveConfigs

sync_will_start.append(saveConfigs)
media_sync_did_start_or_stop.append(readConfigs)
