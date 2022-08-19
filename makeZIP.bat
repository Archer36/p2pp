@echo off
rem #############################################
rem # (c) Copyright 2020 - Tom Van den Eede
rem # required python/pyQt5/cx_freeze to be setup
rem # p2pp must be working prior to running
rem #############################################


rem  Remove ealier builds and create a new one
rem  #########################################

echo [*] Capture current directory
set cur_dir=%cd%

echo [*] Removing any old build/update directory
Rmdir /S /Q _build_update_
echo [*] Make the new build/update directory
Mkdir _build_update_
echo [*] CD to the new build/update directory
Cd _build_update_

echo [*] Clone the repo
git clone --branch zero-width-extrusion https://github.com/Archer36/p2pp.git

rem Create the new BUILD
rem ####################
echo [*] CD to the cloned repo
cd p2pp
echo [*] Running the setup.py file with argument build
python setup.py build

rem Determine the version
rem ####################
echo [*] Get the P2PP Version
python version.py >out.txt
echo [*] Set version env var
set /p version=<out.txt
echo [*] Delete the version out.txt file
del out.txt

echo [*] Set the name env var
set name=p2pp_%version%

echo [*] CD to build directory
cd build

echo [*] Removing any old versions of the p2pp directory
Rmdir /S /Q p2pp

rem create a ZIP file
rem #################
echo [*] Renaming cxfreeze directory to p2pp
move exe.win-amd64-3.10 p2pp
echo [*] Deleting any old versions of the zip files.
del %name%.zip
echo [*] Creating Zip
"c:\Program Files\7-Zip\7z.exe" a -tzip %name%.zip p2pp

rem copy the file to dropbox
rem ########################
echo [*] Copy the zip file to the downloads directory
copy %name%.zip %USERPROFILE%\Downloads

rem # go up to the top level #
cd %cur_dir%
echo [*] Removing the build/update directory
Rmdir /S /Q _build_update_

echo [*] Done!


