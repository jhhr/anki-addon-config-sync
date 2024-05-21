import filecmp
import shutil
from pathlib import Path

from aqt import mw


def saveConfigs():
    anki_addons_path = Path(mw.pm.addonFolder()).resolve(strict=True)
    media_path = Path(mw.pm.profileFolder(), 'collection.media')

    for addon_dir in anki_addons_path.iterdir():
        if not addon_dir.is_dir():
            continue

        meta_json = addon_dir / "meta.json"
        dest_file = media_path / f"_{addon_dir.name}_meta.json"

        if meta_json.is_file():
            # If the destination media file doesn't exist, or the meta.json file has changed,
            # copy the meta.json file to the media folder
            if not dest_file.is_file() or not filecmp.cmp(meta_json, dest_file, False):
                shutil.copy(meta_json, dest_file)
                # Just copying the file doesn't seem to trigger Anki to sync it, so rename it and then rename it back
                dest_file.rename(dest_file.with_suffix('.temp'))
                dest_file.with_suffix('.temp').rename(dest_file)


def readConfigs(media_sync_status):
    # If media_sync_status is True, then media sync is still in progress, and we should not read the configs yet
    if media_sync_status is True:
        return

    anki_addons_path = Path(mw.pm.addonFolder()).resolve(strict=True)
    media_path = Path(mw.pm.profileFolder(), 'collection.media')

    for addon_dir in anki_addons_path.iterdir():
        if not addon_dir.is_dir():
            continue

        meta_json = addon_dir / "meta.json"
        dest_file = media_path / f"_{addon_dir.name}_meta.json"

        # do we have a dest file that differs from the current meta.json file?
        if dest_file.is_file():
            if not meta_json.is_file() or not filecmp.cmp(meta_json, dest_file, False):
                # The files don't match, so copy the dest file to the meta.json
                shutil.copy(dest_file, meta_json)
