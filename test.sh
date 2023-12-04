#!/usr/bin/env bash
# Configure nginx on port 80
cat <<EOL > /etc/nginx/sites-available/default
server {
    listen 80 default_server;
    server_name _;

    location / {
        root /usr/share/nginx/html;
        index index.html;
    }

    location /custom_404.html {
        internal;
        root /usr/share/nginx/html;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=dphzDKZa6xk;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /usr/share/nginx/html;
        internal;
    }
}
EOL