@echo off
SET mypath=%~dp0
echo %mypath:~0,-1%
echo %mypath%
python %mypath%__init__.py %1
PAUSE