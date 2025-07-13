import time
from glob import glob
from pathlib import Path

from fastglob import glob as cppglob
from rust_glob import glob as rustglob
from nanobind_example import glob as nanoglob

DIR = "data"


def benchmark(opt, recursive=False):
    print(f"{opt:5s}: ", end="")
    start = time.time()

    if opt == "glob":
        a = glob(f"{DIR}/**", recursive=recursive)
    elif opt == "Path":
        if recursive:
            a = list(Path(DIR).glob("**/*"))
        else:
            a = list(Path(DIR).glob("**"))
    elif opt == "cppglob":
        a = cppglob(DIR, recursive=recursive)
    elif opt == "rustglob":
        a = rustglob(DIR, recursive=recursive)

    elif opt == "nanoglob":
        a = nanoglob(DIR, recursive)

    total = time.time() - start
    print(f"{total:.5f}s")


print("Non recursive")
benchmark("glob", recursive=False)
benchmark("Path", recursive=False)
benchmark("cppglob", recursive=False)
benchmark("rustglob", recursive=False)
benchmark("nanoglob", recursive=False)
print()
print("Recursive")
benchmark("glob", recursive=True)
benchmark("Path", recursive=True)
benchmark("cppglob", recursive=True)
benchmark("rustglob", recursive=True)
benchmark("nanoglob", recursive=True)
