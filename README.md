# ALX System engineering & DevOps

This repository contains **system engineering and DevOps** projects: shell basics, permissions, redirections, variables, loops, processes and signals, regular expressions, networking, web infrastructure design, configuration management (Puppet), SSH, web server, load balancer, HTTPS/SSL, debugging, firewall, MySQL, API, monitoring, and application server. Each folder is a project; this README explains what each folder is for, what the main files do, and how to run the exercises.

## Structure

* [0x00. Shell basics](./0x00-shell_basics)
* [0x01. Shell permissions](./0x01-shell_permissions)
* [0x02. Shell redirections](./0x02-shell_redirections)
* [0x03. Shell variables & expansions](./0x03-shell_variables_expansions)
* [0x04. Loops, conditions and parsing](./0x04-loops_conditions_and_parsing)
* [0x05. Processes and signals](./0x05-processes_and_signals)
* [0x06. Regular expressions](./0x06-regular_expressions)
* [0x07. Networking basics](./0x07-networking_basics)
* [0x08. Networking basics #2](./0x08-networking_basics_2)
* [0x09. Web infrastructure design](./0x09-web_infrastructure_design)
* [0x0A. Configuration management](./0x0A-configuration_management)
* [0x0B. SSH](./0x0B-ssh)
* [0x0C. Web server](./0x0C-web_server)
* [0x0D. Web stack debugging #0](./0x0D-web_stack_debugging_0)
* [0x0E. Web stack debugging #1](./0x0E-web_stack_debugging_1)
* [0x0F. Load balancer](./0x0F-load_balancer)
* [0x10. HTTPS/SSL](./0x10-https_ssl)
* [0x11. What happens when you type google.com](./0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_ente)
* [0x12. Web stack debugging #2](./0x12-web_stack_debugging_2)
* [0x13. Firewall](./0x13-firewall)
* [0x14. MySQL](./0x14-mysql)
* [0x15. API](./0x15-api)
* [0x16. API advanced](./0x16-api_advanced)
* [0x17. Web stack debugging #3](./0x17-web_stack_debugging_3)
* [0x18. Webstack monitoring](./0x18-webstack_monitoring)
* [0x1A. Application server](./0x1A-application_server)
* [0x1B. Web stack debugging #4](./0x1B-web_stack_debugging_4)
* [command_line_for_the_win](./command_line_for_the_win)
* [attack_is_the_best_defense](./attack_is_the_best_defense)

| Folder | Topic | What you'll practice |
|--------|-------|----------------------|
| [0x00-shell_basics](./0x00-shell_basics) | Shell basics | cd, ls, pwd, mkdir, etc. |
| [0x01-shell_permissions](./0x01-shell_permissions) | Permissions | chmod, chown, suid |
| [0x02-shell_redirections](./0x02-shell_redirections) | Redirections | stdin/stdout, pipes |
| [0x03-shell_variables_expansions](./0x03-shell_variables_expansions) | Variables | env, export, expansion |
| [0x04-loops_conditions_and_parsing](./0x04-loops_conditions_and_parsing) | Loops & parsing | while, if, parsing |
| [0x05-processes_and_signals](./0x05-processes_and_signals) | Processes | ps, kill, signals |
| [0x06-regular_expressions](./0x06-regular_expressions) | Regex | grep, sed, regex |
| [0x07-networking_basics](./0x07-networking_basics) | Networking | OSI, TCP/IP, curl |
| [0x08-networking_basics_2](./0x08-networking_basics_2) | Networking #2 | DNS, DHCP, etc. |
| [0x09-web_infrastructure_design](./0x09-web_infrastructure_design) | Infra design | Diagrams, LAMP |
| [0x0A-configuration_management](./0x0A-configuration_management) | Config mgmt | Puppet |
| [0x0B-ssh](./0x0B-ssh) | SSH | Keys, config |
| [0x0C-web_server](./0x0C-web_server) | Web server | Nginx, Apache |
| [0x0D-web_stack_debugging_0](./0x0D-web_stack_debugging_0) | Debugging | Debug containers |
| [0x0E-web_stack_debugging_1](./0x0E-web_stack_debugging_1) | Debugging #1 | More debugging |
| [0x0F-load_balancer](./0x0F-load_balancer) | Load balancer | HAProxy |
| [0x10-https_ssl](./0x10-https_ssl) | HTTPS/SSL | Certificates, Nginx SSL |
| [0x11-what_happens...](./0x11-what_happens_when_your_type_google_com_in_your_browser_and_press_ente) | DNS & browser | End-to-end flow |
| [0x12-web_stack_debugging_2](./0x12-web_stack_debugging_2) | Debugging #2 | Debug stack |
| [0x13-firewall](./0x13-firewall) | Firewall | ufw, iptables |
| [0x14-mysql](./0x14-mysql) | MySQL | DB setup, replication |
| [0x15-api](./0x15-api) | API | REST, HTTP |
| [0x16-api_advanced](./0x16-api_advanced) | API advanced | Pagination, auth |
| [0x17-web_stack_debugging_3](./0x17-web_stack_debugging_3) | Debugging #3 | Debug stack |
| [0x18-webstack_monitoring](./0x18-webstack_monitoring) | Monitoring | Datadog, logs |
| [0x1A-application_server](./0x1A-application_server) | App server | Gunicorn, systemd |
| [0x1B-web_stack_debugging_4](./0x1B-web_stack_debugging_4) | Debugging #4 | Debug stack |
| [command_line_for_the_win](./command_line_for_the_win) | CLI challenge | Bash commands |
| [attack_is_the_best_defense](./attack_is_the_best_defense) | Security | Network attacks/defense |

## Prerequisites

- Linux (Ubuntu recommended), shell, SSH
- Docker (for many debugging tasks)
- MySQL, Nginx, Puppet as per project

## Quick reference

- Run scripts as in each folder's README (often `./script` or `bash script`).
