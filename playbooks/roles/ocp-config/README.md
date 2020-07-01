ocp-config: OCP Configuration
=========

This module will create the ignition files for the cluster nodes. All the ignition files will be hosted at `/var/www/html/ignition/`.

Requirements
------------

 - All the required configurations are done on the bastion node eg: HTTP, openshift-install binary is available on $PATH. This can also be achieved by using [ocp4-helpernode](https://github.com/RedHatOfficial/ocp4-helpernode) playbook.
 - Master count can be extracted from host group 'masters'.
 - Updated pull secret file with registry credentials located at `~/.openshift/pull-secret-updated` (Required for restricted network install)
 - Registry certificate file located at `/opt/registry/certs/domain.crt` (Required for restricted network install)
 - Local registry with local repo named as `ocp4/openshif4` (Required for restricted network install)

Role Variables
--------------

| Variable                | Required | Default        | Comments                                    |
|-------------------------|----------|----------------|---------------------------------------------|
| workdir                 | no       | ~/ocp4-workdir | Place for config generation and auth files  |
| log_level               | no       | info           | Option --log-level in openshift-install cmd |
| release_image_override  | no       | ""             | OCP image overide variable                  |
| enable_local_registry   | no       | false          | Set to true to enable usage of local registry for restricted network install |
| master_count            | yes      |                | Number of master nodes                      |

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
