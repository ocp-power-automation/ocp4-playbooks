ocp-customization: OCP post-install customizations
=========

This module will run all the post install customization steps. Currently following tasks are supported:

**1. RHCOS kernel options via MachineConfig**

Use this to [add kernel arguments](https://docs.openshift.com/container-platform/4.4/nodes/nodes/nodes-nodes-working.html#nodes-nodes-kernel-arguments_nodes-nodes-working) to the cluster nodes. All the `rhcos_kernel_options` will be applied via MachineConfig to the master and worker nodes. The CRDs will be created at `workdir` and applied to each master and worker node. It will take some minutes to apply the configuration and nodes to be in Ready status again (depends on the number of master and worker nodes). Ensure none of the nodes are in SchedulingDisabled status. To get the node status run `oc get nodes`.

**2. Sysctl settings via tuned operator**

Use this to modify kernel tunables for nodes/pods via [tuned operator](https://docs.openshift.com/container-platform/4.3/scalability_and_performance/using-node-tuning-operator.html).

**3. RSCT/RMC**

Use this to deploy containerized version of [RSCT](https://www.ibm.com/support/knowledgecenter/SGVKBA) on every OCP node running on PowerVM infrastructure.  
This is enabled by default when deploying OCP in PowerVM or PowerVS. Follow the instructions provided [here](/docs/rsct-deploy.md) to deploy RSCT on an existing OCP cluster. 

**4. Automate setting of Node Labels**

Use this to automate setting of Node Labels on PowerVS. This refers to the [Well-known Labels document](https://kubernetes.io/docs/reference/labels-annotations-taints).

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
| sysctl_tuned_options    | no       | false       | Set to true to apply sysctl options via tuned operator |
| powervm_rmc             | no       | true           | Set to true to deploy RMC daemonset on Node with arch ppc64le |
| rsct_image              | no       | quay.io/powercloud/rsct-ppc64le:latest | Change to your own registry if you install without internet connection |
| node_labels             | no       | {}              | Map of node labels and its values          |

If `sysctl_tuned_options` is true then the following variables are must and should be set in [vars/tuned.yaml](./vars/tuned.yaml)

| Variable       | Required | Default        | Comments                                    |
|----------------|----------|----------------|---------------------------------------------|
| sysctl_options | yes      | []             | List of sysctl options to apply. Look at [vars/tuned.yaml](./vars/tuned.yaml) for example |
| match_array    | yes      | []             | Criteria for node/pod selection. Look at [vars/tuned.yaml](./vars/tuned.yaml) for example |

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

- Yussuf Shaikh (yussuf@us.ibm.com)
- Pradipta Kr. Banerjee (bpradipt@in.ibm.com)
