# Written by Miguel Bigueur
# Linux Incident Response Script
# Security Scripting w/Python
# Dec 25, 2017


#! /bin/bash

echo "Running IR Detect Script v1.0"
echo "*****************************"
echo "Begin Sequence Now***********"

# Create IRDETECT Directory
mkdir /root/IRDETECT

# Disk Filesystem Usage
df >> /root/IRDETECT/DiskFile.txt

# Display environment variables
env >> /root/IRDETECT/ENV.txt

# Display active connections and paths
netstat >> /root/IRDETECT/Netstat.txt

# Display current running processes
ps >> /root/IRDETECT/PS.txt

# Vurtual memory statistics
vmstat >> /root/IRDETECT/VMstat.txt

# Network interface Information
ifconfig -a >> /root/IRDETECT/ifconfig.txt

# List of last logged in users
last >> /root/IRDETECT/last.txt

# Most recent login of all users
lastlog >> /root/IRDETECT/lastlog.txt

# Who is looged on and what are they doing
w >> /root/IRDETECT/w.txt

# Check for hardware events
dmesg | grep hd >> /root/IRDETECT/dmesgHD.txt

# Command History
history >> /root/IRDETECT/history.txt

# Dispaly port status
nmap -v 10.0.125.128 >> /root/IRDETECT/nmap.txt

# Show list of open handles
lsof >> /root/IRDETECT/lsof.txt

# Identify all modified or accessed files
find >> /root/IRDETECT/find.txt

# Show host information
cat /etc/hosts >> /root/IRDETECT/hosts.txt

# Display static file system info
cat /etc/fstab >> /root/IRDETECT/fstab.txt

# Show activity log
cat /var/log/messages >> /root/IRDETECT/messages.txt

# Display disk partition info
fdisk -l >> /root/IRDETECT/fdisk.txt

# List all mounted files and drives
ls -lat /mnt >> /root/IRDETECT/mountlist.txt

# List Password file contents
cat /etc/passwd >> /root/IRDETECT/passwd.txt

# Display shadow file contents
cat /etc/shadow >> /root/IRDETECT/shadow.txt

echo "***************IR Detect Script completed successfully"
echo "All files saved to /root/IRDETECT"
echo "Goodbye!"

