import os

ENTRY = "You have a camera inside you, Wi-Fi, and a touchscreen — yet somehow you still can't tell the milk expired three days ago."
MAX_CHARS = 200  # the gate accepts 1..200 characters


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY.strip())


if __name__ == "__main__":
    main()
