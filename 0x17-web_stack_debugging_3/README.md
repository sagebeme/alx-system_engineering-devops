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

## Files

| File | Description |
|------|-------------|
| [0-strace_is_your_friend.pp](./0-strace_is_your_friend.pp) | Puppet manifest that fixes `phpp` typos in `wp-settings.php` |

## Author

Sagebeme | :octocat: [GitHub](https://github.com/sagebeme)
