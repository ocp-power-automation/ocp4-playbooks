ocp-upgrade: Upgrade OCP cluster
=========

This module will upgrade an existing OCP cluster to a higher version.

Requirements
------------

 - Running OCP 4.x cluster is needed.

Role Variables
--------------

| Variable      | Required | Default | Comments                                                      |
|---------------|----------|---------|---------------------------------------------------------------|
| upgrade_image | no       | ""      | OCP upgrade image                                             |
| pause_time    | no       | 90      | Pauses playbook execution for a set amount of time in minutes |
| delay_time    | no       | 600     | Number of seconds to wait before starting to poll             |

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
          when: upgrade_image!= ""

License
-------

See LICENCE.txt

Author Information
------------------

Prajyot Parab (prajyot.parab@ibm.com)

