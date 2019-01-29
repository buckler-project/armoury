import os
import subprocess as _subprocess

def run_cmd(cmd, subprocess=False, output=True):
    if output:
        print(cmd)

    if subprocess:
        result = _subprocess.getoutput(cmd)
    else:
        os.system(cmd)
        result = ''
    
    return result
