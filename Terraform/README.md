Great! Let's walk through the **step-by-step process** to install and configure your Proxmox infrastructure using **Terraform**, starting from scratch.

---

## ✅ Prerequisites

### 1. **System Requirements**

* One machine running **Proxmox VE** (you have this at IP `10.36.18.102`)
* One **client machine** (e.g., your Ubuntu VM) with:

  * Terraform installed
  * SSH access to the Proxmox server (optional for extra control)

---

## 🔧 Step-by-Step Installation and Configuration

---

### **Step 1: Install Terraform (on your VM)**

On your Ubuntu VM (not Proxmox):

```bash
sudo apt update
sudo apt install -y wget unzip gnupg software-properties-common
wget https://releases.hashicorp.com/terraform/1.8.3/terraform_1.8.3_linux_amd64.zip
unzip terraform_1.8.3_linux_amd64.zip
sudo mv terraform /usr/local/bin/
terraform -version  # Confirm it works
```

---

### **Step 2: Install the Proxmox Terraform Provider Plugin**

This is automatically handled when you run `terraform init` — no manual download needed.

---

### **Step 3: Create Your Terraform Project**

1. Make a folder:

```bash
mkdir terraform-proxmox && cd terraform-proxmox
```

2. Paste your `main.tf` file content into a new file:

```bash
nano main.tf
# Paste your configuration here
```

---

### **Step 4: Initialize Terraform**

This downloads the required provider (Proxmox):

```bash
terraform init
```

---

### **Step 5: Plan and Apply Infrastructure**

#### 🧹 If you’ve run Terraform before and want a clean state:

```bash
terraform state rm proxmox_lxc.ubuntu_container
```

#### ✅ Run Plan (dry-run check):

```bash
terraform plan
```

#### 🚀 Apply Configuration:

```bash
terraform apply
# Type "yes" when prompted
```

✅ If successful, Proxmox will create an LXC container using the provided Ubuntu template.

---

### **Step 6: Check Container in Proxmox**

* Go to: `http://10.36.18.102:8006/`
* Login as `root@pam`
* You should see a container named `ubuntu-lxc` under the node `police`.

---

### **Step 7: Connect to LXC**

#### Option A: From Proxmox Host (via SSH or console)

```bash
ssh root@10.36.18.102
pct list         # Find container ID (e.g., 102)
pct exec 102 -- bash
```

#### Option B: SSH Directly (if SSH server is installed in container)

```bash
ssh root@192.168.100.11
# default password: ubuntu123
```

> ⚠️ If `openssh-server` is not installed in the LXC template, you'll need to install it first using `pct exec`.

---

### **Step 8: (Optional) Post-Install Setup Inside LXC**

```bash
# Inside container
apt update && apt install -y sudo curl git openssh-server
```

---

## 🧠 Summary of What You Built

* A Proxmox LXC container named `ubuntu-lxc`
* 3 vCPUs, 4048MB RAM, 50GB storage
* Static IP: `192.168.100.11`
* Ready for hosting web apps, APIs, CI/CD, or other headless services

---

## 🛠️ Next Steps

* Create a shell script to automate `terraform init`, `plan`, and `apply`
* Install and configure apps inside the LXC (e.g., web server, Node.js)
* Secure the container (firewall rules, SSH keys, users)

---

Let me know if you'd like help with:

* Installing software in the container
* Creating a reusable Terraform module
* Automating backups or snapshots in Proxmox
