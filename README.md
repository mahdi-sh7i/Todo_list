# To-Do List Application

A simple desktop To-Do List application built with Python and PyQt5. This app allows users to add, delete, clear, and save tasks using a graphical user interface, with persistent storage via SQLite.

## Features

- Add new to-do items
- Delete selected items
- Clear all tasks from the list
- Save the list to a local SQLite database (`t_list.db`)
- Load saved items on startup
- Modal popup confirmation upon saving

## Requirements

- Python 3.x
- PyQt5

Install dependencies via pip if needed:

```bash
pip install PyQt5
```

## Usage

1. Ensure you have the UI file named `todo_c4.ui` and the module `sub.py` containing the `Ui_Dialog` class in the same directory.
2. Run the app using:

```bash
python todo.py
```

3. The GUI will load, and any previously saved tasks will be displayed.
4. Use the interface to manage your task list.

## File Structure

- `todo.py` – Main application file
- `todo_c4.ui` – Qt Designer UI file
- `sub.py` – Contains the `Ui_Dialog` class for popup windows
- `t_list.db` – SQLite database for storing tasks