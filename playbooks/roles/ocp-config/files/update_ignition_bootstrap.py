import base64
import json
import os

with open('bootstrap.ign', 'r') as f:
    ignition = json.load(f)

files = ignition['storage'].get('files', [])

if os.path.isfile('/tmp/chrony.conf.tmp'):
    with open("/tmp/chrony.conf.tmp", "rb") as chronyconf:
        chrony_b64 = base64.standard_b64encode(chronyconf.read()).decode().strip()
        files.append(
        {
            'path': '/etc/chrony.conf',
            'user': {
                'name': 'root'
            },
            'mode': 420,
            'contents': {
                'source': 'data:text/plain;charset=utf-8;base64,' + chrony_b64,
                'verification': {}
                },
            'filesystem': 'root',
            'overwrite': True
        })

ignition['storage']['files'] = files;

with open('bootstrap.ign', 'w') as f:
    json.dump(ignition, f)
