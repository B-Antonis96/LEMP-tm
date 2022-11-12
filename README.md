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
Install updates:
```console
sudo apt update && sudo apt dist-upgrade -y
```
Firewall settings:
```console
sudo ufw limit ssh
sudo ufw enable
```
Optional firewall settings (dev tools):
```console
sudo ufw allow 8000
sudo ufw allow 3306
sudo ufw reload
```
### `Database`
Install MariaDB server:
```console
sudo apt install mariadb-server -y
```
Start configuration of database:
```console
sudo mysql_secure_installation
```
Following prompts must be handled:
* "Enter current password for root" -> `none (ENTER)`
* "Switch to unix_socket authentication" -> `n`
* "Set root password?" -> `n`
* "Remove anonymous users?" -> `Y`
* "Disallow root login remotely?" -> `Y`
* "Remove test database and access to it?" -> `Y`
* "Reload privilege tables now? " -> `Y`

Run lemp.sql file from the project directory:
```console
sudo mysql < ./database/lemp.sql
```
### `Webserver`
Install Nginx webserver:
```console
sudo apt install nginx -y
```
Set firewall rules:
```console
sudo ufw allow 'Nginx HTTP'
sudo ufw reload
```
Copy the configuration file from the project directory to Nginx config:
```console
sudo cp ./linux/nginx/default.conf /etc/nginx/conf.d
```
Install Nodejs
```console
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```
Build the frontend:
```console
cd frontend/
npm install
npm run build
cd ..
```
Copy the contents of the build directory:
```console
sudo cp -r ./frontend/build/* /var/www/html/
```
### `Backend`
Create project directory:
```console
sudo mkdir /var/www/api
```
Install required packages:
```console
sudo apt install -y python3.10 python3-pip
```
Install project pip packages:
```console
pip install -r ./requirements.txt
```
Copy the contents of the backend directory:
```console
sudo cp -r ./backend/* /var/www/api/
```