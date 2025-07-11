terraform {
  required_providers {
    proxmox = {
      source  = "telmate/proxmox"
      version = "3.0.2-rc01"
    }
  }
}

provider "proxmox" {
  pm_api_url      = "http://10.36.18.102:8006/api2/json"
  pm_user         = "root@pam"
  pm_password     = "Nairai@2024"
  pm_tls_insecure = true
}

resource "proxmox_lxc" "ubuntu_container" {
  target_node  = "police"
  hostname     = "ubuntu-lxc"
  ostemplate   = "local:vztmpl/ubuntu-25.04-standard_25.04-1.1_amd64.tar.zst"
  password     = "ubuntu123"
  unprivileged = false

  cores  = 3
  memory = 4048
  swap   = 512

  rootfs {
    storage = "local-lvm"
    size    = "50G"
  }

  network {
    name     = "eth0"
    bridge   = "vmbr1"
    ip       = "192.168.100.11/24"  # Choose an unused IP
    gw       = "192.168.100.1"      # Gateway is Proxmox NAT
    firewall = false
  }

  cmode   = "console"
  console = true
  tty     = 1

  start = true
}
