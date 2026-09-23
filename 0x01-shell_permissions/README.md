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

## Task Descriptions

### 0. My name is Betty

Create a script that switches the current user to the user   ` betty `  .

* You should use exactly 8 characters for your command (+1 character for the new line)

* You can assume that the user  ` betty `  will exist when we will run your script

```bash
julien@ubuntu:/tmp/h$ tail -1 0-iam_betty | wc -c
9
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [0-iam_betty](./0-iam_betty)

### 1. Who am I

Write a script that prints the effective username of the current user.

```bash
julien@ubuntu:/tmp/h$ ./1-who_am_i
julien
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [1-who_am_i](./1-who_am_i)

### 2. Groups

Write a script that prints all the groups the current user is part of.

```bash
julien@ubuntu:/tmp/h$ ./2-groups
julien adm cdrom sudo dip plugdev lpadmin sambashare
julien@ubuntu:/tmp/h$

```

Note: depending on the user, you will get a different output.

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [2-groups](./2-groups)

### 3. New owner

Write a script that changes the owner of the file   ` hello `   to the user   ` betty `  .

```bash
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 julien julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$ sudo ./3-new_owner
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 betty  julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [3-new_owner](./3-new_owner)

### 4. Empty!

Write a script that creates an empty file called   ` hello `  .

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [4-empty](./4-empty)

### 5. Execute

Write a script that adds execute permission to the owner of the file   ` hello `  .

* The file  ` hello `  will be in the working directory

```bash
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:26 5-execute
-rw-rw-r-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./hello
bash: ./hello: Permission denied
julien@ubuntu:/tmp/h$ ./5-execute
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:26 5-execute
-rwxrw-r-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [5-execute](./5-execute)

### 6. Multiple permissions

Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file   ` hello `  .

* The file  ` hello `  will be in the working directory

```bash
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 36 Sep 20 14:31 6-multiple_permissions
-r--r----- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./6-multiple_permissions
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 36 Sep 20 14:31 6-multiple_permissions
-r-xr-xr-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [6-multiple_permissions](./6-multiple_permissions)

### 7. Everybody!

Write a script that adds execution permission to the owner, the group owner and the other users, to the file   ` hello `

* The file  ` hello `  will be in the working directory

* You are not allowed to use commas for this script

```bash
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:35 7-everybody
-rw-r----- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./7-everybody
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:35 7-everybody
-rwxr-x--x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [7-everybody](./7-everybody)

### 8. James Bond

Write a script that sets the permission to the file   ` hello `   as follows:

* Owner: no permission at all

* Group: no permission at all

* Other users: all the permissions

The file   ` hello `   will be in the working directoryYou are not allowed to use commas for this script

```bash
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:40 8-James_Bond
-rwxr-x--x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./8-James_Bond
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:40 8-James_Bond
-------rwx 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [8-James_Bond](./8-James_Bond)

### 9. John Doe

Write a script that sets the mode of the file   ` hello `   to this:

```bash
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello

 ` * The file  ` hello `  will be in the working directory
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [9-John_Doe](./9-John_Doe)

### 10. Look in the mirror

Write a script that sets the mode of the file   ` hello `   the same as   ` olleh `  ’s mode.

* The file  ` hello `  will be in the working directory

* The file  ` olleh `  will be in the working directory

```bash
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$ ./10-mirror_permissions
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rw-rw-r-- 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$

```

Note: the mode of   ` olleh `   will not always be 664. Make sure your script works for any mode.

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [10-mirror_permissions](./10-mirror_permissions)

### 11. Directories

Create a script that adds execute permission to all subdirectories of the current directory for  the owner, the group owner and all other users. Regular files should not be changed.

```bash
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories_permissions
drwx------ 2 julien julien 4096 Sep 20 14:49 dir0
drwx------ 2 julien julien 4096 Sep 20 14:49 dir1
drwx------ 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./11-directories_permissions
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [11-directories_permissions](./11-directories_permissions)

### 12. More directories

Create a script that creates a directory called   ` my_dir `   with permissions 751 in the working directory.

```bash
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   39 Sep 20 14:59 12-directory_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./12-directory_permission s
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   39 Sep 20 14:59 12-directory_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [12-directory_permissions](./12-directory_permissions)

### 13. Change group

Write a script that changes the group owner to   ` school `   for the file   ` hello `

* The file  ` hello `  will be in the working directory

```bash
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   34 Sep 20 15:03 13-change_group
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./13-change_group
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      34 Sep 20 15:03 13-change_group
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien    4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien school   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [13-change_group](./13-change_group)

### 100. Owner and group

Write a script that changes the owner to   ` vincent `   and the group owner to   ` staff `   for all the files and directories in the working directory.

```bash
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   36 Sep 20 15:06 100-change_owner_and_group
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./100-change_owner_and_group
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 vincent staff   36 Sep 20 15:06 100-change_owner_and_group
drwx--x--x 2 vincent staff 4096 Sep 20 14:49 dir0
drwx--x--x 2 vincent staff 4096 Sep 20 14:49 dir1
drwx--x--x 2 vincent staff 4096 Sep 20 14:49 dir2
drwxr-x--x 2 vincent staff 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 vincent staff   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [100-change_owner_and_group](./100-change_owner_and_group)

### 101. Symbolic links

Write a script that changes the owner and the group owner of   ` _hello `   to   ` vincent `   and   ` staff `   respectively.

* The file  ` _hello `  is in the working directory

* The file  ` _hello `  is a symbolic link

```bash
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   44 Sep 20 15:12 101-symbolic_link_permissions
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
lrwxrwxrwx 1 julien julien    5 Sep 20 15:10 _hello -> hello
julien@ubuntu:/tmp/h$ sudo ./101-symbolic_link_permissions
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      44 Sep 20 15:12 101-symbolic_link_permissions
-rw-rw-r-- 1 julien julien      23 Sep 20 14:25 hello
lrwxrwxrwx 1 vincent  staff    5 Sep 20 15:10 _hello -> hello
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [101-symbolic_link_permissions](./101-symbolic_link_permissions)

### 102. If only

Write a script that changes the owner of the file   ` hello `   to   ` vincent `   only if it is owned by the user   ` guillaume `  .

* The file  ` hello `  will be in the working directory

```bash
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien    julien      47 Sep 20 15:18 102-if_only
-rw-rw-r-- 1 guillaume julien      23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./102-if_only
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      47 Sep 20 15:18 102-if_only
-rw-rw-r-- 1 vincent  julien      23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [102-if_only](./102-if_only)

### 103. Star Wars

Write a script that will play the StarWars IV episode in the terminal.

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x01-shell_permissions`
- File: [103-Star_Wars](./103-Star_Wars)

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
