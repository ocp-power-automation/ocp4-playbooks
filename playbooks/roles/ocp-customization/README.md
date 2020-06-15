ocp-customization: OCP post-install customizations
=========

This module will run all the post install customization steps. Currently following tasks are supported:

**1. RHCOS kernel options via MachineConfig**

Use this to [add kernel arguments](https://docs.openshift.com/container-platform/4.4/nodes/nodes/nodes-nodes-working.html#nodes-nodes-kernel-arguments_nodes-nodes-working) to the cluster nodes. All the `rhcos_kernel_options` will be applied via MachineConfig to the master and worker nodes. The CRDs will be created at `workdir` and applied to each master and worker node. It will take some minutes to apply the configuration and nodes to be in Ready status again (depends on the number of master and worker nodes). Ensure none of the nodes are in SchedulingDisabled status. To get the node status run `oc get nodes`.

Requirements
------------

 - A working OCP 4.X cluster
 - All the nodes requiring customization should be in 'Ready' status

Role Variables
--------------

| Variable                | Required | Default        | Comments                                    |
|-------------------------|----------|----------------|---------------------------------------------|
| workdir                 | no       | ~/ocp4-workdir | Place for config generation and auth files  |
| rhcos_kernel_options    | no       | []             | List of kernel options for RHCOS nodes eg: ["slub_max_order=0","loglevel=7"] |

Dependencies
------------

 - ocp-install

Example Playbook
----------------

    - name: OCP post-install customizations
      hosts: bastion
      roles:
      - ocp-customization

License
-------

See LICENCE.txt

Author Information
------------------

Yussuf Shaikh (yussuf@us.ibm.com)
