#!/usr/bin/env python3
import subprocess

#subprocess.run(["ls -l"], shell=True)

oops = subprocess.check_call(["ls -l"], shell=True)

print(oops)

if oops == 0:
    subprocess.run(["ls"], shell=True)