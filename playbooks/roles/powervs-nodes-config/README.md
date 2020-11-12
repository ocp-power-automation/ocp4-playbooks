powervs-nodes-config: PowerVS OCP Cluster Nodes Configuration
=========

This module will enable connectivity between OCP nodes in PowerVS and IBM Cloud infrastructure over DirectLink.

Requirements
------------

 - A working OCP 4.X cluster
 - OCP cluster private network advertised over IBM Cloud DirectLink.
 - Running proxy service on classic infrastructure.

Role Variables
--------------

| Variable                       | Required | Default | Comments                                                      |
|--------------------------------|----------|---------|---------------------------------------------------------------|
| ibm_cloud_dl_endpoint_net_cidr | yes      |         | IBM Cloud DirectLink endpoint network cidr eg. 10.0.0.0/8     |
| ibm_cloud_http_proxy           | yes      |         | IBM Cloud http/squid proxy url eg. `http://10.166.13.64:3128` |
| ocp_node_net_gw                | yes      |         | OCP node private network gateway eg. 192.168.25.1             |
| ocp_node_net_intf              | yes      |         | OCP node private network interface name eg. env3              |

Dependencies
------------

 - None

Example Playbook
----------------

    - name: PowerVS specific nodes configuration
      hosts: bastion
      roles:
      - powervs-nodes-config

License
-------

See LICENCE.txt

Author Information
------------------

Prajyot Parab (prajot.parab@ibm.com)

