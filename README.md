This addon will save and load your current addon configs into Anki's media files folder.
Saving and loading is done on syncing.

# How to use

1. Edit configs on device A
2. Sync on device A
3. Sync on device B.

- Some addons will require restarting Anki for them to load the new configs.

## Conflicting changes

In a nutshell, **the first device to sync to AnkiWeb** is the one whose addon config edits will overwrite conflicting configs when syncing on other devices.
It appears that changes to a media file in AnkiWeb trumps not yet uploaded changes to the same media file which is why the first to sync wins.

In more detail:

1. Edit configs on device A without syncing.
2. Edit configs on device B without syncing.

Device A and B now have conflicting changes.

3. Sync on device A. Edited configs files are uploaded to AnkiWeb
4. Sync on device B. Config files are downloaded from Ankiweb, overwriting conflicting edits on device B

### Recommendation

Immediately after editing configs on one device, sync on that device and then sync on your other devices.

# Links

- [Github](https://github.com/jhhr/anki-addon-config-sync)
- [Anki forums thread](https://forums.ankiweb.net/t/addon-for-syncing-addon-configs/45118)
