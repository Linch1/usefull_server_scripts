- **U NEED SSH FOR DISABLE NODM SO BEFORE ENABLE IT SETUP THE SSH WITH ANOTHER MACHINE**
- Nodm allows to run gui app at startup

- `sudo apt-get -y install nodm matchbox-window-manager`
- 
```
sudo sed -i -e "s/NODM_ENABLED=false/NODM_ENABLED=true/" -e "s/NODM_USER=root/NODM_USER=pi/" \
/etc/default/nodm
```
  
- `sudo nano ~/.xsession`
- write this bash script in ~/.xsession:
```
#!/usr/bin/env bash
xset s off -dpms
exec matchbox-window-manager &
while true; do
  python3 /home/pi/App/main.py
done
```
