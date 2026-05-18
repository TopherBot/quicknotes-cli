#!/usr/bin/env python3
"""quicknotes-cli – a minimal notes manager.

Commands:
  add <text>   Append a note.
  list         Show all notes.
  clear        Delete all notes.
"""
import argparse
import os
import sys

NOTE_FILE = os.path.expanduser('~/.quicknotes.txt')

def ensure_file():
    if not os.path.exists(NOTE_FILE):
        open(NOTE_FILE, 'a').close()

def add_note(text: str) -> None:
    with open(NOTE_FILE, 'a', encoding='utf-8') as f:
        f.write(text.rstrip('\n') + '\n')
    print('Note added.')

def list_notes() -> None:
    ensure_file()
    with open(NOTE_FILE, 'r', encoding='utf-8') as f:
        notes = [line.rstrip('\n') for line in f]
    if not notes:
        print('No notes found.')
        return
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")

def clear_notes() -> None:
    open(NOTE_FILE, 'w').close()
    print('All notes cleared.')

def main():
    parser = argparse.ArgumentParser(prog='quicknotes', description='Tiny notes manager')
    subparsers = parser.add_subparsers(dest='cmd', required=True)

    add_parser = subparsers.add_parser('add', help='Add a new note')
    add_parser.add_argument('text', nargs='+', help='Text of the note')

    subparsers.add_parser('list', help='List all notes')
    subparsers.add_parser('clear', help='Delete all notes')

    args = parser.parse_args()

    if args.cmd == 'add':
        add_note(' '.join(args.text))
    elif args.cmd == 'list':
        list_notes()
    elif args.cmd == 'clear':
        clear_notes()
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    main()
