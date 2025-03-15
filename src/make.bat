@echo off
cd %~dp0
set FRB=FRB-main
set PDF=%FRB%.pdf
set TEMP=%FRB%.xdv %FRB%.aux %FRB%.log %FRB%.idx %FRB%.ind %FRB%.ilg %FRB%.out %FRB%.toc %FRB%.los %FRB%-example.aux %FRB%.synctex.gz

if "%1"=="clean" goto clean
if "%1"=="distclean" goto distclean

set TEX=xelatex
set NOPDFMODE=-interaction=nonstopmode -synctex=1 --no-pdf
set MODE=-interaction=nonstopmode -synctex=1
set MAKEINDEX=makeindex

%TEX% %NOPDFMODE% %FRB%
%MAKEINDEX% -s %FRB%.ist %FRB%
%TEX% %NOPDFMODE% %FRB%
%TEX% %MODE% %FRB%

if exist %PDF% (
copy %PDF% ..
)
exit /B

:clean
del %TEMP%
del %PDF%
exit /B

:distclean
del %TEMP%
del %PDF%
del ..\%PDF%
exit /B
