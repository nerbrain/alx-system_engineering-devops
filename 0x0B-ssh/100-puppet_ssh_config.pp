#SSH config file created with Puppet
file { '/home/username/.ssh/config':
  owner   => 'username',
  group   => 'username',
  mode    => '0600',
  content => "
Host myserver
  Hostname 100.26.243.4
  User ubuntu
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
  ",
}
