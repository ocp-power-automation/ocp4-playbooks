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

Role Variables
--------------

| Variable                    | Required | Default        | Comments                                    |
|-----------------------------|----------|----------------|---------------------------------------------|
| workdir                     | no       | ~/ocp4-workdir | Place for config generation and auth files  |
| log_level                   | no       | info           | Option --log-level in openshift-install cmd |
| release_image_override      | no       | ""             | OCP image overide variable                  |
| master_count                | yes      |                | Number of master nodes                      |
| worker_count                | yes      |                | Number of worker nodes                      |
| setup_squid_proxy           | no       | false          | Flag for setting up squid proxy server on bastion node |
| proxy_url                   | no       | ""             | Proxy url eg: http://[user:passwd@]server:port (NA when setup_squid_proxy: true)|
| no_proxy                    | no       | ""             | Comma seperated string of domains/cidr to exclude proxy |
| enable_local_registry       | no       | false          | Set to true to enable usage of local registry for restricted network install |
| fips                        | no       | false          | Set to true to enable usage of fips for ocp deployment |
| chronyconfig.enabled        | no       | true           | Set to true to enable chrony configuration on the bastion node during installation. This also configure the bastion as a NTP server for the cluster. |
| chronyconfig.content        | no       | ""             | List of time NTP servers and options pair (see chronyconfig examples). If empty, bastion will try sync with some default ntp server (internet) AND local HW clock (with higher stratum). |
| chronyconfig.allow          | no       | ""             | List of network cidr (X.X.X.X/Y) allowed to sync with bastion configured as NTP server |
| dhcp_shared_network         | no       |                | Flag to update DHCP server work on a shared network. (Neither ACK nor NACK unknown clients) |
| cni_network_provider        | no       | OpenshiftSDN   | Sets the default Container Network Interface (CNI) network provider for the cluster |
| cni_network_mtu             | no       |                | MTU value to assign to the CNI network. Recommended values for OpenshiftSDN: <NIC MTU> - 50; OVNKubernetes: <NIC MTU> - 100 |
| cluster_network_cidr        | no       | 10.128.0.0/14  | Network (in CIDR) used for the pod networks.
| cluster_network_hostprefix  | no       | 23             | The subnet prefix length to assign to each individual node. (netmask in CIDR format)
| service_network             | no       | 172.30.0.0/16  | Network (in CIDR) used for the service network.
| rhcos_pre_kernel_options    | no       | []             | List of day-1 kernel options for RHCOS nodes eg: ["rd.multipath=default","root=/dev/disk/by-label/dm-mpath-root"] |

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
