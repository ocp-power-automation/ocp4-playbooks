ocp-customization: OCP post-install customizations
=========

Setup and copy the required files to backup bastion nodes from the master bastion. This module will run post install and customization steps.

Requirements
------------

 - A working OCP 4.X cluster in HA mode
 - More than one bastion hosts, bastion[0] being the master

Role Variables
--------------

| Variable                | Required | Default        | Comments                                    |
|-------------------------|----------|----------------|---------------------------------------------|
| workdir                 | no       | ~/ocp4-workdir | Place for config generation and auth files  |
| bastion_master          | yes      |                | Master bastion host                         |

Dependencies
------------

 - ocp-install

Example Playbook
----------------

    - name: OCP post-install HA
      hosts: bastion[1:]
      roles:
      - ocp-ha
      vars:
        bastion_master: "{{ groups['bastion'][0] }}"

License
-------

See LICENCE.txt

Author Information
------------------

Yussuf Shaikh (yussuf@us.ibm.com)
