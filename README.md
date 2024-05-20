Currently, this is a very simple addon that reads and writes addon configs to the media folder.

Adds the following new menu:
Main window > Tools -> Sync Addon Configs
- Save Configs: writes all current addon configs into files in the media folder.
- Read Configs: reads all addon configs from files in the media folder and overwrites current addon configs.

How to use:
1. Save configs on device A
2. Sync on device A
3. Sync on device B
4. Read configs on device B
5. Configs in device B should now match what was on device A, assuming they have all the same addons.

BEWARE

- As you are about to save your recently edited configs for syncing to another device, accidentally clicking Read
  Configs instead will overwrite your current edits... A proper syncing system should remove this shortfall (TODO soon)
