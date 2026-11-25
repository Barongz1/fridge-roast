"""Fridge Roast: One Line, Biggest Laugh — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The roast: the smart fridge updated its firmware and now judges my midnight snacks.
TEXT = "My smart fridge updated its firmware and now judges my midnight snacks. It even locked the ice maker until I finish a salad."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
