# from app import test_meeting
# def app():
#     user = test_meeting()
#     return user
# app()

# import requests
import subprocess
from app import test_meeting

os_name = subprocess.run(["lsb_release", "-a"])
print("The exit code was: %d" % os_name.returncode)

def app():
    print("hi success")
app()