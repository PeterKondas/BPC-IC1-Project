# BPC-IC1 Project - how to

This is a web application ContactManager running on Ubuntu server. 

### Run ubuntu server
After starting virtual machine you can enter username and password or connect via ssh:
```commandline
ssh student@192.168.0.114
password: student
```

### Start database 
It is MySQL database running in docker. To make sure that the database is running use command:
```commandline
docker ps -a
```

If there is existing container which looks like the one below, the database is running. Important are PORTS and COMMAND array.
```commandline
CONTAINER ID   IMAGE         COMMAND                  CREATED       STATUS                   PORTS                                                  NAMES
3fc5ea51c763   mysql         "docker-entrypoint.s…"   4 days ago    Up 41 minutes            0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   database
```
If there is no Container ID, the container must be started first. To do that, you can use following command (keep in mind that you have to be in folder where is this file).
```commandline
docker-compose up -d
```

### Run app
```commandline
python3 app.py
```