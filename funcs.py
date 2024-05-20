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
        if meta_json.is_file():
            dest_file = media_path / f"_{addon_dir.name}_meta.json"
            shutil.copy(meta_json, dest_file)


def readConfigs():
    anki_addons_path = Path(mw.pm.addonFolder()).resolve(strict=True)
    media_path = Path(mw.pm.profileFolder(), 'collection.media')

    for addon_dir in anki_addons_path.iterdir():
        if not addon_dir.is_dir():
            continue

        meta_json = media_path / f"_{addon_dir.name}_meta.json"
        if meta_json.is_file():
            dest_file = addon_dir / "meta.json"
            shutil.copy(meta_json, dest_file)
