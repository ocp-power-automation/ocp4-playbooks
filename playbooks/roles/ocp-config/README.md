ocp-config: OCP Configuration
=========

This module will create the ignition files for the cluster nodes. All the ignition files will be hosted at `/var/www/html/ignition/`.

Requirements
------------

 - All the required configurations are done on the bastion node eg: HTTP, openshift-install binary is available on $PATH. This can also be achieved by using [ocp4-helpernode](https://github.com/RedHatOfficial/ocp4-helpernode) playbook.
 - Master count can be extracted from host group 'masters'.
 - Updated pull secret file with registry credentials located at `~/.openshift/pull-secret-updated` (Required for restricted network install)
 - Registry certificate file located at `/opt/registry/certs/domain.crt` (Required for restricted network install)
 - Local registry with local repo named as `ocp4/openshift4` (Required for restricted network install)

Role Variables
--------------

| Variable                | Required | Default        | Comments                                    |
|-------------------------|----------|----------------|---------------------------------------------|
| workdir                 | no       | ~/ocp4-workdir | Place for config generation and auth files  |
| log_level               | no       | info           | Option --log-level in openshift-install cmd |
| release_image_override  | no       | ""             | OCP image overide variable                  |
| master_count            | yes      |                | Number of master nodes                      |
| setup_squid_proxy       | no       | false          | Flag for setting up squid proxy server on bastion node |
| proxy_url               | no       | ""             | Proxy url eg: http://[user:passwd@]server:port (NA when setup_squid_proxy: true)|
| no_proxy                | no       | ""             | Comma seperated string of domains/cidr to exclude proxy |
| enable_local_registry   | no       | false          | Set to true to enable usage of local registry for restricted network install |
| chronyconfig.enabled    | no       | true           | Set to true to enable chrony configuration on the bastion node during installation. This also configure the bastion as a NTP server for the cluster. |
| chronyconfig.content    | no       | ""             | List of time NTP servers and options pair (see chronyconfig examples). If empty, bastion will try sync with some default ntp server (internet) AND local HW clock (with higher stratum). |
| chronyconfig.allow      | no       | ""             | List of network cidr (X.X.X.X/Y) allowed to sync with bastion configured as NTP server |

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

License
-------

See LICENCE.txt

Author Information
------------------

Yussuf Shaikh (yussuf@us.ibm.com)
Prajyot Parab (prajyot.parab@ibm.com)
