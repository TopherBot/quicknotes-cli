# quicknotes-cli

A **tiny** Python CLI tool for quickly jotting down notes.

## Features
- Add a note with a single command
- List all saved notes
- Clear all notes

## Installation
```bash
# Clone the repo (or copy the single file)
git clone https://github.com/yourname/quicknotes-cli.git
cd quicknotes-cli

# Make the script executable (optional)
chmod +x quicknotes.py
```

## Usage
```bash
# Add a note
./quicknotes.py add "Buy milk"

# List notes
./quicknotes.py list

# Clear all notes
./quicknotes.py clear
```

The notes are stored in a hidden file `~/.quicknotes.txt`.

## Requirements
- Python 3.6+

---
*Enjoy rapid notetaking without any bloat!*