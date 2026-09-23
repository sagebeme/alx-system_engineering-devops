0x02. Shell redirections
========================

This project practices **shell redirections**: redirecting standard input, output, and error (e.g. `>`, `>>`, `<`, `|`, `2>`). You write commands and scripts that use redirection and pipes.

## Learning Objectives

- Redirecting stdin, stdout and stderr (`>`, `>>`, `<`, `|`)
- Displaying and slicing files with `cat`, `head` and `tail`
- Filtering and transforming text with `sort`, `uniq`, `grep`, `tr` and `cut`
- Finding files with `find` and escaping special characters in the shell

Tasks
-----

### 0. Shell redirections (tasks 0–n)

mandatory

Each task uses redirection or pipes: echo to file, cat, head, tail, find with exec, wc, and similar. Run: execute the required command or script as specified in the task description.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x02-shell_redirections`
-   File: (task scripts/commands as per project)

## Files

| File | Description |
|------|-------------|
| [0-hello_world](./0-hello_world) | Prints `Hello, World` |
| [1-confused_smiley](./1-confused_smiley) | Displays a confused smiley `"(Ôo)'` |
| [2-hellofile](./2-hellofile) | Displays the content of `/etc/passwd` |
| [3-twofiles](./3-twofiles) | Displays the content of `/etc/passwd` and `/etc/hosts` |
| [4-lastlines](./4-lastlines) | Displays the last 10 lines of `/etc/passwd` |
| [5-firstlines](./5-firstlines) | Displays the first 10 lines of `/etc/passwd` |
| [6-third_line](./6-third_line) | Displays the third line of the file `iacta` |
| [7-file](./7-file) | Creates a file whose name is a string of special characters, containing `Best School` |
| [8-cwd_state](./8-cwd_state) | Writes the long listing of the current directory to `ls_cwd_content` |
| [9-duplicate_last_line](./9-duplicate_last_line) | Duplicates the last line of `iacta` |
| [10-no_more_js](./10-no_more_js) | Deletes all `.js` files in the current directory and subdirectories |
| [11-directories](./11-directories) | Counts the number of directories and subdirectories (hidden included, `.` excluded) |
| [12-newest_files](./12-newest_files) | Displays the 10 newest files, newest first |
| [13-unique](./13-unique) | Prints only the lines that appear once in the input |
| [14-findthatword](./14-findthatword) | Displays lines of `/etc/passwd` containing `root` |
| [15-countthatword](./15-countthatword) | Counts lines of `/etc/passwd` containing `bin` (case-insensitive) |
| [16-whatsnext](./16-whatsnext) | Displays lines containing `root` plus the 3 lines after each match |
| [17-hidethisword](./17-hidethisword) | Displays lines of `/etc/passwd` that do not contain `bin` |
| [18-letteronly](./18-letteronly) | Displays lines of `/etc/ssh/sshd_config` starting with a letter |
| [19-AZ](./19-AZ) | Replaces `A` with `Z` and `c` with `e` from stdin |
| [20-hiago](./20-hiago) | Removes the letters `c` and `C` from stdin |
| [21-reverse](./21-reverse) | Reverses its input |
| [22-users_and_homes](./22-users_and_homes) | Displays usernames and home directories from `/etc/passwd`, sorted |
| [100-empty_casks](./100-empty_casks) | Finds all empty files and directories in the current directory tree |
| [101-gifs](./101-gifs) | Lists all `.gif` files (extension removed), sorted case-insensitively |
| [102-acrostic](./102-acrostic) | Decodes an acrostic by joining the first letter of each line |
| [103-the_biggest_fan](./103-the_biggest_fan) | Lists the 11 most frequent entries in the first column of a tab-separated file (header skipped) |

## Author

Sagebeme | :octocat: [GitHub](https://github.com/sagebeme)
