#nginx puppet setup

exec{ 'install':
  provider => shell,
  command  => 'sudo apt-get -y updates ; sudo apt-get -y nginx ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/google.com permanent;/" /etc/nginx/sites-available/default ; service nginx start ; echo "Hello World!" > /var/www/html/index.nginx-debian.html ; sudo service nginx restart',
}
