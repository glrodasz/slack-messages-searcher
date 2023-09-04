## Install

This project uses `pyenv` to manage dependencies.

1. Install it with `pip install pyenv`
2. Run `pyenv install` to install dependencies.
3. Copy `.env.example` into `.env` and set the slack token.

## How to use

Run the script:

For JSON (default):

```
python script_name.py "your_query_message_here"
```

For CSV:

```
python script_name.py "your_query_message_here" csv
```
