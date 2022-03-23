# NOTICE: This branch is no longer updated with new features and only allow critical fixes if any.


# Introduction
The playbooks are used for installation of OCP on Power and other post install customizations.
The playbooks are used with [PowerVS](https://github.com/ocp-power-automation/ocp4_upi_powervs), [PowerVC](https://github.com/ocp-power-automation/ocp4_upi_powervm)
and [KVM](https://github.com/ocp-power-automation/ocp4_upi_kvm) projects.

## Assumptions

 - A bastion/helper node is already created where the playbooks would run.
 - The required services are configured on the bastion/helper node using [helpernode playbook](https://github.com/RedHatOfficial/ocp4-helpernode).
 - The cluster nodes are already created.

## Bastion HA setup

We can have multiple bastion nodes as part of the OpenShift 4.X setup. Ensure that all the required services are configured on all the bastion nodes. Also, keepalived service should be configured and running.

To use this playbook for bastion HA you need to:
1. Run helpernode playbook with [HA configurations](https://github.com/RedHatOfficial/ocp4-helpernode/blob/master/docs/examples/vars-ha-ppc64le.yaml#L48-L57).
1. Use `bastion_vip` variable with keepalived vrrp address.
1. Add `bastion` host group entries with all bastion nodes in `examples/inventory`.

The OpenShift install commands will always run on the first bastion. Additional services such as squid proxy, chrony, etc. will be configured on all nodes. The auth directory and ignition files will be available on all nodes once the installation complete.


## Set up the required variables

Make use of the sample file at `examples/install_vars.yaml`. Modify the values as per your cluster.

```
cp examples/install_vars.yaml .
```

### Use install_vars.yaml

This section sets the variables for the install-config.yaml template file.

```
install_config:
   cluster_domain: < Cluster domain name. Match to the baseDomain in install-config.yaml.>
   cluster_id: < Cluster identifier. Match to the metadata.name in install-config.yaml.>
   pull_secret: '<pull-secret json content>'
   public_ssh_key: '<SSH public key content to access the cluster nodes>'
```

Below variables will be used by the OCP install playbook.

```
workdir: <Directory to use for creating OCP configs>
storage_type: <Storage type used in the cluster. Eg: nfs (Note: Currently NFS provisioner is not configured using this playbook. This variable is only used for setting up image registry to EmptyDir if storage_type is not nfs)>
log_level: <Option --log-level in openshift-install commands. Default is 'info'>
release_image_override: '<This is set to OPENSHIFT_INSTALL_RELEASE_IMAGE_OVERRIDE while creating ign files. If you are using internal artifactory then ensure that you have added auth key to the pull_secret>'
rhcos_pre_kernel_options: <List of day-1 kernel options for RHCOS nodes eg: ["rd.multipath=default","root=/dev/disk/by-label/dm-mpath-root"]>
rhcos_kernel_options: <List of kernel options for RHCOS nodes eg: ["slub_max_order=0","loglevel=7"]>
```

## Setting up inventory

Make use of sample file at `examples/inventory`. Modify the host values as per your cluster.

```
cp examples/inventory .
```


## Run the playbook

Once you have configured the vars & inventory file, run the install playbook using:

```
ansible-playbook  -i inventory -e @install_vars.yaml playbooks/install.yaml
```


License
-------

See LICENCE.txt
