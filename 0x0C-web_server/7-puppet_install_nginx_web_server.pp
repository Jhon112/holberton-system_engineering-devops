# same as task 1 but with pupper
exec { 'server configuration':
  provider => shell,
  command  => 'URL=\"https://www.youtube.com/watch?v=7C9EYka6fIU\"; VAR=\"rewrite ^/redirect_me $URL permanent;\"; sudo apt-get update -y; sudo apt-get install nginx -y; sudo chown -R \"$USER:$USER\" /var/www/html; sudo chown -R \"$USER:$USER\" /etc/nginx/sites-available/; echo \"Holberton School\" > /var/www/html/index.html; sed -i \"19i $VAR\" /etc/nginx/sites-available/default; sudo service nginx restart;'
}