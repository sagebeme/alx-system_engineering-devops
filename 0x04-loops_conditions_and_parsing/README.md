# Loops, conditions and parsing

In this project, I worked on loops and conditionals statements in Bash.

## Learning Objectives

- How to create SSH keys
- The advantage of `#!/usr/bin/env bash` over `#!/bin/bash`
- Using `while`, `until` and `for` loops
- Using `if`, `else`, `elif` and `case` statements
- Using the `cut` command and file/comparison operators

Tasks
-----

### 0. Loops and parsing (RSA key, for/while/until, conditions, log parsing)

mandatory

Create SSH RSA key, write for/while/until loops, use if/elif/else, and parse apache-access.log in tasks 102–103. Run: `./script` or as per task.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x04-loops_conditions_and_parsing`
-   File: (task scripts as per project)

## Helper File :raised_hands:

* [apache-access.log](./apache-access.log): An Apache access log file parsed in tasks `102` and `103`.

## Tasks :page_with_curl:

* **0. Create a SSH RSA key pair**
  * [0-RSA_public_key.pub](./0-RSA_public_key.pub): A public SSH key uploaded for the purposes of School.

* **1. For Best School loop**
  * [1-for_Best_school](./1-for_best_school): Bash script that displays `Best School` 10 times using a `for` loop.

* **2. While Best School loop**
  * [2-while_Best_school](./2-while_best_school): Bash script that displays `Best School` 10 times using a `while` loop.

* **3. Until Best School loop**
  * [3-until_Best_school](./3-until_best_school): Bash script that displays `Best School` 10 times using an `until` loop.

* **4. If 9, say Hi!**
  * [4-if_9_say_hi](./4-if_9_say_hi): Bash script that displays `Best School` 10 times using a `while` loop.
  * For the 9th iteration, displays `Best School` and then `Hi` on a new line.
  * Uses an `if` statement.

* **5. 4 bad luck, 8 is your chance**
  * [5-4_bad_luck_8_is_your_chance](./5-4_bad_luck_8_is_your_chance): Bash script that loops from 1 to 10 using a `while` loop and:
    * Displays `bad luck` on the 4th iteration.
    * Displays `good luck` on the 8th iteration.
    * Displays `Best School` for all other iterations.
  * Uses the `if`, `elif`, and `else` statements.

* **6. Superstitious numbers**
  * [6-superstitious_numbers](./6-superstitious_numbers): Bash script that displays numbers from `1` to `20` using a `while` loop and:
    * Displays `4` and then `bad luck from China` for the 4th iteration.
    * Displays `9` and then `bad luck from Japan` for the 9th iteration.
    * Displays `17` and then `bad luck from Italy` for the 17th iteration.
  * Uses a `case` statement.

* **7. Clock**
  * [7-clock](./7-clock): Bash script that displays the time for 12 hours and 59 minutes.
    * Displays hours from `0` to `12`.
    * Displays minutes from `0` to `59`.

* **8. For ls**
  * [8-for_ls](./8-for_ls): Bash script that displays the contents of the current directory in list format.
  * Only the part of the name after the first dash is displayed.

* **9. To file, or not to file**
  * [9-to_file_or_not_to_file](./9-to_file_or_not_to_file): Bash script that gives information  about the `school` file.
    * If the file exists, displays: `school file exists`.
    * If the file does not exist, displays: `school file does not exist`.
    * If the file exists and is empty, displays: `school file is empty`.
    * If the file exists and is not empty, displays: `school file is not empty`.
    * If the file exists and is a regular file, displays: `school file is a regular file`.
    * Otherwise, displays nothing.

## Files

| File | Description |
|------|-------------|
| [0-RSA_public_key.pub](./0-RSA_public_key.pub) | Public key of an RSA key pair created for the project |
| [1-for_best_school](./1-for_best_school) | Displays `Best School` 10 times using a `for` loop |
| [2-while_best_school](./2-while_best_school) | Displays `Best School` 10 times using a `while` loop |
| [3-until_best_school](./3-until_best_school) | Displays `Best School` 10 times using an `until` loop |
| [4-if_9_say_hi](./4-if_9_say_hi) | Displays `Best School` 10 times, printing `Hi` after the 9th |
| [5-4_bad_luck_8_is_your_chance](./5-4_bad_luck_8_is_your_chance) | Loops 1–10 printing `bad luck` on the 4th, `good luck` on the 8th and `Best School` otherwise |
| [6-superstitious_numbers](./6-superstitious_numbers) | Loops 1–20 with a `case` statement: `bad luck from China/Japan/Italy` on the 4th, 9th and 17th |
| [7-clock](./7-clock) | Displays the time for 12 hours and 59 minutes |
| [8-for_ls](./8-for_ls) | Lists the current directory showing only the part of each name after the first dash |
| [9-to_file_or_not_to_file](./9-to_file_or_not_to_file) | Reports whether `school` exists, is empty, and whether it is a regular file |
| [10-fizzbuzz](./10-fizzbuzz) | Prints 1–100 with `Fizz`, `Buzz` and `FizzBuzz` substitutions |
| [100-read_and_cut](./100-read_and_cut) | Displays username, user id and home directory from `/etc/passwd` |
| [101-tell_the_story_of_passwd](./101-tell_the_story_of_passwd) | Tells the story of each `/etc/passwd` line using `while` and `IFS` |
| [102-lets_parse_apache_logs](./102-lets_parse_apache_logs) | Displays visitor IP and HTTP status code from an Apache log |
| [103-dig_the-data](./103-dig_the-data) | Groups visitors by IP and status code, sorted by occurrences |

## Author

Sagebeme | :octocat: [GitHub](https://github.com/sagebeme)
