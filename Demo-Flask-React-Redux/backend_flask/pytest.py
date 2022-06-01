# import requests
import subprocess

os_name = subprocess.run(["lsb_release", "-a"])
print("The exit code was: %d" % os_name.returncode)
