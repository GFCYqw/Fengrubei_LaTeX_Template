@echo off
chcp 65001
cls

echo ================================================================
echo 脚本名称：make.bat
echo 功能：自动化编译 LaTeX 文档并清理辅助文件
echo 使用方法：
echo   （在 src\ 下打开 cmd 并输入如下命令）
echo   .\make.bat           - 执行完整编译流程
echo   .\make.bat clean     - 清理临时文件和PDF
echo   .\make.bat distclean - 彻底清理（包括上级目录中的PDF）
echo ================================================================


cd %~dp0
set FRB=FRB-main
set PDF=%FRB%.pdf
set TEMP=%FRB%.xdv %FRB%.aux %FRB%.log %FRB%.idx %FRB%.ind %FRB%.ilg %FRB%.out %FRB%.toc %FRB%.los %FRB%-example.aux %FRB%.synctex.gz %FRB%.lof %FRB%.lot texput.log


echo 检查是否传递启动参数...
if "%1"=="clean" goto clean
if "%1"=="distclean" goto distclean


echo 无启动参数，进行编译...
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
echo 运行完成
exit /B


:clean
echo （clean）清除辅助文件，不删除上层目录的PDF
del %TEMP%
del %PDF%
echo 运行完成
exit /B


:distclean
echo （distclean）清除辅助文件，删除上层目录的PDF
del %TEMP%
del %PDF%
del ..\%PDF%
echo 运行完成
exit /B
