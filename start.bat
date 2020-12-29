@echo off
TITLE YaramazRobot
rem Bu sonraki satır, bot yeniden başlatıldığında kökte bulunan tüm fban csv dosyalarını kaldırır. 
del *.csv
py -3.7 --version
IF "%ERRORLEVEL%" == "0" (
    py -3.7 -m Yaramaz_Robot
) ELSE (
    py -m tg_bot
)

pause
