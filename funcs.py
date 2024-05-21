import filecmp
import os
import shutil
from pathlib import Path

from aqt import mw


def saveConfigs():
    """
    Saves the configs from the addon folder to the media folder, if they have changed or
    don't exist in the media folder yet.

    The file actions done here are what will trigger Anki to upload the files to AnkiWeb.
    This is run before media sync starts, so the changes will be immediately uploaded.
    Any conflicting changes previously uploaded to AnkiWeb will be overwritten, which means
    that the last person to sync their changes will have their changes uploaded.
    :return:
    """
    anki_addons_path = Path(mw.pm.addonFolder()).resolve(strict=True)
    media_path = Path(mw.pm.profileFolder(), 'collection.media')

    print("Saving configs")

    for addon_dir in anki_addons_path.iterdir():
        if not addon_dir.is_dir():
            continue

        meta_json = addon_dir / "meta.json"
        dest_file = media_path / f"_{addon_dir.name}_meta.json"

        if meta_json.is_file():
            # If the destination media file doesn't exist, or the meta.json file has changed,
            # copy the meta.json file to the media folder
            if not dest_file.is_file():
                shutil.copy(meta_json, dest_file)
            elif not filecmp.cmp(meta_json, dest_file, False):
                # To trigger Anki to sync the file, remove the old one and copy the new one
                os.remove(dest_file)
                print(f"Copying meta.json to media for {addon_dir.name}", dest_file.is_file())
                shutil.copy(meta_json, dest_file)


def readConfigs(media_sync_status: bool):
    """
    Read the configs from the media folder and copy them to the addon folder.
    This is run after media sync has finished and saveConfigs has run.
    If saveConfigs has written a new meta.json file into media folder, then it's modified date will
    be newer than anything downloaded from AnkiWeb, and Anki will not overwrite it.

    Thus, any changes that are detected between the meta.json file in the addon folder and the one in the media folder
    will be because those changes were uploaded to AnkiWeb but not modified locally.
    """
    print("Media sync status:", media_sync_status, )
    # If media_sync_status is True, then media sync is still in progress, and we should not read the configs yet
    if media_sync_status is True:
        return
    print("Reading configs")

    anki_addons_path = Path(mw.pm.addonFolder()).resolve(strict=True)
    media_path = Path(mw.pm.profileFolder(), 'collection.media')

    for addon_dir in anki_addons_path.iterdir():
        if not addon_dir.is_dir():
            continue

        meta_json = addon_dir / "meta.json"
        dest_file = media_path / f"_{addon_dir.name}_meta.json"

        print(f"dest_file for {addon_dir.name}", dest_file.is_file())

        # do we have a dest file that differs from the current meta.json file?
        if dest_file.is_file():
            if not meta_json.is_file() or not filecmp.cmp(meta_json, dest_file, False):
                print(f"Copying dest_file to meta.json for {addon_dir.name}")
                # The files don't match, so copy the dest file to the meta.json
                shutil.copy(dest_file, meta_json)
