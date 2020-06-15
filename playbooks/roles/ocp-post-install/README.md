ocp-post-install: OCP Post install steps
=========

This module will run all the post install steps. Currently following features are supported:

**1. RHCOS kernel options via MachineConfig**
All the `rhcos_kernel_options` will be applied via MachineConfig to the master and worker nodes. The CRDs will be created at `workdir` and applied to each master and worker node. It will take some minutes to apply the configuration and nodes to be in Ready status again (depends on the number of master and worker nodes). To get the node status run the below command and ensure none of the node is in SchedulingDisabled status before you start using the cluster.

```
oc get nodes
```

Requirements
------------

 - A working OCP 4.X cluster
 - All the nodes should be in Ready status

Role Variables
--------------

| Variable                | Required | Default        | Comments                                    |
|-------------------------|----------|----------------|---------------------------------------------|
| workdir                 | no       | ~/ocp4-workdir | Place for config generation and auth files  |
| rhcos_kernel_options    | no       | []             | List of kernel options for RHCOS nodes      |

Dependencies
------------

 - ocp-install

Example Playbook
----------------

    - name: Post Install OCP
      hosts: bastion
      roles:
      - ocp-post-install

License
-------

See LICENCE.txt

Author Information
------------------

Yussuf Shaikh (yussuf@us.ibm.com)
