@echo off
perl .\abcde.pl --multi-table-files -cm abcde::Cartographer sd2.orig.sfc commands_sd2-hex.txt script_sd2-hex -s
perl .\abcde.pl --multi-table-files -cm abcde::Cartographer sd2.orig.sfc commands_sd2.txt script_sd2 -s
python atlasify-sd2.py