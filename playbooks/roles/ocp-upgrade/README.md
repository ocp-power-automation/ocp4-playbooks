ocp-upgrade: Upgrade OCP cluster
=========

This module will upgrade an existing OCP cluster to a higher version.

Requirements
------------

 - Running OCP 4.x cluster is needed.

Role Variables
--------------

| Variable        | Required | Default    | Comments                                                      |
|-----------------|----------|------------|---------------------------------------------------------------|
| upgrade_version | no       | ""         | Set to a specific version eg. 4.5.4                        |
| upgrade_channel | no       | ""         | Set to channel having required upgrade version available for cluster upgrade (stable-4.x, fast-4.x, candidate-4.x) eg. stable-4.5 |
| pause_time      | no       | 90         | Pauses playbook execution for a set amount of time in minutes |
| delay_time      | no       | 600        | Number of seconds to wait before starting to poll             |

Dependencies
------------

 - None

Example Playbook
----------------

    - name: Upgarde OCP cluster
      hosts: bastion
      tasks:
        - include_role:
            name: ocp-upgrade
          when: upgrade_version != ""

License
-------

See LICENCE.txt

Author Information
------------------

Prajyot Parab (prajyot.parab@ibm.com)

