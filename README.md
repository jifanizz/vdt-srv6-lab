# VDT SRv6 Lab

Welcome to the VDT SRv6 Lab repository. This README provides an overview of the project, setup instructions, and usage guidelines.


## Setup Instructions

Follow these steps to set up the VDT SRv6 Lab environment:

1. Connect to dCloud server:
    ```sh
    ssh admin@198.18.130.5
    ```
    passwd=cisco123

2. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/vdt-srv6-lab.git
    ```
3. Navigate to the project directory:
    ```sh
    cd vdt-srv6-lab
    ```
4. Start the lab:
    ```sh
    sudo clab deploy
    ```
5. Get IP addresses of routers:
    ```sh
    sudo clab inspect
    ```
6. SSH to virtual routers with username cisco and password cisco123.

