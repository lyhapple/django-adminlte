@echo off 
echo *********************************************************** 
echo ���SVN�汾�� Ϣ                                                                                               
echo *********************************************************** 
:start 
::�������̣��л�Ŀ¼ 
:set pwd=%cd% 
:cd %1 
echo ����Ŀ¼�ǣ�& chdir 
:input 
::��ȡ���룬����������д��� 
set source=: 
set /p source=ȷ��Ҫ�����ǰĿ¼�µ�.svn��Ϣ��[Y/N/Q] 
set "source=%source:"=%" 
if "%source%"=="y" goto clean 
if "%source%"=="Y" goto clean 
if "%source%"=="n" goto noclean 
if "%source%"=="N" goto noclean 
if "%source%"=="q" goto end 
if "%source%"=="Q" goto end 
goto input 
:clean 
::��������̣�ִ�������� 
@echo on 
@for /d /r %%c in (.svn) do @if exist %%c ( rd /s /q %%c & echo    ɾ��Ŀ¼%%c) 
@echo off 
echo "��ǰĿ¼�µ�svn��Ϣ�����" 
goto end 
:noclean 
::��֧���̣�ȡ�������� 
echo "svn��Ϣ���������ȡ��" 
goto end 
:end 
::�˳����� 
cd "%pwd%" 
pause