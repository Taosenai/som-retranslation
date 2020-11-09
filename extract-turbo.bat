@echo off
perl .\abcde.pl --multi-table-files -cm abcde::Cartographer turbo.orig.sfc commands_turbo-vwf.txt script_turbo-vwf -s
perl .\abcde.pl --multi-table-files -cm abcde::Cartographer turbo.orig.sfc commands_turbo-vwf.vanilla.txt script_turbo-vwf.vanilla -s
python atlasify-turbo.py