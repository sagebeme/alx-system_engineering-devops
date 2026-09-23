# 0x0C. Web server

## About

**Web servers**: transferring files with `scp`, installing and configuring **Nginx**, setting up a domain name, redirects and a custom 404 page.

## Learning Objectives

- What a web server is and how DNS (A records) points a domain at it
- How to transfer files with `scp` and configure Nginx
- How to configure a redirect (`301`) and a custom `404` page
- How to automate an Nginx setup with Puppet

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png" />
</p>

## Resource

<details>
<summary><a href="https://www.gnu.org/software/libc/manual/html_node/Processes.html#Processes">Child Process</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/bw6hYBS5/image.png' border='0' alt='image'/></a>
</details>

- [Background contenxt](https://www.youtube.com/watch?v=AZg4uJkEa-4)
- [How the web works](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/How_the_Web_works)
- [Nginx](https://en.wikipedia.org/wiki/Nginx)
- [How to Configure Nginx](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-server-blocks-virtual-hosts-on-ubuntu-16-04)
- [Root and sub domain](https://landingi.com/help/domains-vs-subdomains/)
- [HTTP requests](https://www.tutorialspoint.com/http/http_methods.htm)
- [HTTP redirection](https://moz.com/learn/seo/redirection)
- [Not found HTTP response code](https://en.wikipedia.org/wiki/HTTP_404)
- [Logs files on Linux](https://www.cyberciti.biz/faq/ubuntu-linux-gnome-system-log-viewer/)
- [RFC 7231 (HTTP/1.1)](https://datatracker.ietf.org/doc/html/rfc7231)
- [RFC 7540 (HTTP/2)](https://datatracker.ietf.org/doc/html/rfc7540)

## Tasks

-----

### 0. Web server (transfer, nginx, domain, redirection, 404)

mandatory

Transfer files, install nginx, set up domain, redirection, and custom 404. Run: as per task (e.g. `curl`, `nginx`).

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x0C-web_server`
-   File: (task scripts as per project)

<details>
<summary><a href="./0-transfer_file">0. Transfer a file to your server</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/j2P4SmgY/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./1-install_nginx_web_server">1. Install nginx web server</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/QMbf1FrY/image.png' border='0' alt='image'/></a>
<a href='https://postimg.cc/621fsx68' target='_blank'><img src='https://i.postimg.cc/vTGqVGpt/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./2-setup_a_domain_name">2. Setup a domain name</a></summary><br>
<a href='https://postimg.cc/svdGgYqp' target='_blank'><img src='https://i.postimg.cc/L6htvvV0/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./3-redirection">3. Redirection</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/tTmZ8GqZ/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./4-not_found_page_404">4. Not found page 404</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/zvhdBrG6/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./7-puppet_install_nginx_web_server.pp">5. Install Nginx web server (w/ Puppet)</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/Vs2dxb0D/image.png' border='0' alt='image'/></a>
</details>

## Files

| File | Description |
|------|-------------|
| [0-transfer_file](./0-transfer_file) | Transfers a file to a server with `scp` (path, IP, username, SSH key as arguments) |
| [1-install_nginx_web_server](./1-install_nginx_web_server) | Installs Nginx and serves `Hello World!` on port 80 |
| [2-setup_a_domain_name](./2-setup_a_domain_name) | The domain name pointing to the server |
| [3-redirection](./3-redirection) | Configures `/redirect_me` as a 301 redirect |
| [4-not_found_page_404](./4-not_found_page_404) | Configures a custom 404 page containing `Ceci n'est pas une page` |
| [7-puppet_install_nginx_web_server.pp](./7-puppet_install_nginx_web_server.pp) | Installs Nginx with Puppet: `Hello World!` page and the `/redirect_me` 301 redirect |

## Author

Sagebeme | :octocat: [GitHub](https://github.com/sagebeme)
