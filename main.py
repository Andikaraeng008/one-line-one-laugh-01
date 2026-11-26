import os

LINE = "The plumber fixed the leak and billed the puddle for therapy."

# Gate: entry must be UTF-8 text of 1 to 200 characters, not only whitespace.
assert 1 <= len(LINE) <= 200 and LINE.strip(), "entry violates the 1-200 character gate"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
