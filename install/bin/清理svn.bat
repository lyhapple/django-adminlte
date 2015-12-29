@echo off 
echo *********************************************************** 
echo 清除SVN版本信 息                                                                                               
echo *********************************************************** 
:start 
::启动过程，切换目录 
:set pwd=%cd% 
:cd %1 
echo 工作目录是：& chdir 
:input 
::获取输入，根据输入进行处理 
set source=: 
set /p source=确定要清楚当前目录下的.svn信息吗？[Y/N/Q] 
set "source=%source:"=%" 
if "%source%"=="y" goto clean 
if "%source%"=="Y" goto clean 
if "%source%"=="n" goto noclean 
if "%source%"=="N" goto noclean 
if "%source%"=="q" goto end 
if "%source%"=="Q" goto end 
goto input 
:clean 
::主处理过程，执行清理工作 
@echo on 
@for /d /r %%c in (.svn) do @if exist %%c ( rd /s /q %%c & echo    删除目录%%c) 
@echo off 
echo "当前目录下的svn信息已清除" 
goto end 
:noclean 
::分支过程，取消清理工作 
echo "svn信息清楚操作已取消" 
goto end 
:end 
::退出程序 
cd "%pwd%" 
pause