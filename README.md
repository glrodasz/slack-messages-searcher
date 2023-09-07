## Install

This project uses `pyenv` to manage dependencies.

1. Install it with `pip install pyenv`
2. Run `pyenv install` to install dependencies.
3. Copy `.env.example` into `.env` and set an user slack token.

## How to get an user slack token
#### Prerequisites
1. A Slack workspace with enough privileges to install apps. You may need to get in contact with an Admin or Owner on your workspace to be able to do this.
2. Make sure your app has the user scope enable: `search:read`

### Steps
Use postman to authorize and test: https://api.slack.com/tutorials/slack-apps-and-postman

**Note**: Make sure to read "2. Add in the User scopes that you need" section.

## How to use

Run the script:

For JSON (default):

```
python search.py "your_query_message_here"
```

For CSV:

```
python search.py "your_query_message_here" csv
```
