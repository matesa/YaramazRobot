@echo off

:: BatchGotAdmin
:-------------------------------------
REM  --> izinleri kontrol edin
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> Hata bayrağı ayarlanmışsa, yöneticimiz yoktur.
if '%errorlevel%' NEQ '0' (
    echo Yönetici ayrıcalıkları talep ediliyor ...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------
net stop YaramazRobot
net start YaramazRobot
