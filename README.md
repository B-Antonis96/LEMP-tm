# LEMP-tm

## Project
LEMP stack for school project, application hosts a website for displaying "messages" from database.

## Tools and technologies used:
### `Linux`
* Ubuntu 22.04: https://ubuntu.com/download/server
### `Frontend`
* Node.js: https://nodejs.org/en/
* Reactjs: https://reactjs.org
* Nginx: https://nginx.org
### `Backend`
* FastAPI: https://fastapi.tiangolo.com
* Python 3.10: https://www.python.org
* MariaDB: https://mariadb.com
### `DevOps`
* Ansible: https://www.ansible.com
* Docker: https://www.docker.com

## Installation (Linux)
Following installation only implies to Ubuntu setup.
### Pre-requirements:
* Fresh installed Ubuntu machine
* Project files (Lemp-tm)
### `Base`
Become the root user:
```console
sudo -i
```
Move the project directory (from downloaded location):
```console
mv ./LEMP-tm /opt
```
Access the project directory:
```console
cd /opt/LEMP-tm
```
Install updates:
```console
apt update && apt dist-upgrade -y
```
When UI shows prompts for restarting services:
* press TAB
* press ENTER
  
Firewall settings:
```console
ufw limit ssh &&\
ufw enable
```
Optional firewall settings (dev tools):
```console
ufw allow 8000 &&\
ufw allow 3306 &&\
ufw reload
```

### `Database`
Install MariaDB server:
```console
apt install mariadb-server -y
```
Start configuration of database:
```console
mysql_secure_installation
```
Following prompts must be handled:
* "Enter current password for root" -> `none (ENTER)`
* "Switch to unix_socket authentication" -> `n`
* "Set root password?" -> `Y`
  * Password: `insecure`
  * Re-enter password
* "Remove anonymous users?" -> `Y`
* "Disallow root login remotely?" -> `n`
* "Remove test database and access to it?" -> `Y`
* "Reload privilege tables now? " -> `Y`

Copy configuration to mysql directory:
```console
cp ./database/my.cnf /etc/mysql/conf.d/
```
Run lemp.sql file from the project directory:
```console
mysql < ./database/lemp.sql
```
Restart MariaDB service:
```console
systemctl restart mariadb
```

### `Backend`
Create api directory:
```console
mkdir -p /var/www/api
```
Install required packages:
```console
apt install -y python3.10 python3-pip
```
Install project pip packages:
```console
pip install -r ./requirements.txt
```
Copy the contents of the backend directory:
```console
cp -r ./backend/* /var/www/api/
```
Copy the service file to the system directory:
```console
cp ./linux/backend/lemp-backend.service /etc/systemd/system/
```
Enable and start the backend service:
```console
systemctl daemon-reload &&\
systemctl enable lemp-backend &&\
systemctl start lemp-backend
```

### `Webserver`
Install Nginx webserver:
```console
apt install nginx -y
```
Set firewall rules:
```console
ufw allow 'Nginx HTTP' &&\
ufw reload
```
Copy the configuration file from the project directory to Nginx config:
```console
cp ./linux/nginx/default.conf /etc/nginx/conf.d
```
Install Nodejs:
```console
curl -fsSL https://deb.nodesource.com/setup_18.x | bash - &&\
apt install -y nodejs
```
`!!!` Do NOT set following environment variable for LOCAL development:
```console
export REACT_APP_BACKEND="$HOSTNAME:8000"
```
`!` *Repeat all following steps after 'redeclaring' the `REACT_APP_BACKEND` variable* `!`

Build the frontend:
```console
cd frontend/ &&\
npm install &&\ 
npm run build &&\
cd ..
```
Copy the contents of the build directory:
```console
cp -r ./frontend/build/* /var/www/html/
```
Restart Nginx service:
```console
systemctl restart nginx
```