@echo off
copy sd2.orig.sfc sd2.sfc
perl .\abcde.pl --multi-table-files -cm abcde::Atlas sd2.sfc .\script_sd2-atlasify-hex.txt