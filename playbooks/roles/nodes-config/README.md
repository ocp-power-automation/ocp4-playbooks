nodes-config: OCP Cluster Nodes Configuration
=========

This module will wait for ssh connection to the cluster nodes/machines (RHCOS). Once connected will configure settings as given in the task 'Configure cluster nodes'.

Requirements
------------

 - The cluster machines should be created manually or using IaC tools such as Terraform.
 - Inventory should have host groups named bootstrap, masters, workers.
 - Only 'core' user is allowed to ssh to the cluster nodes.
 - OCP install configuration should be created and the machines should be ignited before running this role.
 - Connection will timeout after 45 minutes (configurable).

Role Variables
--------------

| Variable                | Required | Default        | Comments                                    |
|-------------------------|----------|----------------|---------------------------------------------|
| node_connection_timeout | no       | 2700           | Maximum number of seconds to wait for       |

Dependencies
------------

 - ocp-config

Example Playbook
----------------

    - name: Check and configure control-plane nodes
      hosts: bootstrap, masters
      gather_facts: no
      roles:
      - nodes-config

License
-------

See LICENCE.txt

Author Information
------------------

Yussuf Shaikh (yussuf@us.ibm.com)
