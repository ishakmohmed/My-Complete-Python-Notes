import subprocess

# subprocess.call
# subprocess.check_call
# subprocess.check_output

# ^ these are old! new >

# subprocess.run(["python3", "afilethatiwastoolazytocreate.py"]

try:
    completed = subprocess.run(
        ["ls", "-l"], capture_output=True, text=True, check=True)
    # since capture_output=True, it'll be available not in terminal, but stdout!
    completed.args
    # ['ls', '-l']
    completed.returncode
    # returncode 0
    completed.stderr
    # None
    completed.stdout
    # None
except subprocess.CalledProcessError as ex:
    print(ex)
