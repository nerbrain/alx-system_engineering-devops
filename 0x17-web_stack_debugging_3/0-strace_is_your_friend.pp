# Fixing Wordpress 500 Error

exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
  onlyif   => 'cat /var/www/html/wp-settings.php | grep class-wp-locale.phpp'
}

