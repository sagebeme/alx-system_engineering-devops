0x00. Shell basics
==================

This project introduces **shell basics**: navigating the filesystem (`cd`, `ls`, `pwd`), creating and removing directories and files (`mkdir`, `rm`, `touch`), and listing in different formats. All tasks are shell commands or scripts.

## Learning Objectives

- What the shell is and how to use it (`cd`, `ls`, `pwd`, `mkdir`, `rm`, `mv`, `cp`, `ln`)
- Relative vs absolute paths, hidden files and long-format listings
- Symbolic links and file types (`file`)
- Reading man pages and using keyboard shortcuts in Bash

Tasks
-----

### 0. Shell basics (tasks 0–15)

mandatory

Each task is a single command or short script that performs a basic shell operation: e.g. print current working path, list files, change directory, create a directory, create an empty file, or list in long format. The goal is to get comfortable with the shell. Run: execute the script (e.g. `./0-current_working_directory`) or run the commands as specified in the task description.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x00-shell_basics`
-   File: (task scripts 0–15 or as per project)

---

**How to run / test**

1. Open a terminal in this directory.
2. Run each script (e.g. `./script_name`) or type the required commands.
3. Verify output against the task requirements (e.g. correct path, files created).

## Task Descriptions

### 0. Where am I?

Write a script that prints the absolute path name of the current working directory.

Example:

```bash
$ ./0-current_working_directory

/0x00-shell_basics
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [0-current_working_directory](./0-current_working_directory)

### 1. What’s in there?

Display the contents list of your current directory.

Example:

```bash
$ ./1-listit
Applications    Documents   Dropbox Movies Pictures
Desktop Downloads   Library Music Public
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [1-listit](./1-listit)

### 2. There is no place like home

Write a script that changes the working directory to the user’s home directory.

* You are not allowed to use any shell variables

```bash
julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ echo $HOME
/home/julien
julien@ubuntu:/tmp$ source ./2-bring_me_home
julien@ubuntu:~$ pwd
/home/julien
julien@ubuntu:~$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [2-bring_me_home](./2-bring_me_home)

### 3. The long format

Display current directory contents in a long format

Example:

```bash
$ ./3-listfiles
total 32
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [3-listfiles](./3-listfiles)

### 4. Hidden files

Display current directory contents, including hidden files (starting with   ` . `  ). Use the long format.

Example:

```bash
$ ./4-listmorefiles
total 32
drwxr-xr-x@ 6 sylvain staff 204 Jan 25 00:29 .
drwxr-xr-x@ 43 sylvain staff 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 sylvain staff 19 Jan 25 00:23 1-listit
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 sylvain staff 18 Jan 25 00:41 4-listmorefiles
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [4-listmorefiles](./4-listmorefiles)

### 5. I love numbers

Display current directory contents.

* Long format

* with user and group IDs displayed numerically

* And hidden files (starting with .)

Example:

```bash
$ ./5-listfilesdigitonly
total 32
drwxr-xr-x@ 6 501 20 204 Jan 25 00:29 .
drwxr-xr-x@ 43 501 20 1462 Jan 25 00:19 ..
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:19 0-current_working_directory
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:23 1-listfiles
-rwxr-xr-x@ 1 501 20 19 Jan 25 00:29 2-bring_me_home
-rwxr-xr-x@ 1 501 20 20 Jan 25 00:39 3-listfiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:41 4-listmorefiles
-rwxr-xr-x@ 1 501 20 18 Jan 25 00:43 5-listfilesdigitonly
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [5-listfilesdigitonly](./5-listfilesdigitonly)

### 6. Welcome

Create a script that creates a directory named   ` my_first_directory `   in the   ` /tmp/ `   directory.

Example:

```bash
$ ./6-firstdirectory
$ file /tmp/my_first_directory/
/tmp/my_first_directory/: directory
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [6-firstdirectory](./6-firstdirectory)

### 7. Betty in my first directory

Move the file   ` betty `   from   ` /tmp/ `   to   ` /tmp/my_first_directory `  .

Example:

```bash
$ ./7-movethatfile
$ ls /tmp/my_first_directory/
betty
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [7-movethatfile](./7-movethatfile)

### 8. Bye bye Betty

Delete the file   ` betty `  .

* The file  ` betty `  is in  ` /tmp/my_first_directory `

Example:

```bash
$ ./8-firstdelete
$ ls /tmp/my_first_directory/
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [8-firstdelete](./8-firstdelete)

### 9. Bye bye My first directory

Delete the directory   ` my_first_directory `   that is in the   ` /tmp `   directory.

Example:

```bash
$ ./9-firstdirdeletion
$ file /tmp/my_first_directory
/tmp/my_first_directory: cannot open `/tmp/my_first_directory' (No such file or directory)
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [9-firstdirdeletion](./9-firstdirdeletion)

### 10. Back to the future

Write a script that changes the working directory to the previous one.

```bash
julien@ubuntu:/tmp$ pwd
/tmp
julien@ubuntu:/tmp$ cd /var
julien@ubuntu:/var$ pwd
/var
julien@ubuntu:/var$ source ./10-back
/tmp
julien@ubuntu:/tmp$ pwd
/tmp
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [10-back](./10-back)

### 11. Lists

Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the   ` /boot `   directory (in this order), in long format.

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [11-lists](./11-lists)

### 12. File type

Write a script that prints the type of the file named   ` iamafile `  . The file   ` iamafile `   will be in the   ` /tmp `   directory when we will run your script.

Example

```bash
ubuntu@ip-172-31-63-244:~$ ./12-file_type
/tmp/iamafile: ELF 64-bit LSB  executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=bd39c07194a778ccc066fc963ca152bdfaa3f971, stripped

```
Note that depending on the file, the output of your script will be different.

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [12-file_type](./12-file_type)

### 13. We are symbols, and inhabit symbols

Create a symbolic link to   ` /bin/ls `  , named   ` __ls__ `  .The symbolic link should be created in the current working directory.

```bash
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 144
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
ubuntu@ip-172-31-63-244:/tmp/sym$./13-symbolic_link
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 144
drwxrwxr-x  2 ubuntu ubuntu   4096 Sep 20 03:24 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:24 ..
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [13-symbolic_link](./13-symbolic_link)

### 14. Copy HTML files

Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

You can consider that all HTML files have the extension   ` .html `

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [14-copy_html](./14-copy_html)

### 100. Let’s move

Create a script that moves all files beginning with an uppercase letter to the directory   ` /tmp/u `  .

You can assume that the directory   ` /tmp/u `   will exist when we will run your script

```bash
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 148
drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 My_file
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 Elif_ym
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la /tmp/u
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
ubuntu@ip-172-31-63-244:/tmp/sym$ ./100-lets_move
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la
total 148
drwxrwxr-x  3 ubuntu ubuntu   4096 Sep 20 03:33 .
drwxrwxrwt 12 root   root   139264 Sep 20 03:26 ..
lrwxrwxrwx  1 ubuntu ubuntu      7 Sep 20 03:24 __ls__ -> /bin/ls
-rw-rw-r--  1 ubuntu ubuntu      0 Sep 20 03:32 random_file
ubuntu@ip-172-31-63-244:/tmp/sym$ ls -la /tmp/u
total 8
drwxrwxr-x 2 ubuntu ubuntu 4096 Sep 20 03:33 .
drwxrwxr-x 3 ubuntu ubuntu 4096 Sep 20 03:33 ..
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 My_file
-rw-rw-r-- 1 ubuntu ubuntu    0 Sep 20 03:32 Elif_ym
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [100-lets_move](./100-lets_move)

### 101. Clean Emacs

Create a script that deletes all files in the current working directory that end with the character   ` ~ `  .

```bash
ubuntu@ip-172-31-63-244:/tmp/sym$ ls
main.c  main.c~  Makefile~
ubuntu@ip-172-31-63-244:/tmp/sym$ ./101-clean_emacs
ubuntu@ip-172-31-63-244:/tmp/emacs$ ls
main.c
ubuntu@ip-172-31-63-244:/tmp/emacs$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [101-clean_emacs](./101-clean_emacs)

### 102. Tree

Create a script that creates the directories   ` welcome/ `  ,   ` welcome/to/ `   and   ` welcome/to/school `   in the current directory.

You are only allowed to use two spaces (and lines) in your script, not more.

```bash
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 44 Sep 20 12:09 102-tree
julien@ubuntu:/tmp/h$ wc -l 102-tree
2 102-tree
julien@ubuntu:/tmp/h$ head -1 102-tree
#!/bin/bash
julien@ubuntu:/tmp/h$ tr -cd ' ' < 102-tree | wc -c # you do not have to understand this yet, but the result should be 2, 1 or 0
2
julien@ubuntu:/tmp/h$ ./102-tree
julien@ubuntu:/tmp/h$ ls
102-tree  welcome
julien@ubuntu:/tmp/h$ ls welcome/
to
julien@ubuntu:/tmp/h$ ls -l welcome/to
total 4
drwxrwxr-x 2 julien julien 4096 Sep 20 12:11 school
julien@ubuntu:/tmp/h$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [102-tree](./102-tree)

### 103. Life is a series of commas, not periods

Write a command that lists all the files and directories of the current directory, separated by commas (  ` , `  ).

* Directory names should end with a slash ( ` / ` )

* Files and directories starting with a dot ( ` . ` ) should be listed

* The listing should be alpha ordered, except for the directories  ` . `  and  ` .. `  which should be listed at the very beginning

* Only digits and letters are used to sort; Digits should come first

* You can assume that all the files we will test with will have at least one letter or one digit

* The listing should end with a new line

```bash
ubuntu@ubuntu:~/$ ls -a

.  ..  0-commas  0-commas-checks  1-empty_casks  2-gifs  3-directories  4-zeros  5-rot13  6-odd  7-sort_rot13  Makefile  quote  .test  test_dir  test.var

ubuntu@ubuntu:~/$ ./103-commas

./, ../, 0-commas, 0-commas-checks/, 1-empty_casks, 2-gifs, 3-directories, 4-zeros, 5-rot13, 6-odd, 7-sort_rot13, Makefile, quote, .test, test_dir/, test.var

ubuntu@ubuntu:~/$
```

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x00-shell_basics`
- File: [103-commas](./103-commas)

## Files

| File | Description |
|------|-------------|
| [0-current_working_directory](./0-current_working_directory) | Prints the absolute path of the current working directory |
| [1-listit](./1-listit) | Lists the contents of the current directory |
| [2-bring_me_home](./2-bring_me_home) | Changes the working directory to the user's home directory |
| [3-listfiles](./3-listfiles) | Lists files in long format |
| [4-listmorefiles](./4-listmorefiles) | Lists all files, including hidden ones, in long format |
| [5-listfilesdigitonly](./5-listfilesdigitonly) | Long-format listing of all files with numeric user and group IDs |
| [6-firstdirectory](./6-firstdirectory) | Creates the directory `/tmp/my_first_directory` |
| [7-movethatfile](./7-movethatfile) | Moves `/tmp/betty` into `/tmp/my_first_directory` |
| [8-firstdelete](./8-firstdelete) | Deletes `betty` from `/tmp/my_first_directory` |
| [9-firstdirdeletion](./9-firstdirdeletion) | Deletes `/tmp/my_first_directory` |
| [10-back](./10-back) | Moves back to the previous directory |
| [11-lists](./11-lists) | Lists the current directory, its parent and `/boot` in long format |
| [12-file_type](./12-file_type) | Prints the type of the file `/tmp/iamafile` |
| [13-symbolic_link](./13-symbolic_link) | Creates a symbolic link `__ls__` pointing to `/bin/ls` |
| [14-copy_html](./14-copy_html) | Copies HTML files into the parent directory, only if new or updated |
| [100-lets_move](./100-lets_move) | Moves all files beginning with an uppercase letter to `/tmp/u` |
| [101-clean_emacs](./101-clean_emacs) | Deletes all files ending with `~` in the current directory |
| [102-tree](./102-tree) | Creates the directory tree `welcome/to/school` |
| [103-commas](./103-commas) | Lists all files (hidden included) separated by commas, directories suffixed with `/` |

## Author

Sagebeme | :octocat: [GitHub](https://github.com/sagebeme)
