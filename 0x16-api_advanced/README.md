# 0x16. API advanced

## About

**Advanced API** work with the Reddit API: querying subreddit information, recursion and counting keywords across hot posts.

## Learning Objectives

- How to read API documentation and authenticate/identify with a custom `User-Agent`
- How to parse JSON results from an API
- How to make recursive API calls with pagination



## Files

| File | Description |
|------|-------------|
| [0-main.py](./0-main.py) | Test file for `0-subs.py` |
| [0-subs.py](./0-subs.py) | `number_of_subscribers(subreddit)`: returns the number of subscribers, or 0 if invalid |
| [1-main.py](./1-main.py) | Test file for `1-top_ten.py` |
| [1-top_ten.py](./1-top_ten.py) | `top_ten(subreddit)`: prints the titles of the first 10 hot posts |
| [2-main.py](./2-main.py) | Test file for `2-recurse.py` |
| [2-recurse.py](./2-recurse.py) | `recurse(subreddit, hot_list)`: recursively returns titles of all hot posts |
| [100-count.py](./100-count.py) | `count_words(subreddit, word_list)`: recursively counts keywords in hot post titles |

## Author

Sagebeme | :octocat: [GitHub](https://github.com/sagebeme)
