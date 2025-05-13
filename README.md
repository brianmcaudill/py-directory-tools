# py-directory-tools
python tools for working with dirs in windows

I'll help you create a Python script that generates a markdown file with a directory tree structure like your example.



I've created a Python script that generates a directory tree structure and saves it to a markdown file. Here's how to use it:

1. Basic usage:
```bash
python directory_tree.py /path/to/your/directory
```

2. With custom output file:
```bash
python directory_tree.py /path/to/your/directory -o custom_output.md
```

3. With custom ignore patterns:
```bash
python directory_tree.py /path/to/your/directory -i .git node_modules .env
```

The script features:

1. Creates a tree structure similar to your example
2. Automatically ignores common directories like `.git`, `__pycache__`, etc.
3. Supports custom ignore patterns
4. Properly handles Unicode characters
5. Sorts entries (directories first, then files)
6. Uses proper tree characters (├── for items, └── for last items)
7. Adds trailing slashes to directories for better visibility

The output will be saved in a markdown file with the tree structure wrapped in code blocks, making it perfect for documentation.

app/
├── public/                     # Public-facing files
│   ├── assets/                 # Static assets
│   │   ├── css/                # Stylesheets
│   │   ├── js/                 # Client-side scripts
│   │   └── images/             # Image assets
│   ├── index.*                 # Entry point
│   └── .htaccess               # Apache config


