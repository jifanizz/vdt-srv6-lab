# Backup Cisco XR config
 
# import modules needed and set up ssh connection parameters
import paramiko
import datetime
import os
user = 'cisco'
secret = 'cisco123'
port = 22
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
 
# define variables
time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S')

# Create the directory
outfilepath = ("./pybackup/" + time_now + "/")
os.makedirs(outfilepath, exist_ok=True)


infilepath = "./"
devicelist = "device-list1.txt"
 
# open device file
input_file = open( infilepath + devicelist, "r")
iplist = input_file.readlines()
input_file.close()
 
# loop through device list and execute commands
for ip in iplist:
    ipaddr = ip.strip()
    ssh.connect(hostname=ipaddr, username=user, password=secret, port=port)
    stdin, stdout, stderr = ssh.exec_command('show run')
    list = stdout.readlines()
    outfile = open(outfilepath + ipaddr, "w")
    for char in list:
        outfile.write(char)
    ssh.close()
    outfile.close()
