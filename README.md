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

### `Project Setup`
*`Valid for all implementations!`*

Find the project directory (downloaded from git):
```console
~ ./LEMP-tm
```

## Installation (Linux)
`Following installation only implies to Ubuntu setup.`
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
Start configuration of database `(only for development)`:
```console
mysql_secure_installation
```
Following prompts must be handled (capital Y: default):
* "Enter current password for root" -> `none (ENTER)`
* "Switch to unix_socket authentication" -> `n`
* "Set root password?" -> `Y`
  * Password: "`insecure`"
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
Install NPM (should be normally provided with NodeJS):
```console
apt install -y npm
```
`!!!` Only set following environment variable when remote access is required:
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

## Automatization (Ansible)
`Following installation (again) only implies to Ubuntu setup.`

Start with installing necessary packages:
```console
sudo apt install -y ansible openssh-server sshpass
```
Limit ssh port with ufw:
```console
sudo ufw limit ssh &&\
sudo ufw enable
```
Go to the ansible directory:
```console
cd /opt/LEMP-tm/linux/ansible
```
Ansible will be run locally with following command:
```console
sudo ansible-playbook -i inventory lemp-playbook.yml --extra-vars "server_hosts=localhost" -kK -v
```

## Containerization (Docker)
Start with installing necessary packages:

Setup Docker repo:
```console
sudo apt update

sudo apt install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
Install Docker:
```console
sudo chmod a+r /etc/apt/keyrings/docker.gpg

sudo apt update

sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-compose
```
Start up Docker Compose with following commands:
```console
cd /opt/LEMP-tm

sudo docker-compose build

sudo docker-compose up
```
