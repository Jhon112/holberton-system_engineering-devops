# deactivate password authentication
file_line { 'set passwd':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
}

# using holberton key
file_line { 'Using key':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/holberton',
}