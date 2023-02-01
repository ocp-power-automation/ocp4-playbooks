ocp-upgrade: Upgrade OCP cluster
=========

This module will upgrade an existing OCP cluster based on upgrade_version or upgrade_image. If both upgrade_version and upgrade_image are specified then upgrade_image value gets preference.  

For intermediate EUS upgrade please use eus variables and use other variables for final upgrade. 

Restricted network OCP cluster can be upgraded by providing parameters restricted_network_upgrade, upgrade_version, architecture, local_secret, local_registry and local repository.

Requirements
------------

 - Running OCP 4.x cluster is needed.

Role Variables
--------------

| Variable                   | Required | Default           | Comments                                              |
|----------------------------|----------|-------------------|-------------------------------------------------------|
| eus_upgrade_version        | no       | ""                | Set to a specific version eg. 4.11.3                  |
| eus_upgrade_channel        | no       | ""                | Set to channel having required upgrade version available for cluster upgrade (stable-4.x, fast-4.x, candidate-4.x, eus-4.x) eg. stable-4.11     |
| eus_upgrade_image          | no       | ""                | Set to OCP upgrade image eg. quay.io/openshift-release-dev/ocp-release@sha256:12345..   |
| eus_upstream               | no       | ""                | Set the URL for OCP update server eg. https://ppc64le.ocp.releases.ci.openshift.org/graph   |
| upgrade_version            | no       | ""                | Set to a specific version eg. 4.5.4                   |
| upgrade_channel            | no       | ""                | Set to channel having required upgrade version available for cluster upgrade (stable-4.x, fast-4.x, candidate-4.x) eg. stable-4.5 |
| upgrade_image              | no       | ""                | Set to OCP upgrade image eg. quay.io/openshift-release-dev/ocp-release@sha256:12345.. |
| pause_time                 | no       | 90                | Pauses playbook execution for a set amount of time in minutes |
| delay_time                 | no       | 600               | Number of seconds to wait before starting to poll     |
| restricted_network_upgrade | no       | false             | Set to true to upgrade the restricted network cluster |
| architecture               | no       | "ppc64le"         | Architecture of the cluster.                          |
| local_secret               | no       | ""                | Path to pull secret of the registry                   |
| local_registry             | no       | ""                | Specify the local registry name along with port for your mirror repository eg. registry.test-ocp-600b.ibm.com:5000 |
| local_repository           | no       | "ocp4/openshift4" | Name of the repository to create in your registry eg. ocp4/openshift4 |

Note: If eus_upgrade_channel is set to the eus channel then no need to set upgrade_channel.

Dependencies
------------

 - None

Example Playbook
----------------

    - name: Upgarde OCP cluster
      hosts: bastion
      tasks:
        - include_role:
            name: ocp-upgrade
          when: >
            (upgrade_version != "") or (upgrade_image != "") or 
            (eus_upgrade_channel != "") or (eus_upgrade_image != "")

License
-------

See LICENCE.txt

Author Information
------------------

Prajyot Parab (prajyot.parab@ibm.com)

