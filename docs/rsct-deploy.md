Deploy RSCT/RMC on an OCP Cluster on PowerVM
=========

These instructions will help you deploy the RSCT/RMC daemonset on an OCP cluster running on PowerVM:

**1. Setting up the inventory**

Use the instructions provided [here](https://github.com/ocp-power-automation/ocp4-playbooks#setting-up-inventory) to setup the inventory for your cluster. For deploying RSCT, you would only need to set the bastion host details in the inventory.

Provide the hostname or the IP address of the bastion node and the user name in the inventory file. An example of the inventory file would look like this:

```
$ cat inventory
[bastion]
192.168.26.155 ansible_connection=ssh ansible_user=root
```

**2. Set up the variables**

Make use of the sample file at examples/rmc_vars.yaml.

```
cp examples/rmc_vars.yaml .
```

**3. Run the playbook to deploy RSCT**

The ocp-customization [module](https://github.com/ocp-power-automation/ocp4-playbooks/tree/master/playbooks/roles/ocp-customization) is used to deploy RSCT/RMC daemonset on the cluster.

```
ansible-playbook -i inventory -e @rmc_vars.yaml playbooks/customization.yaml
```

Use the following command in case a non-root user is specified in the inventory file. Upon running the playbook, enter the password of the user when prompted for the "BECOME password".

```
ansible-playbook -i inventory -e @rmc_vars.yaml playbooks/customization.yaml -K --become
```

Note: While running the playbook as a non-root user, you may see an error such as: "oc: command not found". Since the command to run the playbook uses the `become` privilege escalataion option, such errors may arise when the PATH environment variable for `sudo` may not be the same as your user. You can rectify this by modifying the `Defaults secure_path` section in the sudoers file.

Example: If the `oc` client binary is present in the /usr/local/bin directory, run the `visudo` command and navigate to the `Defaults secure_path` section. Set the PATH by adding `/usr/local/bin` as given below, save the file and re-run the ansible playbook:

```
Defaults secure_path = /sbin:/bin:/usr/sbin:/usr/bin:/usr/local/bin
```

**4. Post deployment checks**

After the playbook execution completes, the daemonset and pods should be available in the `powervm-rmc` namespace on the cluster. Run the following command to list them:

```
oc get daemonset,pods -n powervm-rmc
```

**NOTE:**
On systems with large memory configuration, powervc-rmc pod may crash with OOMKilled error message. This happens when the memory limit is not sufficient on the pod. This can be resolved by modifying the daemonset for powervm-rmc to increase the memory limit to a bigger value.
