file { '/home/username/.ssh/config':
  owner   => 'username',
  group   => 'username',
  mode    => '0600',
  content => "
Host myserver
  Hostname myserver.example.com
  User myusername
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
  ",
}
