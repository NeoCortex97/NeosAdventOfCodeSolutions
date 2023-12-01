import pathlib
import subprocess

for directory in filter(lambda item: item.is_dir(), pathlib.Path(".").iterdir()):
    if directory.name[0].isdigit():
        for day in filter(lambda item: item.is_dir(), directory.iterdir()):
            for script in filter(lambda item: item.is_file() and item.suffix.startswith(".py"), day.iterdir()):
                proc = subprocess.Popen(f'python3 {script}'.split(" "), stdout= subprocess.PIPE)
                out, _ = proc.communicate()
                print(script, out.decode("utf-8").rstrip())
