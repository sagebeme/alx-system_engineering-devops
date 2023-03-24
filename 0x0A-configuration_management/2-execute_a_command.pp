#executing a command
execute{ 'killmenow':
        command => 'pkill killmenow',
        path    => '/usr/bin';
}
