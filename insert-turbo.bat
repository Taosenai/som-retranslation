@echo off
copy turbo.orig.sfc turbo.sfc
perl .\abcde.pl --multi-table-files -cm abcde::Atlas turbo.sfc .\script_turbo-vwf-atlasify.txt