# import os
# os.system("python3 detect.py && python3 cimg.py")

import subprocess

subprocess.run("python3 detect.py & python3 cimg.py", shell=True)
