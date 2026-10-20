import json
import os
import sys

FILE = "tasks.json"

USAGE = """Usage:
  python3 todo.py add <task text>
  python3 todo.py list
  python3 todo.py done <id>
  python3 todo.py delete <id>"""


def load():
    """Read tasks from the file. Return an empty list if no file yet."""
    if not os.path.exists(FILE):
        return []
    with open(FILE) as f:
        return json.load(f)


def save(tasks):
    """Write tasks to the file."""
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add(text):
    tasks = load()
    new_id = max([t["id"] for t in tasks], default=0) + 1
    tasks.append({"id": new_id, "text": text, "done": False})
    save(tasks)
    print(f"Added task {new_id}: {text}")


def main():
    if len(sys.argv) < 2:
        print(USAGE)
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "add" and args:
        add(" ".join(args))
    else:
        print(USAGE)


if __name__ == "__main__":
    main()
