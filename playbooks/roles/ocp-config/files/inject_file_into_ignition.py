import base64
import json
import os
import sys

# inject_file_into_ignition.py
#
# Update an ignition file with a file to be added onto a target host.
# Usage:  python3 inject_file_into_ignition.py <ignition> <file> <path>
# ignition: Path to ignition file to be updated.
# file: File to be injected.
# path: Full path to place the new file on the target host, including
# the file name.

with open(str(sys.argv[1]), 'r') as f:
    ignition = json.load(f)

if os.path.isfile(sys.argv[2]):
    cfg = open(str(sys.argv[2]), 'rb')
    cfg_b64 = base64.standard_b64encode(cfg.read()).decode().strip()
else:
    print("File:", sys.argv[2], "not found - skipping")
    sys.exit(0)

if 'storage' not in ignition:
    newfile =( { "files": [
        {
            'path': str(sys.argv[3]),
            'user': {
                'name': 'root'
            },
            'mode': 420,
            'contents': {
                'source': 'data:text/plain;charset=utf-8;base64,' + cfg_b64 }
         }]} )

    ignition["storage"]=newfile

else:
    files = ignition['storage'].get('files', [])
    files.append(
        {
            'path': str(sys.argv[3]),
            'user': {
                'name': 'root'
            },
            'mode': 420,
            'contents': {
                'source': 'data:text/plain;charset=utf-8;base64,' + cfg_b64,
                'verification': {}
                },
            'overwrite': True
        })

# debuging
# json.dump(ignition, sys.stdout, indent=4)

print("Updating:",sys.argv[1]);
with open(sys.argv[1], 'w') as f:
     json.dump(ignition, f)
