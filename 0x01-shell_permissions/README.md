0x01. Shell permissions
=======================

This project practices **file and directory permissions** in the shell: `chmod`, `chown`, `chgrp`, and special modes (e.g. suid). You change permissions and ownership so scripts run correctly or only certain users can access files.

## Learning Objectives

- Users and groups (`su`, `whoami`, `groups`, `id`)
- Changing ownership (`chown`, `chgrp`) and permissions (`chmod`)
- Octal vs symbolic permission modes, and how permissions apply to directories
- The `sudo` command and its use as root

Tasks
-----

### 0. Shell permissions (chmod, chown, chgrp)

mandatory

Use chmod, chown, or chgrp to set permissions or ownership on files/directories. Some tasks require a specific permission (e.g. 755, 644) or suid bit. Run: execute the required command (e.g. `chmod 755 file`) or run a script that applies the change.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x01-shell_permissions`
-   File: (task scripts or commands as per project)

---

**How to run / test**

1. Create or use the files mentioned in the task.
2. Apply the correct `chmod`/`chown` and verify with `ls -l`.

## Files

| File | Description |
|------|-------------|
| [0-iam_betty](./0-iam_betty) | Switches the current user to `betty` |
| [1-who_am_i](./1-who_am_i) | Prints the effective username of the current user |
| [2-groups](./2-groups) | Prints all the groups the current user belongs to |
| [3-new_owner](./3-new_owner) | Changes the owner of the file `hello` to `betty` |
| [4-empty](./4-empty) | Creates an empty file called `hello` |
| [5-execute](./5-execute) | Adds execute permission to the owner of `hello` |
| [6-multiple_permissions](./6-multiple_permissions) | Adds execute for owner and group and read for others on `hello` |
| [7-everybody](./7-everybody) | Adds execute permission to owner, group and others on `hello` |
| [8-James_Bond](./8-James_Bond) | Sets `hello` to mode 007 (no permissions for owner and group, all for others) |
| [9-John_Doe](./9-John_Doe) | Sets `hello` to mode 753 |
| [10-mirror_permissions](./10-mirror_permissions) | Copies the permissions of `olleh` onto `hello` |
| [11-directories_permissions](./11-directories_permissions) | Adds execute permission to all subdirectories of the current directory |
| [12-directory_permissions](./12-directory_permissions) | Creates the directory `my_dir` with mode 751 |
| [13-change_group](./13-change_group) | Changes the group owner of `hello` to `school` |
| [100-change_owner_and_group](./100-change_owner_and_group) | Changes owner to `vincent` and group to `staff` for all files in the directory |
| [101-symbolic_link_permissions](./101-symbolic_link_permissions) | Changes the owner and group of the symbolic link `_hello` itself |
| [102-if_only](./102-if_only) | Changes the owner of `hello` to `betty` only if it is owned by a given user (`--from`) |
| [103-Star_Wars](./103-Star_Wars) | Plays Star Wars in the terminal via `telnet` |

## Author

Sagebeme | :octocat: [GitHub](https://github.com/sagebeme)
