# Written by Miguel Bigueur
# Incident Response Windows
# Security Scripting w/Python
# Dec 25, 2017


@echo ******************************
@echo Running Intrusion Detection Script v1.0

REM Get date and time
date /t >> c:\IRDETECT\start.txt
time /t >> c:\IRDETECT\start.txt

REM fast information from PSLIST, IPCONFIG, etc
ipconfig /displaydns >> c:\IRDETECT\displaydns.txt
ipconfig /all >> c:\IRDETECT\ipconfig.txt

REM Check status of open connections
netstat -abno >> c:\IRDETECT\netstat.abno.txt

REM Show OS Versions
Ver >> c:\IRDETECT\ver.txt

REM Show started services on the system
Net start >> c:\IRDETECT\netstart.txt

REM List of running process, PID, memory usage, user account, CPU time, etcÖ
tasklist /v >> c:\IRDETECT\tasks.txt

REM Registry entry information
Reg export HKLM\Software\Microsoft\Windows\CurrentVersion\Run c:\IRDETECT\RunReg.txt

REM Check for scheduled tasks
Schtasks > c:\IRDETECT\schtasks.txt

REM Event Log Info
WEVTUtil query-events System /count:250 /RD:true /format:text >> C:\IRDETECT\Systemlog.txt
WEVTUtil query-events Security /count:250 /RD:true /format:text >> C:\IRDETECT\Securitylog.txt
WEVTUtil query-events Application /count:250 /RD:true /format:text >> C:\IRDETECT\Applicationlog.txt

@echo ******************************
@echo Script Complete!
