>[Back to Index](README.md)

### Table of contents
1. [Linux Essentials](#linux-essentials)
2. [Finding Your Way](#finding-your-way)
3. [Command Line](#command-line)
4. [Operating Systems](#operating-systems)
5. [Security](#security)



## Linux Essentials
### Linux Distributions
***Linux*** is a open source and freely distributed operating system. Popular Linux distros are Ubuntu, Red Hat Enterprise Linux, Fedora, Debian

**Linux distribution** comprises of: 
- **Kernel** 

  It is the framework that connects the application layer to the hardware of a computer. The kernel is the foundation of the operating system which sits directly on     the hardware and permits applications to interact with the hardware and use the hardware as a compute resource.
  
- **GNU core**

  The GNU core utilities are basic file shell and text manipulation utilities of the GNU operating system. They are foundational utilities which are expected to exist   on every operating system. Examples include setting and changing file permissions and ownerships, concatenating, and writing files, giving exit statuses, listing       directories and files, being able to move between directories and files. One of the utilities provided is  
  ```bash
  ls
  ```
  which lists directories.
  
- **X server (optional)**

  This is a framework for the GUI environment or Graphical User Interface. X is an architecture agnostic framework for remote graphical user interfaces and input         devices. 
  
- **Graphical interface (optional)**

  The graphical interface is often referred to as the desktop environment, common Linux desktops include Gnome, KDE, Unity which is what Ubuntu runs here. This is the   environment that permits you to navigate the operating system,
  using a mouse and folders.

All of these run on the hardware (laptop/desktop).


### Embedded Linux

An embedded system is a combination of hardware and software for a purpose. Android, Raspberry Pi, Smart TVs, Networking equipment (routers and switches) are examples of embedded systems.


| Embedded Linux  | 
| ------------- | 
| Application  | 
| Libraries (Applications uses libraries to function) | 
| High-level abstractions | 
| Networking (for communication) & File Systems | 
| Low-level interfaces | 
| Hardware | 


### Linux in the Cloud

The cloud is a collection of data centers providing compute, application and storage services over the Internet. 

![Linux in the Cloud](https://user-images.githubusercontent.com/97931452/161281159-d2859789-3fc1-4b2a-95d2-6990f5395baa.jpg)

- Region: Each Azure region features datacenters deployed within a latency-defined perimeter. They're connected through a dedicated regional low-latency network. This   design ensures that Azure services within any region offer the best possible performance and security.

- [Availability Zone](https://docs.microsoft.com/en-us/azure/availability-zones/az-overview): A subset of compute resources within a region.

- Subnet: a local network instance for the compute resources in the cloud. There may be multiple computer instances or virtual servers existing within a subnet and      these are replicated into additional availability zones in additional regions. In case one of them becomes corrupt or if there is a problem at one of the data          centers, the resources are spread around to create a very fault tolerant or redundant service. This is often accompanied by automation mechanisms to create and        manage a self-healing infrastructure.


## Major Open Source Applications

### Desktop Applications

Common open source desktop applications are OpenOffice (office application) and Firefox (web browser). OpenOffice is developed and maintained by the Apache software foundation and is free to use for any purpose. OpenOffice is developed and maintained by the Apache software foundation and is
free to use for any purpose. An alternative to OpenOffice is LibreOffice. LibreOffice was developed by the developers by using the open-source code from OpenOffice to create a parallel project. This is a process called forking.

### Server Applications

Server is something that provide client services. The types of open source server applications are: 

- Web server (Apache, NGINX)
- Database server (mySQL, MariaDB)
- File sharing server (Samba, NFS)
- Private cloud (ownCloud, Nextcloud)

![NGINX](https://user-images.githubusercontent.com/97931452/161305940-16a61ee1-3721-4d24-80c2-6c87ac1e1c82.jpg)


**NGINX** is a web server that can also be used for reverse proxy, load balancing, mail proxy, and HTTP caching. Load balancing means that it can balance incoming requests (managing traffic). It can balance those requests between backend web hosts (NGINX host and Apache host). All of the requests come in through the load balancer and then are distributed out to the backend hosts.


### Development Languages

The common open source languages for application development are: 

- **Shell**: Runned by command line interpreter. Shell scripts are often used to automate strings of commands
- **C**: Imperative programming language. A basic low-level programming language. As an example, you write the code for a web browser. You use C to write it. You then compile it and you're left with an executable something like Firefox.
- **Java**: Object oriented general purpose programming language. 
- **Javascript**: HTML, CSS and JavaScript make up the core technologies of the world wide web. Most web browsers have a dedicated JavaScript engine for JavaScript execution as it is a technology that enables interactive web pages.
- **Perl**: supports both procedural and object-oriented programming and is highly extensible with over 20,000 third party modules available.
- **Python**: an interpreted general purpose programming language. Python source code is generally regarded as easier to read due to the structuring requirements.
- **PHP**: PHP or the PHP Hypertext Processor is a programming language originally designed for web development.

### Package Management Tools and Repositories
