# Pterodactyl_Crash_Alerts \n
 \n
 \n

## mk the dir for the program
mkdir /opt/log_auditor/ \n
\n
\n
### copy main.py to /opt/log_auditor/main.py
\n
## copy and pasta this file ##edit as you wish \n
/etc/systemd/system/log_auditor.service \n
\n
\n
## run these commands at bash console \n
systemctl daemon-reload \n
systemctl enable log_auditor \n
systemctl start log_auditor --no-block \n
