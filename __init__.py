from aqt.gui_hooks import sync_will_start, media_sync_did_start_or_stop

from .funcs import readConfigs, saveConfigs

# def build_action(fun, text, shortcut=None):
#     """fun -- without argument
#     text -- the text in the menu
#     """
#     action = QAction(text)
#     action.triggered.connect(lambda b: fun())
#     if shortcut:
#         action.setShortcut(shortcut)
#     return action
#
#
# readAction = build_action(readConfigs, "Read Configs")
# saveAction = build_action(saveConfigs, "Save Configs")
#
# menu_for_helper = mw.form.menuTools.addMenu("Sync Addon Configs")
# menu_for_helper.addAction(readAction)
# menu_for_helper.addAction(saveAction)

sync_will_start.append(saveConfigs)
media_sync_did_start_or_stop.append(readConfigs)
