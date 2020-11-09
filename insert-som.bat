@echo off
echo --- Patching clean ROM
del som.sfc
xdelta\xdelta.exe -f -d -s som.orig.sfc patch_som.move-bank-locations.xdelta som.sfc
echo --- Inserting script
perl .\abcde.pl --multi-table-files -cm abcde::Atlas som.sfc .\script_som-atlasify.txt
echo --- Inserting menu
perl .\abcde.pl --multi-table-files --artificial-end-token "<END>" -cm abcde::Atlas som.sfc .\script_som-menu-atlasify.txt