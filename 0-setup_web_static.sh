#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

# Update package lists
sudo apt-get -y update
sudo apt-get -y upgrade

# Install nginx web server
sudo apt-get install -y nginx

# Ensure nginx is stopped
sudo service nginx stop

# Create main directories for the web app
sudo mkdir -p /data/web_static/shared
sudo mkdir -p /data/web_static/releases/test

# Create test file
sudo touch /data/web_static/releases/test/index.html
sudo echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' | sudo tee /data/web_static/releases/test/index.html

# -s: Creates a symbolic link (symlink) instead of a hard link
# -f: This flag can be useful to forcefully update or recreate existing links.
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group
# -h: Affect symbolic links instead of their targets.
# -R: hange the ownership of a directory and all of its contents.
sudo chown -hR ubuntu:ubuntu /data/

# Update the Nginx configuration 
# Config for Nginx
NGINX_CONFIG=\
"server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;

    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /hbnb_static/ {
        alias /data/web_static/current/;
    }
}"

sudo echo "$NGINX_CONFIG" | sudo tee /etc/nginx/sites-available/default;

# Start nginx server
sudo service nginx start