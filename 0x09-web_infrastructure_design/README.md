# 0x09. Web infrastructure design 

## About

**Web infrastructure design**: whiteboard diagrams and written explanations of web stacks, from a single server to a scaled, secured and monitored setup.

## Learning Objectives

- What a web stack is and the role of each component (web server, app server, database, load balancer)
- What a single point of failure (SPOF) is and how to remove it
- Firewalls, HTTPS/SSL and monitoring in a web infrastructure
- How to scale up an infrastructure with clustering and split components

## Resource

- [Web Infrastructure](https://youtu.be/lQNEW76KdYg)
- [What is a database](https://searchdatamanagement.techtarget.com/definition/database)
- [What’s the difference between a web server and an app server?](https://www.youtube.com/watch?v=S97eKyv2b9M)
- [DNS record types](https://pressable.com/?s=DNS&post_type=knowledgebase)
- [Single point of failure](https://en.wikipedia.org/wiki/Single_point_of_failure)
- [How to avoid downtime when deploying new code](https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt#answers-header)
- [High availability cluster (active-active/active-passive)](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA712)
- [What is HTTPS](https://www.instantssl.com/http-vs-https)
- [What is a firewall](https://www.webopedia.com/definitions/firewall/)
- [Load Balancing Algorithms and Techniques](https://kemptechnologies.com/load-balancer/load-balancing-algorithms-techniques/)
- [Active/Passive vs. Active/Active](https://kemptechnologies.com/fr/white-papers/unfog-confusion-active-passive-activeactive-load-balancing/)

## Tasks

<details>
<summary><a href="./0-simple_web_stack.jpg">0. Simple web stack</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/jdk2SN17/image.png' border='0' alt='image'/></a>
<ul>
  <li>Links from screenshot
  <ul>
      <li><a href="https://en.wikipedia.org/wiki/LAMP_%28software_bundle%29">LAMP stack</a></li>
  </ul>
  </li>
</ul>
</details>

<details>
<summary><a href="./1-distributed_web_infrastructure.jpg">1. Distributed web infrastructure</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/MTwSdKn5/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./2-secured_and_monitored_web_infrastructure.jpg">2. Secured and monitored web infrastructure</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/KYsZdtCJ/image.png' border='0' alt='image'/></a>
</details>

<details>
<summary><a href="./3-scale_up.jpg">3. Scale up</a></summary><br>
<a href='https://postimages.org/' target='_blank'><img src='https://i.postimg.cc/13ndnc2x/image.png' border='0' alt='image'/></a>
<ul>
  <li>Links from screenshot
  <ul>
      <li><a href="https://www.nginx.com/resources/glossary/application-server-vs-web-server/">Application server vs web server</a></li>
  </ul>
  </li>
</ul>
</details>

## Task Descriptions

### 0. Simple web stack

Design of a one-server web infrastructure ([diagram](./0-simple_web_stack.pdf)).

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x09-web_infrastructure_design`
- File: [0-simple_web_stack](./0-simple_web_stack)

### 1. Distributed web infrastructure

Three-server infrastructure with a load balancer ([diagram](./1-distributed_web_infrastructure.pdf)).

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x09-web_infrastructure_design`
- File: [1-distributed_web_infrastructure](./1-distributed_web_infrastructure)

### 2. Secured and monitored web infrastructure

Write a script that adds firewalls, an SSL certificate and monitoring clients ([diagram](./2-secured_and_monitored_web_infrastructure.pdf)).

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x09-web_infrastructure_design`
- File: [2-secured_and_monitored_web_infrastructure](./2-secured_and_monitored_web_infrastructure)

### 3. Scale up

Splits components onto their own servers and adds a load-balancer cluster ([diagram](./3-scale_up.pdf)).

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x09-web_infrastructure_design`
- File: [3-scale_up](./3-scale_up)

## Files

| File | Description |
|------|-------------|
| [0-simple_web_stack](./0-simple_web_stack) | Design of a one-server web infrastructure ([diagram](./0-simple_web_stack.pdf)) |
| [1-distributed_web_infrastructure](./1-distributed_web_infrastructure) | Three-server infrastructure with a load balancer ([diagram](./1-distributed_web_infrastructure.pdf)) |
| [2-secured_and_monitored_web_infrastructure](./2-secured_and_monitored_web_infrastructure) | Adds firewalls, an SSL certificate and monitoring clients ([diagram](./2-secured_and_monitored_web_infrastructure.pdf)) |
| [3-scale_up](./3-scale_up) | Splits components onto their own servers and adds a load-balancer cluster ([diagram](./3-scale_up.pdf)) |

## Author

Sagebeme | :octocat: [GitHub](https://github.com/sagebeme)
