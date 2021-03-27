# Python-Apache-Cassandra-Connection-and-CQL-Interface

This tutorial describes how to connect from Python to remote Apache Cassandra and exacute CQL commands on database. In my case Cassandra is installed on VM (VirtualBox) and my host computer is Mac. 
First of all make sure that sure that Cassandra's system service is running and listening default port 9042 (if default port has not been changed). Run one of the following commands on the machine where Cassandra is installed to check if port is active 
```
sudo netstat -anp | grep 9042
OR
sudo lsof -i | grep 9042 
```
The following output is what you can expect
```
java       1682 cassandra  134u  IPv4  20375      0t0  TCP *:9042 *(LISTEN)*
```
