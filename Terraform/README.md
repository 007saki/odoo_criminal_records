<!-- If you already have state running -->
terraform state rm proxmox_lxc.ubuntu_container

<!-- Once plan and apply you have a state running -->
terraform plan

terraform apply

Terraform Config
----------------------------------------------------------------
<!-- How to work with terraform -->
Your container is ideal for headless operations, such as:

Hosting web servers (Nginx, Apache)

Running API services (Node.js, Python)

Hosting microservices or app backends

CI/CD agents, automation runners, small databases

You typically SSH into it, or run commands using pct exec, not necessarily via console UI.

---------------------------------------------------------------
<!-- Use pct exec to interact -->
You're running Terraform from a VM (Ubuntu) inside Proxmox. The pct command controls LXC containers at the Proxmox host level (e.g., root@proxmox or root@police).

That means:

You cannot use pct from inside your VM.

You must SSH into the Proxmox host to use pct.

pct exec 102 -- bash

This will open a shell inside the LXC container with ID 102.

----------------------------------------------------------------

Now install and configure your infrastructure
