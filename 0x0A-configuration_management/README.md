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

## Files

| File | Description |
|------|-------------|
| [0-create_a_file.pp](./0-create_a_file.pp) | Creates `/tmp/school` (mode 0744, owner/group `www-data`) containing `I love Puppet` |
| [1-install_a_package.pp](./1-install_a_package.pp) | Installs Flask 2.1.0 using `pip3` |
| [2-execute_a_command.pp](./2-execute_a_command.pp) | Runs `pkill killmenow` to kill the process of that name |
| [killmenow](./killmenow) | Helper script that sleeps forever, used as the target for task 2 |

## Author

Sagebeme | :octocat: [GitHub](https://github.com/sagebeme)
