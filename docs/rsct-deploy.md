Deploy RSCT/RMC on an OCP Cluster on PowerVM
=========

These instructions will help you deploy the RSCT/RMC daemonset on an OCP cluster running on PowerVM:

**1. Setting up the inventory**

Use the instructions provided [here](https://github.com/ocp-power-automation/ocp4-playbooks#setting-up-inventory) to setup the inventory for your cluster. For deploying RSCT, you would only need to set the bastion host details in the inventory.


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

**4. Post deployment checks**

After the playbook execution completes, the daemonset and pods should be available in the `powervm-rmc` namespace on the cluster. Run the following command to list them:

```
oc get daemonset,pods -n powervm-rmc
```
