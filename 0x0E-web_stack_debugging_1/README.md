# 0x0E. Web stack debugging #1 

## About

Second **web stack debugging** project: fixing an Nginx container that is not listening on port 80.

## Learning Objectives

- How to debug a web stack systematically
- Using `netstat`/`ss` and `lsof` to find what is listening on a port
- Reading Nginx configuration and symlinks in `sites-enabled`

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/271/B4eeypV.jpg" />
</p>

## Resource

- [Resources from Web stack debugging #0](https://github.com/iAmG-r00t/alx-system_engineering-devops/tree/main/0x0D-web_stack_debugging_0#resource)


## Tasks

-----

### 0. Web stack debugging #1 (Nginx port 80, short config)

mandatory

Fix Nginx to listen on port 80 and shorten config. Run: use Docker and apply fixes as per task.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x0E-web_stack_debugging_1`
-   File: (task scripts as per project)

<details>
<summary><a href="./0-nginx_likes_port_80">0. Nginx likes port 80</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/43fwt3rJ/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./1-debugging_made_short">1. Make it sweet and short</a></summary><br>
<a href='https://postimg.cc/dDNKGf46' target='_blank'><img src='https://i.postimg.cc/FsNsX5SM/image.png' border='0' alt='image'/></a>
</details>

## Files

| File | Description |
|------|-------------|
| [0-nginx_likes_port_80](./0-nginx_likes_port_80) | Fixes the Nginx config so it listens on port 80 of all active IPv4 addresses |
| [1-debugging_made_short](./1-debugging_made_short) | Same fix as task 0 in as few lines as possible |

## Author

Sagebeme | :octocat: [GitHub](https://github.com/sagebeme)
