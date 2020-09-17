import os
import shutil
import json


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


dir1 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dir1")
if os.path.isdir(dir1):
    shutil.rmtree(dir1)
os.mkdir(dir1)
open(os.path.join(dir1, "file1_1.html"), "x")
with open(os.path.join(dir1, "file1_2.json"), "w") as f:
    json.dump(obj, f)
open(os.path.join(dir1, "file1_3.txt"), "x")
open(os.path.join(dir1, "file1_4.txt"), "x")

dir1_1 = os.path.join(dir1, "dir1_1")
os.mkdir(dir1_1)
open(os.path.join(dir1_1, "example.py"), "x")
open(os.path.join(dir1_1, "file1_1_1.txt"), "x")
open(os.path.join(dir1_1, "file1_1_2.json"), "x")

dir1_2 = os.path.join(dir1, "dir1_2")
os.mkdir(dir1_2)
open(os.path.join(dir1_2, "file1_2_1.md"), "x")
open(os.path.join(dir1_2, "file1_2_2.tar.gz"), "x")
open(os.path.join(dir1_2, "file1_2_3.txt"), "x")
with open(os.path.join(dir1_2, "requirements.txt"), "w") as f:
    f.writelines(packages)
