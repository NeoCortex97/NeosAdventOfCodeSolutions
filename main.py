import pathlib
import subprocess

for directory in sorted(filter(lambda item: item.is_dir(), pathlib.Path(".").iterdir())):
    if directory.name[0].isdigit():
        print(f'{directory.name}:')
        for day in sorted(filter(lambda item: item.is_dir(), directory.iterdir())):
            print(f'  {day.name}:')
            for script in filter(lambda item: item.is_file() and item.suffix.startswith(".py"), day.iterdir()):
                proc = subprocess.Popen(f'python3 {script}'.split(" "), stdout= subprocess.PIPE)
                out, _ = proc.communicate()
                print(f'    {script.name[:-3]}:')
                for line in [l.rstrip() for l in out.decode("utf-8").rstrip().split("\n")]:
                    print(f'      {line}')
