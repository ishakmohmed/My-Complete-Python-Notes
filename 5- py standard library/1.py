from pathlib import Path

Path(r"C:\Program Files\Microsoft")
Path()
Path("ecommerce/__init__.py")
Path() / "ecommerce" / "__init__.py"
Path.home()

path = Path("ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
path.name
path.stem
path.suffix
path.parent
path = path.with_name("file.txt")
path.absolute
path = path.with_suffix(".txt")
print(path)

# ***************************
path.mkdir()
path.rmdir()
path.rename("ecommerce2")

for p in path.iterdir():
  # returns generator object
    print(p)

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)

# limitations of .iterdir()
# - cannot search by pattern
# - doesn't search recursively, so use glob >>>

py_files = [p for p in path.glob("**/*.py")]
# replace .glob with .rglob to search recursively