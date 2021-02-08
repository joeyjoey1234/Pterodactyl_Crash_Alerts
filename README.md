# Pterodactyl_Crash_Alerts 

Make proper edits to Main.py to fit your mailer system, current config is for mailgun using requests
### make and 
mkdir /opt/log_auditor/ 

copy main.py to /opt/log_auditor/main.py

### copy and pasta this file ##edit as you wish 
#/etc/systemd/system/log_auditor.service 



### run these commands at bash console 
#systemctl daemon-reload 
#systemctl enable log_auditor 
#systemctl start log_auditor --no-block 
