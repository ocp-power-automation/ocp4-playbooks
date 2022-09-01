cluster-health-check: Checks cluster health
=========

This role can be used for checking cluster operators and nodes are in good state.

Requirements
------------

- OCP Cluster

Role Variables
--------------

- None

Dependencies
------------

 - None


Example Playbook
----------------

```
- name: Check cluster health
  hosts: bastion
  tasks:
  - name: Check if cluster operators and nodes are healthy
    include_role:
      name: playbooks/roles/cluster-health-check
```

License
-------

See LICENCE.txt

Author Information
------------------

Varad Ahirwadkar (varad.ahirwadkar@ibm.com)
