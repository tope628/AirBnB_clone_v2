#!/usr/bin/env bash
# configure web server for deploying web_static

# install Nginx
sudo apt-get update
sudo apt-get -y install nginx
service nginx start

# create folders if not already exist
mkdir --parents /data/web_static/releases/test/
mkdir --parents /data/web_static/shared/

# create a fake html file for testing
cd /data/web_static/releases/test/
wget https://github.com/tanyastropheus/AirBnB_clone_v2/blob/master/index.html

# delete symlink if it exists
file="/data/web_static/current"
if [-L "$file"]
then unlink "$file"
fi

# re-establish symlink /data/web_static/current to target
ln -s /data/web_static/releases/test/ /data/web_static/current

# change ownership (user & group) for the /data/ directory & sub-directories
sudo chown -R ubuntu:ubuntu /data/

# configure Nginx to serve proper web content
cd /etc/nginx/sites-available
sudo rm -f default
wget https://github.com/tanyastropheus/AirBnB_clone_v2/blob/master/default
service nginx restart
