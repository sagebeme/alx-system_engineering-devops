# 0x0A. Configuration management by Sagebeme

## About

Introduction to **configuration management with Puppet**: writing manifests that create a file, install a package and run a command.

## Learning Objectives

- What configuration management is and why it matters
- Puppet resources (`file`, `package`, `exec`) and the Puppet DSL
- Applying and linting manifests with `puppet apply` and `puppet-lint`
- Idempotence: making the same manifest safe to run repeatedly

## Resource

- [Intro to Configuration Management](https://www.digitalocean.com/community/tutorials/an-introduction-to-configuration-management)
- [Puppet resource type: file](https://puppet.com/docs/puppet/5.5/types/file.html) (*Check "Resource types" for all manifest types in the left menu*)
- [Puppet’s Declarative Language: Modeling Instead of Scripting](https://puppet.com/blog/puppets-declarative-language-modeling-instead-of-scripting/)
- [Puppet lint](http://puppet-lint.com/)
- [Puppet emacs mode](https://github.com/voxpupuli/puppet-mode)
- [Puppet CookBook](https://www.puppetcookbook.com/)

## Installing `puppet` and `puppet-lint`

```sh
# installing puppet and puppet-lint
wget https://apt.puppet.com/puppet7-release-focal.deb && \
    dpkg -i puppet7-release-focal.deb && \
    apt-get update && \
    apt-get install puppet-agent puppet-lint -y

# confirming installation
puppet -V
puppet-lint -v

# If you get an error saying puppet command not found, source the path
source /etc/profile.d/puppet-agent.sh
```

## Tasks

-----

### 0. Configuration management (Puppet)

mandatory

Create Puppet manifests to manage files and configurations. Run: `puppet apply manifest.pp` or as per task.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x0A-configuration_management`
-   File: (task manifests as per project)

## Task Descriptions

### 0. Create a file

Using Puppet, create a file in `/tmp`.

Requirements:

*   File path is `/tmp/school`
*   File permission is `0744`
*   File owner is `www-data`
*   File group is `www-data`
*   File contains `I love Puppet`

Example:

    root@6712bef7a528:~# puppet-lint --version
    puppet-lint 2.5.2
    root@6712bef7a528:~# puppet-lint 0-create_a_file.pp
    root@6712bef7a528:~#
    root@6712bef7a528:~# puppet apply 0-create_a_file.pp
    Notice: Compiled catalog for 6712bef7a528.ec2.internal in environment production in 0.04 seconds
    Notice: /Stage[main]/Main/File[school]/ensure: defined content as '{md5}f1b70c2a42a98d82224986a612400db9'
    Notice: Finished catalog run in 0.03 seconds
    root@6712bef7a528:~#
    root@6712bef7a528:~# ls -l /tmp/school
    -rwxr--r-- 1 www-data www-data 13 Mar 19 23:12 /tmp/school
    root@6712bef7a528:~# cat /tmp/school
    I love Puppetroot@6712bef7a528:~#

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0A-configuration_management`
- File: [0-create_a_file.pp](./0-create_a_file.pp)

### 1. Install a package

Using Puppet, install `puppet-lint`.

Requirements:

*   Install `puppet-lint`
*   Version must be `2.5.0`

Example:

    root@d391259bf577:/# puppet apply 1-install_a_package.pp
    Notice: Compiled catalog for d391259bf577 in environment production in 0.14 seconds
    Notice: Applied catalog in 0.20 seconds
    root@d391259bf577:/# gem list

    *** LOCAL GEMS ***

    puppet-lint (2.5.0)
    root@d391259bf577:/#

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0A-configuration_management`
- File: [1-install_a_package.pp](./1-install_a_package.pp)

### 2. Execute a command

Using Puppet, create a manifest that kills a process named `killmenow`.

Requirements:

*   Must use the `exec` Puppet resource
*   Must use `pkill`

Example:

Terminal #0 - starting my process

    root@d391259bf577:/# cat killmenow
    #!/bin/bash
    while [[ true ]]
    do
        sleep 2
    done

    root@d391259bf577:/# ./killmenow

Terminal #1 - executing my manifest

    root@d391259bf577:/# puppet apply 2-execute_a_command.pp
    Notice: Compiled catalog for d391259bf577.hsd1.ca.comcast.net in environment production in 0.01 seconds
    Notice: /Stage[main]/Main/Exec[killmenow]/returns: executed successfully
    Notice: Finished catalog run in 0.10 seconds
    root@d391259bf577:/#

Terminal #0 - process has been terminated

    root@d391259bf577:/# ./killmenow
    Terminated
    root@d391259bf577:/#

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x0A-configuration_management`
- File: [2-execute_a_command.pp](./2-execute_a_command.pp)

## Files

| File | Description |
|------|-------------|
| [0-create_a_file.pp](./0-create_a_file.pp) | Creates `/tmp/school` (mode 0744, owner/group `www-data`) containing `I love Puppet` |
| [1-install_a_package.pp](./1-install_a_package.pp) | Installs Flask 2.1.0 using `pip3` |
| [2-execute_a_command.pp](./2-execute_a_command.pp) | Runs `pkill killmenow` to kill the process of that name |
| [killmenow](./killmenow) | Helper script that sleeps forever, used as the target for task 2 |

## Author

Sagebeme | :octocat: [GitHub](https://github.com/sagebeme)
