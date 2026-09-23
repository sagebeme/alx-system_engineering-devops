# 0x10. HTTPS SSL

## About

**HTTPS and SSL**: how encryption of web traffic works, requesting a certificate, and terminating SSL at the load balancer with HAProxy.

## Learning Objectives

- What SSL certificates are and what SSL termination means
- The purpose of HTTPS and how it differs from HTTP
- How to configure HAProxy for SSL termination
- How to redirect HTTP traffic to HTTPS

### Concepts

For this project, we expect you to look at these concepts: DNS, Web stack debugging.

## Tasks

-----

### 0. HTTPS SSL (certificates, SSL termination)

mandatory

Configure SSL certificates and HTTPS. Run: as per task (e.g. cert generation, nginx/haproxy SSL).

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x10-https_ssl`
-   File: (task configs as per project)

## Files

| File | Description |
|------|-------------|
| [0-world_wide_web](./0-world_wide_web) | Uses `dig` to display the record type and destination of a domain's subdomains (`www`, `lb-01`, `web-01`, `web-02`) |
| [1-haproxy_ssl_termination](./1-haproxy_ssl_termination) | HAProxy configuration with modern TLS defaults and a round-robin backend |
| [100-redirect_http_to_https](./100-redirect_http_to_https) | HAProxy configuration that terminates SSL on port 443 and redirects HTTP to HTTPS (301) |

## Author

Sagebeme | :octocat: [GitHub](https://github.com/sagebeme)
