# Centos - install another linux on your docker container

Make sure you have docker installed on your machine! if you have not, you should google on how to install it before reading the next few requirements:

1. Can you try to pull `centos` image from docker hub?

    `docker pull centos`

2. Then can you run centos via the terminal?

    `docker run -i -t centos`
    

3. Check that it is centos. `cat /etc/os-release`
    ```
    NAME="CentOS Linux"
    VERSION="8"
    ID="centos"
    ID_LIKE="rhel fedora"
    VERSION_ID="8"
    PLATFORM_ID="platform:el8"
    PRETTY_NAME="CentOS Linux 8"
    ANSI_COLOR="0;31"
    ```
4. Check that it has nano, ssh and vim.

    `nano`, `ssh` and `vim` commands are not available. 

    ```
    [root@f6342e5f7e64 /]# nano
    bash: nano: command not found
    [root@f6342e5f7e64 /]# ssh
    bash: ssh: command not found
    [root@f6342e5f7e64 /]# vim
    bash: vim: command not found
    ```
    ### Install nano and vim
    
    Encountered an error while installing. 

    ```
    [root@f6342e5f7e64 /]# yum install nano
    Failed to set locale, defaulting to C.UTF-8
    CentOS Linux 8 - AppStream                                                               64  B/s |  38  B     00:00
    Error: Failed to download metadata for repo 'appstream': Cannot prepare internal mirrorlist: No URLs in mirrorlist
    ```
    Solved the problem using method from [here](https://techglimpse.com/failed-metadata-repo-appstream-centos-8/).

    ```
    cd /etc/yum.repos.d/
    sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
    sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
    yum update -y
    ```
    ```
    yum install vim
    yum install nano
    ```
    ```
    [root@74cca7c24781 yum.repos.d]# vim
    [root@74cca7c24781 yum.repos.d]# nano
    ```

    ### Install ssh
    [Source](https://phoenixnap.com/kb/how-to-ssh-into-docker-container)

    Run the following command: `yum install openssh-server openssh-clients`
    
    ```
    [root@74cca7c24781 /]# ssh
    usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]
           [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
           [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]
           [-i identity_file] [-J [user@]host[:port]] [-L address]
           [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
           [-Q query_option] [-R address] [-S ctl_path] [-W host:port]
           [-w local_tun[:remote_tun]] destination [command]
    ```


    Run `docker ps -a` to check the container id. Start the container `docker start -i 74cca7c24781` and check if the commands work. 

    ### Commit to new image 

    We can save the changes to a new image `centos-vnst` by running the following: `docker commit "CONTAINER_ID" "new image name"`

    ```
    $ docker commit 74cca7c24781 centos-vnst
    sha256:7e2e9bf8db1ef23c62730de90eb8ce3c21076a489e1cd08ffcc745aa8a77b008

    $ docker images
    REPOSITORY               TAG        IMAGE ID       CREATED          SIZE
    centos-vnst              latest     7e2e9bf8db1e   10 seconds ago   566MB
    centos                   latest     5d0da3dc9764   7 months ago     231MB

    $ docker run -it centos-vnst
    ```
    ### Alternative method by creating a Dockerfile
    
    **Create the following Dockerfile**

    ```
    FROM centos:latest

    RUN sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*

    RUN sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

    RUN yum update -y

    RUN yum -y install vim

    RUN yum -y install nano

    RUN yum -y install openssh-server openssh-clients 

    ```
    **Build the image**

    Run the command from the directory where the Dockerfile is located: `docker build -t ailinkhoo/centos .` The option `-t` specifies the image name and optionally a username and tag in the `username/imagename:tag` format. The `.` at the end of the docker build command tells that Docker should look for the Dockerfile in the current directory.

    The new image will be listed:  
    ```
    $ docker images
    REPOSITORY               TAG        IMAGE ID       CREATED          SIZE
    ailinkhoo/centos         latest     e3c5d1774178   8 minutes ago    663MB
    centos-vnst              latest     7e2e9bf8db1e   45 minutes ago   566MB
    ```
    
    Start the container from the new image: `docker run -i -t ailinkhoo/centos` and check if all the commands work. 


5. Can you install `top` in centOS?

    ```
    [root@74cca7c24781 /]# top
    top - 09:25:17 up  9:33,  0 users,  load average: 0.00, 0.00, 0.00
    Tasks:   2 total,   1 running,   1 sleeping,   0 stopped,   0 zombie
    %Cpu(s):  0.0 us,  0.1 sy,  0.0 ni, 99.9 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
    MiB Mem :  12681.9 total,   9942.2 free,    585.3 used,   2154.5 buff/cache
    MiB Swap:   4096.0 total,   4096.0 free,      0.0 used.  11438.4 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
        1 root      20   0   14976   3628   3080 S   0.0   0.0   0:00.10 bash
    21 root      20   0   52060   4348   3728 R   0.0   0.0   0:00.00 top
    [root@74cca7c24781 yum.repos.d]# exit
    ```


If you do not have them, make sure you have vim, nano and other essential packages installed. At this point in time, you need to research on how to update your centos to have all of the above mentioned.


Remember to share your answer and help each other. Write down the commands required to start all of these. Good luck.



Further reading: 

- What's a docker image https://www.tutorialspoint.com/docker/docker_images.htm
- What's a dockerfile: https://www.tutorialspoint.com/docker/docker_file.htm
- Atop https://www.cyberciti.biz/faq/centos-redhat-linux-install-atop-command-using-yum/
- Kubernetes vs docker https://www.geeksforgeeks.org/kubernetes-vs-docker/