This addon will save and load your current addon configs into Anki's media files folder.
Saving and loading is done on syncing.

# How to use

1. Edit configs on device A
2. Sync on device A
3. Sync on device B. Restarting Anki may be required for addons to load the new configs.

## Conflicting changes

If you

1. Edit configs on device A
2. Edit configs on device B
3. Sync on device A
4. Sync on device B

Then the first to sync and upload the changes to AnkiWeb wins = device A's configs overwrite device B's.

It appears that changes to a media file in AnkiWeb trumps not yet uploaded changes to the same media file which is why
the first to sync wins.
