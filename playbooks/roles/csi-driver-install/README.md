csi-driver-install: PowerVS Block CSI Driver Installation
=========

This module will perform necessary configuration on OCP nodes required for CSI Driver installation.

Requirements
------------

 - A working OCP 4.X cluster

Role Variables
--------------

| Variable                       | Required | Default  | Comments                                                      |
|--------------------------------|----------|----------|---------------------------------------------------------------|
| csi_driver_type                | no       | `stable` | Set to csi-driver type. Refers to the stable state of upstream ibm-powervs-block-csi-driver deployment code. Upstream ibm-powervs-block-csi-driver url - `https://github.com/kubernetes-sigs/ibm-powervs-block-csi-driver/deploy/kubernetes/overlays/{csi_driver_type}/?ref={csi_driver_version}`                                   |
| csi_driver_version             | no       | `v0.1.0` | Set to csi-driver version. Refers to the version of the stable upstream ibm-powervs-block-csi-driver deployment code. Upstream ibm-powervs-block-csi-driver url - `https://github.com/kubernetes-sigs/ibm-powervs-block-csi-driver/deploy/kubernetes/overlays/{csi_driver_type}/?ref={csi_driver_version}`                                  |
| service_instance_id            | yes      |          | IBM Cloud PowerVS service instance id.                        |
| region                         | yes      |          | IBM Cloud PowerVS service instance region. eg. mon            |
| zone                           | yes      |          | IBM Cloud PowerVS service instance zone. eg. mon01            |
| masters.name                   | yes      |          | OCP Nodes Master name.                                        |
| masters.id                     | yes      |          | OCP Nodes Master instance id.                                 |
| workers.name                   | yes      |          | OCP Nodes Worker name.                                        |
| workers.id                     | yes      |          | OCP Nodes Worker instance id.                                 |

Dependencies
------------

- Export the IBM Cloud API Key

```
$ set +o history
$ export IBMCLOUD_API_KEY='<your API key>'
$ set -o history
```

Example Playbook
----------------

- name: CSI Driver installation
  hosts: bastion[0]
  tasks:
    - include_role:
        name: csi-driver-install
      vars:
        IBMCLOUD_API_KEY: (lookup('env', 'IBMCLOUD_API_KEY')
      when: (lookup('env', 'IBMCLOUD_API_KEY') != "")

License
-------

See LICENCE.txt

Author Information
------------------

Prajyot Parab (prajyot.parab2@ibm.com)
