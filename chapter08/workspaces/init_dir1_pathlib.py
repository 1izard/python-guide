from pathlib import Path
import json
import shutil

obj = {
    "data": [
        {
            "no": 1,
            "datetime": "2020-08-15 20:10:43",
            "category": "Execution",
            "severity": "Middle"
        },
        {
            "no": 2,
            "datetime": "2020-08-16 09:11:41",
            "category": "Persistence",
            "severity": "Low"
        },
        {
            "no": 3,
            "datetime": "2020-08-16 10:27:30",
            "category": "Persistence",
            "severity": "Low"
        }
    ]
}

packages = [
    "autopep8==1.5.4\n",
    "flake8==3.8.3\n",
    "mccabe==0.6.1\n",
    "pycodestyle==2.6.0\n",
    "pyflakes==2.2.0\n",
    "toml==0.10.1\n",
]


dir1 = Path(__file__).parent / "dir1"
if dir1.is_dir():
    shutil.rmtree(str(dir1))
dir1.mkdir()
(dir1 / "file1_1.html").touch()
with open(dir1 / "file1_2.json", "w") as f:
    json.dump(obj, f)
(dir1 / "file1_3.txt").touch()
(dir1 / "file1_4.txt").touch()

dir1_1 = dir1 / "dir1_1"
dir1_1.mkdir()
(dir1_1 / "example.py").touch()
(dir1_1 / "file1_1_1.txt").touch()
(dir1_1 / "file1_1_2.json").touch()

dir1_2 = dir1 / "dir1_2"
dir1_2.mkdir()
(dir1_2 / "file1_2_1.md").touch()
(dir1_2 / "file1_2_2.tar.gz").touch()
(dir1_2 / "file1_2_3.txt").touch()
with open(dir1_2 / "requirements.txt", "w") as f:
    f.writelines(packages)
