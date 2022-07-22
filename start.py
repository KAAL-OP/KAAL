import os 
import subprocess
from logging import DEBUG, INFO, basicConfig, getLogger, warning
basicConfig(format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=INFO)
LOGS = getLogger("Helper")
os.system("git clone https://gitHub.com/kaal-op/KAAL && cd KAAL && python3 -m KAALX")
os.chdir("KAALX")
process = subprocess.Popen(
        ["python3", "-m", "KAALX"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,)
out, er = process.communicate()
if er:
    LOGS.warning(er.decode())
print("::::::::::::::")
if out:
    LOGS.info(out.decode())
