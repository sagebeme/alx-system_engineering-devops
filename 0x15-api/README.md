# 0x15. API 

## About

Working with a **REST API** in Python: gathering employee TODO-list data from JSONPlaceholder and exporting it to CSV and JSON.

## Learning Objectives

- What an API is and what REST means
- How to make HTTP requests with `requests`
- How to read and write CSV and JSON files in Python

## Resource

- [Friends don’t let friends program in shell script](https://www.turnkeylinux.org/blog/friends-dont-let-friends-program-shell-script)
- [What is an API](https://www.webopedia.com/definitions/api/)
- [What is an API? In English, please](https://www.freecodecamp.org/news/what-is-an-api-in-english-please-b880a3214a82/)
- [What is a REST API](https://www.sitepoint.com/rest-api/)
- [What are microservices](https://smartbear.com/solutions/microservices/)
- [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://www.python.org/dev/peps/pep-0008/)

## Tasks

-----

### 0. API (gather data from API)

mandatory

Gather data from a REST API (e.g. with Python). Run: as per task (e.g. `python3 script.py`).

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `0x15-api`
-   File: (task scripts as per project)

<details>
<summary><a href="./0-gather_data_from_an_API.py">0. Gather data from an API</a></summary><br>
<a href='https://postimg.cc/N5NpbXMC' target='_blank'><img src='https://i.postimg.cc/8zG9pBVG/image.png' border='0' alt='image'/></a>
</details>

## Task Descriptions

_Tasks not already described above._

### 1. Export to CSV

Using what you did in the task #0, extend your Python script to export data in the CSV format.

Requirements:

*   Records all tasks that are owned by this employee
*   Format must be: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
*   File name must be: `USER_ID.csv`

Example:

    sylvain@ubuntu$ python3 1-export_to_CSV.py 2
    sylvain@ubuntu$ cat 2.csv
    "2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
    "2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
    "2","Antonette","False","et itaque necessitatibus maxime molestiae qui quas velit"
    "2","Antonette","False","adipisci non ad dicta qui amet quaerat doloribus ea"
    "2","Antonette","True","voluptas quo tenetur perspiciatis explicabo natus"
    "2","Antonette","True","aliquam aut quasi"
    "2","Antonette","True","veritatis pariatur delectus"
    "2","Antonette","False","nesciunt totam sit blanditiis sit"
    "2","Antonette","False","laborum aut in quam"
    "2","Antonette","True","nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis"
    "2","Antonette","False","repudiandae totam in est sint facere fuga"
    "2","Antonette","False","earum doloribus ea doloremque quis"
    "2","Antonette","False","sint sit aut vero"
    "2","Antonette","False","porro aut necessitatibus eaque distinctio"
    "2","Antonette","True","repellendus veritatis molestias dicta incidunt"
    "2","Antonette","True","excepturi deleniti adipisci voluptatem et neque optio illum ad"
    "2","Antonette","False","sunt cum tempora"
    "2","Antonette","False","totam quia non"
    "2","Antonette","False","doloremque quibusdam asperiores libero corrupti illum qui omnis"
    "2","Antonette","True","totam atque quo nesciunt"
    sylvain@ubuntu$

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x15-api`
- File: [1-export_to_CSV.py](./1-export_to_CSV.py)

### 2. Export to JSON

Using what you did in the task #0, extend your Python script to export data in the JSON format.

Requirements:

*   Records all tasks that are owned by this employee
*   Format must be: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`
*   File name must be: `USER_ID.json`

Example:

    sylvain@ubuntu$ python3 2-export_to_JSON.py 2
    sylvain@ubuntu$ cat 2.json
    {"2": [{"task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": false, "username": "Antonette"}, {"task": "distinctio vitae autem nihil ut molestias quo", "completed": true, "username": "Antonette"}, {"task": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": false, "username": "Antonette"}, {"task": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": false, "username": "Antonette"}, {"task": "voluptas quo tenetur perspiciatis explicabo natus", "completed": true, "username": "Antonette"}, {"task": "aliquam aut quasi", "completed": true, "username": "Antonette"}, {"task": "veritatis pariatur delectus", "completed": true, "username": "Antonette"}, {"task": "nesciunt totam sit blanditiis sit", "completed": false, "username": "Antonette"}, {"task": "laborum aut in quam", "completed": false, "username": "Antonette"}, {"task": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis", "completed": true, "username": "Antonette"}, {"task": "repudiandae totam in est sint facere fuga", "completed": false, "username": "Antonette"}, {"task": "earum doloribus ea doloremque quis", "completed": false, "username": "Antonette"}, {"task": "sint sit aut vero", "completed": false, "username": "Antonette"}, {"task": "porro aut necessitatibus eaque distinctio", "completed": false, "username": "Antonette"}, {"task": "repellendus veritatis molestias dicta incidunt", "completed": true, "username": "Antonette"}, {"task": "excepturi deleniti adipisci voluptatem et neque optio illum ad", "completed": true, "username": "Antonette"}, {"task": "sunt cum tempora", "completed": false, "username": "Antonette"}, {"task": "totam quia non", "completed": false, "username": "Antonette"}, {"task": "doloremque quibusdam asperiores libero corrupti illum qui omnis", "completed": false, "username": "Antonette"}, {"task": "totam atque quo nesciunt", "completed": true, "username": "Antonette"}]}sylvain@ubuntu$

**Repo:**

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x15-api`
- File: [2-export_to_JSON.py](./2-export_to_JSON.py)

## Files

| File | Description |
|------|-------------|
| [0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py) | Prints an employee's TODO-list progress, given the employee ID |
| [1-export_to_CSV.py](./1-export_to_CSV.py) | Exports an employee's tasks to `USER_ID.csv` |
| [2-export_to_JSON.py](./2-export_to_JSON.py) | Exports an employee's tasks to `USER_ID.json` |

## Author

Sagebeme | :octocat: [GitHub](https://github.com/sagebeme)
