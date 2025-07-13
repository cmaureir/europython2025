from pathlib import Path

NUM_DIRECTORIES = 100
NUM_FILES = 100

DATA_DIR = Path("data_small")
DATA_DIR.mkdir(exist_ok=True)

for d in range(NUM_DIRECTORIES):
    dir_name = DATA_DIR / Path(f"dir{d}")
    print("Creating directory:", dir_name)
    dir_name.mkdir(exist_ok=True)
    for f in range(NUM_FILES):
        file_name = Path(f"file{f}")
        with open(dir_name / file_name, "w") as f:
            f.write("holi\n")
