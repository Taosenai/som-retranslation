@echo off
perl .\abcde.pl --multi-table-files -cm abcde::Cartographer som.orig.sfc commands_som.txt script_som -s
perl .\abcde.pl --multi-table-files -cm abcde::Cartographer som.orig.sfc commands_som-menu.txt script_som-menu -s
python atlasify-som.py 