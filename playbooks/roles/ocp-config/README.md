ocp-config: OCP Configuration
=========

This module will create the ignition files for the cluster nodes. All the ignition files will be hosted at `/var/www/html/ignition/`.

Requirements
------------

 - All the required configurations are done on the bastion node using [helpernode playbook](https://github.com/RedHatOfficial/ocp4-helpernode).
 - Master count can be extracted from host group 'masters'.
 - Updated pull secret file with registry credentials located at `~/.openshift/pull-secret-updated` (Required for restricted network install)
 - Registry certificate file located at `/opt/registry/certs/domain.crt` (Required for restricted network install)
 - Local registry with local repo named as `ocp4/openshift4` (Required for restricted network install)
 
Luks Encryption Setup using Tang Server
---------------------------------------

**_Note: This is Day-1 Activity for encryption._**
This feature will enable Luks Encryption using Tang Server on all master/worker nodes. 
Added seperate MachineConfiguration file for master and worker which will perform LUKS encryption.

Role Variables
--------------

| Variable                    | Required | Default                               | Comments                                    |
|-----------------------------|----------|---------------------------------------|---------------------------------------------|
| workdir                     | no       | ~/ocp4-workdir                        | Place for config generation and auth files  |
| log_level                   | no       | info                                  | Option --log-level in openshift-install cmd |
| release_image_override      | no       | ""                                    | OCP image overide variable                  |
| master_count                | yes      |                                       | Number of master nodes                      |
| worker_count                | yes      |                                       | Number of worker nodes                      |
| setup_squid_proxy           | no       | false                                 | Flag for setting up squid proxy server on bastion node |
| proxy_url                   | no       | ""                                    | Proxy url eg: http://[user:passwd@]server:port (NA when setup_squid_proxy: true)|
| no_proxy                    | no       | ""                                    | Comma seperated string of domains/cidr to exclude proxy |
| enable_local_registry       | no       | false                                 | Set to true to enable usage of local registry for restricted network install |
| fips_compliant              | no       | false                                 | Set to true to enable usage of FIPS for OCP deployment |
| chronyconfig.enabled        | no       | true                                  | Set to true to enable chrony configuration on the bastion node during installation. This also configure the bastion as a NTP server for the cluster. |
| chronyconfig.content        | no       | ""                                    | List of time NTP servers and options pair (see chronyconfig examples). If empty, bastion will try sync with some default ntp server (internet) AND local HW clock (with higher stratum). |
| chronyconfig.allow          | no       | ""                                    | List of network cidr (X.X.X.X/Y) allowed to sync with bastion configured as NTP server |
| dhcp_shared_network         | no       |                                       | Flag to update DHCP server work on a shared network. (Neither ACK nor NACK unknown clients) |
| cni_network_provider        | no       | OVNKubernetes                         | Sets the default Container Network Interface (CNI) network provider for the cluster |
| cni_network_mtu             | no       |                                       | MTU value to assign to the CNI network. Recommended values for OpenshiftSDN: <NIC MTU> - 50; OVNKubernetes: <NIC MTU> - 100 |
| cluster_network_cidr        | no       | 10.128.0.0/14                         | Network (in CIDR) used for the pod networks.
| cluster_network_hostprefix  | no       | 23                                    | The subnet prefix length to assign to each individual node. (netmask in CIDR format)
| service_network             | no       | 172.30.0.0/16                         | Network (in CIDR) used for the service network.
| rhcos_pre_kernel_options    | no       | []                                    | List of day-1 kernel options for RHCOS nodes eg: ["rd.multipath=default","root=/dev/disk/by-label/dm-mpath-root"] |
| luks.enabled                | no       | false                                 | Set it true if you prefer to enable LUKS in OCP deployment |
| luks.config                 | yes      |                                       | List of tang servers and thumbprint to apply |
| luks.config[].thumbprint    | yes      |                                       | Thumbprint of tang server to be added in luks_config |
| luks.config[].url           | yes      |                                       | URL of tang server to be added in luks_config |
| luks.filesystem_device      | no       | /dev/mapper/root                      | Set the Path of device to be luks encrypted |
| luks.format                 | no       | xfs                                   | Set the Format of the FileSystem to be luks encrypted |
| luks.wipeFileSystem         | no       | true                                  | Configures the FileSystem to be wiped |
| luks.device                 | no       | /dev/disk/by-partlabel/root           | Set the Path of luks encrypted partition |
| luks.label                  | no       | luks-root                             | Set the value for user label of luks encrpted partition |
| luks.options                | no       | ["--cipher", "aes-cbc-essiv:sha256"]  | Set List of luks options for the luks encryption |
| luks.wipeVolume             | no       | true                                  | Configures the luks encrypted partition to be wiped |
| luks.name                   | no       | root                                  | Set the value for the user label of Filesystem to be luks encrypted |

*chronyconfig variable example *

```yaml
chronyconfig:
   enabled: true
   content:
     - server: ntp1.example.com
       options: iburst
     - server: ntp2.example.com
       options: iburst
    allow:
      - 10.1.1.1/24
      - 10.1.2.3/16
```

*Ansible variable for Luks Encryption example*
```
luks:
 enabled: true
 config:
    - thumbprint: *********
      url: http://*.*.*.*:*
 filesystem_device: /dev/mapper/root
 format: xfs
 wipeFileSystem: true
 device: /dev/disk/by-partlabel/root
 label: luks-root
 options:
    - --cipher
    - aes-cbc-essiv:sha256
 wipeVolume: true
 name: root
```

Dependencies
------------

None

Example Playbook
----------------

    - name: Create OCP config
      hosts: bastion
      roles:
      - ocp-config
      vars:
        master_count: "{{ groups['masters'] | length }}"
        worker_count: "{{ groups['workers'] | default([]) | length }}"

License
-------

See LICENCE.txt

Author Information
------------------

Yussuf Shaikh (yussuf@us.ibm.com)
Prajyot Parab (prajyot.parab@ibm.com)
