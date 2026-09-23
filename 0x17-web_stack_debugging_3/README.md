# 0x17. Web stack debugging #3

## About

Fourth **web stack debugging** project: using `strace` to find why a WordPress site returns a 500 error, and fixing it with Puppet.

## Learning Objectives

- How to use `strace` to trace system calls
- How to find a bad file reference in an application and fix it
- How to automate the fix with Puppet

## Tasks

-----

### 0. Web stack debugging #3

mandatory

Fix broken web stack in container. Run: use Docker and apply fixes as per task.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x17-web_stack_debugging_3`
-   File: (task scripts as per project)

## Task Descriptions

### 0. Strace is your friend

Using `strace`, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

Hint:

*   `strace` can attach to a current running process
*   You can use tmux to run strace in one window and `curl` in another one

Requirements:

*   Your `0-strace_is_your_friend.pp` file must contain Puppet code
*   You can use whatever Puppet resource type you want for you fix

Example:

    root@e514b399d69d:~# curl -sI 127.0.0.1
    HTTP/1.0 500 Internal Server Error
    Date: Fri, 24 Mar 2017 07:32:16 GMT
    Server: Apache/2.4.7 (Ubuntu)
    X-Powered-By: PHP/5.5.9-1ubuntu4.21
    Connection: close
    Content-Type: text/html

    root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
    Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
    Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
    Notice: Finished catalog run in 0.08 seconds
    root@e514b399d69d:~# curl -sI 127.0.0.1:80
    root@e514b399d69d:~#
    HTTP/1.1 200 OK
    Date: Fri, 24 Mar 2017 07:11:52 GMT
    Server: Apache/2.4.7 (Ubuntu)
    X-Powered-By: PHP/5.5.9-1ubuntu4.21
    Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
    Content-Type: text/html; charset=UTF-8

    root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
    <title>Holberton &#8211; Just another WordPress site</title>
    <link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
    <link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
            <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                                <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
            <p>Yet another bug by a Holberton student</p>
    root@e514b399d69d:~#

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x17-web_stack_debugging_3`
- File: [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp)

## Files

| File | Description |
|------|-------------|
| [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp) | Puppet manifest that fixes `phpp` typos in `wp-settings.php` |

## Author

Sagebeme | :octocat: [GitHub](https://github.com/sagebeme)
