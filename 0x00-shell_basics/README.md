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
