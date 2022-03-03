csi-driver-config: PowerVS Block CSI Driver Configuration
=========

This module will perform necessary configuration on OCP nodes required for CSI Driver installation.

Requirements
------------

 - A working OCP 4.X cluster

Role Variables
--------------

| Variable                       | Required | Default | Comments                                                      |
|--------------------------------|----------|---------|---------------------------------------------------------------|
| service_instance_id            | yes      |         | IBM Cloud PowerVS service instance id.                        |
| region                         | yes      |         | IBM Cloud PowerVS service instance region. eg. mon            |
| zone                           | yes      |         | IBM Cloud PowerVS service instance zone. eg. mon01            |
| masters.name                   | yes      |         | OCP Nodes Master name.                                        |
| masters.id                     | yes      |         | OCP Nodes Master instance id.                                 |
| workers.name                   | yes      |         | OCP Nodes Worker name.                                        |
| workers.id                     | yes      |         | OCP Nodes Worker instance id.                                 |

Dependencies
------------

 - None

Example Playbook
----------------

    - name: CSI Driver configuration
      hosts: bastion
      roles:
      - csi-driver-config

License
-------

See LICENCE.txt

Author Information
------------------

Prajyot Parab (prajyot.parab2@ibm.com)
