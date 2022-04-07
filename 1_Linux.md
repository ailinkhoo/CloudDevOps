>[Back to Index](README.md)

### Table of contents
- [Linux Essentials](#linux-essentials)
  - [Linux Distributions](#linux-distributions)
  - [Embedded Linux](#embedded-linux)
  - [Linux in the Cloud](#linux-in-the-cloud)
  - [Major Open Source Applications](#major-open-source-applications)
  - [Development Languages](#development-languages)
  - [Package Management Tools and Repositories](#package-management-tools-and-repositories)
- [Finding Your Way](#finding-your-way)
  - [CLI Basics](#cli-basics)
  - [Getting Help](#getting-help)
  - [Using Directories and Listing Files](#using-directories-and-listing-files)
  - [Working with Files and Directories](#working-with-files-and-directories)
- [Command Line](#command-line)
  - [Archiving Files on the Command Line](#archiving-files-on-the-command-line)
  - [Searching and Extracting Data from Files](#searching-and-extracting-data-from-files)
  - [Turning Commands into Scripts](#turning-commands-into-scripts)
- [Operating Systems](#operating-systems)
  - [Choosing an OS](#choosing-an-os)
  - [Computer Hardware](#computer-hardware)
  - [Data Storage](#data-storage)
  - [Network](#network)
- [Security](#security)



# Linux Essentials
## Linux Distributions
***Linux*** is a open source and freely distributed operating system. Popular Linux distros are Ubuntu, Red Hat Enterprise Linux, Fedora, Debian

**Linux distribution** comprises of: 
- **Kernel** 

  It is the framework that connects the application layer to the hardware of a computer. The kernel is the foundation of the operating system which sits directly on     the hardware and permits applications to interact with the hardware and use the hardware as a compute resource.
  
- **GNU core**

  The GNU core utilities are basic file shell and text manipulation utilities of the GNU operating system. They are foundational utilities which are expected to exist   on every operating system. Examples include setting and changing file permissions and ownerships, concatenating, and writing files, giving exit statuses, listing directories and files, being able to move between directories and files. One of the utilities provided is `ls` which lists directories.
  
- **X server (optional)**

  This is a framework for the GUI environment or Graphical User Interface. X is an architecture agnostic framework for remote graphical user interfaces and input         devices. 
  
- **Graphical interface (optional)**

  The graphical interface is often referred to as the desktop environment, common Linux desktops include Gnome, KDE, Unity which is what Ubuntu runs here. This is the   environment that permits you to navigate the operating system,
  using a mouse and folders.

All of these run on the hardware (laptop/desktop).


## Embedded Linux

An embedded system is a combination of hardware and software for a purpose. Android, Raspberry Pi, Smart TVs, Networking equipment (routers and switches) are examples of embedded systems.


| Embedded Linux  | 
| ------------- | 
| Application  | 
| Libraries (Applications uses libraries to function) | 
| High-level abstractions | 
| Networking (for communication) & File Systems | 
| Low-level interfaces | 
| Hardware | 


## Linux in the Cloud

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

<img src="https://user-images.githubusercontent.com/97931452/161305940-16a61ee1-3721-4d24-80c2-6c87ac1e1c82.jpg" width=80% height=80%>


**NGINX** is a web server that can also be used for reverse proxy, load balancing, mail proxy, and HTTP caching. Load balancing means that it can balance incoming requests (managing traffic). It can balance those requests between backend web hosts (NGINX host and Apache host). All of the requests come in through the load balancer and then are distributed out to the backend hosts.


## Development Languages

The common open source languages for application development are: 

- **Shell**: Runned by command line interpreter. The shell is basically a program that takes your commands from the keyboard and sends them to the operating system to perform. Shell scripts are often used to automate strings of commands
- **C**: Imperative programming language. A basic low-level programming language. As an example, you write the code for a web browser. You use C to write it. You then compile it and you're left with an executable something like Firefox.
- **Java**: Object oriented general purpose programming language. 
- **Javascript**: HTML, CSS and JavaScript make up the core technologies of the world wide web. Most web browsers have a dedicated JavaScript engine for JavaScript execution as it is a technology that enables interactive web pages.
- **Perl**: supports both procedural and object-oriented programming and is highly extensible with over 20,000 third party modules available.
- **Python**: an interpreted general purpose programming language. Python source code is generally regarded as easier to read due to the structuring requirements.
- **PHP**: PHP or the PHP Hypertext Processor is a programming language originally designed for web development.

## Package Management Tools and Repositories

The system is comprised of many packages such as internet browsers, text editors, media players, etc. These packages are managed via package managers, which install and maintain the software on your system. Not all packages are installed through package managers though, you can commonly install packages directly from their source code. What are packages? You may know them as Chrome, Photoshop, etc and they are, but what they really are just lots and lots of files that have been compiled into one. 

Popular package managers are 
- **Debian Package (dpkg)** 
  - **Advanced Package Tool (apt-get)** 
- **Red Hat Package Manager (rpm)**
  - **Yellow Dog Updater (yum)**
 
`apt-get` is an extension of `dpkg` which solves the dependency problems of `dpkg`. It will look through the repositories and pull in all the dependencies, thus managing all of the installations of `dpkg` applications or packages on the system. `apt-get` permits the user to easily search for and install packages from repositories or directories containing software packages in an index. **Package Repositories** are a collection of packages. Your distribution already comes with pre-approved sources to get packages from and this is how it installs all the base packages you see on your system. On a Debian system, this sources file is the /etc/apt/sources.list file. Your machine will know to look there and check for any source repositories you added.


# Finding Your Way

## CLI Basics

### Basic Shell
The standard Linux shell (BASH) is both a command line interpreter and a programming language.

<img src="https://user-images.githubusercontent.com/97931452/161514481-52c412f7-bb8f-4038-8c3e-2540ab75660d.jpg" width=80% height=80%>

<img src="https://user-images.githubusercontent.com/97931452/161514570-59205708-62b1-4f86-9753-8f82149d52ed.jpg" width=80% height=80%>

We send input through Standard In or STDIN this is a stream going in. The interpreter is going to parse that input.  It is then going to execute it and provide us back a result. The output is then sent out to 1 of 2 streams Standard Out or STDOUT or Standard Error STDERR. Both screens will print to the screen by default. However, the output may be changed with redirection or pipeline.

<img src="https://user-images.githubusercontent.com/97931452/161514613-9714a5c5-b943-4354-a7c9-3590ef008c83.jpg" width=50% height=50%>

The command prompt usually consists of the current user, current host and working directory. The dollar sign denotes that the current user is unprivileged. 

### Command Line Syntax

The full syntax for a Bash command is:

```Bash

command [options] [arguments]

```

Bash treats the first string it encounters as a command. The following command uses Bash's `ls` (for "list") command to display the contents of the current working directory:

```Bash

ls

```
Bash commands are often accompanied by arguments. For example, you can include a path name in an `ls` command to list the contents of another directory:

```Bash

ls /etc

```

Most Bash commands have options for modifying how they work. Options, also called flags, give a command more specific instructions. As an example, files and directories whose names begin with a period are hidden from the user and are not displayed by `ls`. However, you can include the `-a` (for "all") flag in an ls command and see everything in the target directory:

```Bash

ls -a /etc
```

You can even combine flags for brevity. For example, rather than enter `ls -a -l /etc` to show all files and directories in Linux's /etc directory in long form, you can enter this instead:

```Bash

ls -al /etc

```

### Variables

Variables may contain a number, character or a string of characters. These variables do not need to be declared, nor are there data types. They are simply assigned. 

```Bash

variable1="This is a variable." 
echo $variable1

```

```Bash

var1=$(ls) 
echo $var1

```
Set `var1` equals and instead of using quotes, a dollar sign parentheses, which is going to execute anything that occurs in that dollar sign parentheses. So this is in place execution of the `ls` command. Now, if I echo out `var1`. This is what `ls` was at the time, it was executed upon variable assignment. If I were to remove one of these files now and echo out `var1`, it would still show all 4.

#### Bourne Shell Variable 

- `$HOME` the current user's home directory
- `$PS1` the primary prompt string 
- `$PATH` a colon-seperated list of directories where the shell looks for command. In other words, the `$PATH` variable is an environment variable that contains all of    the directories that are automatically searched when we try to call a program. 
try: `echo $PATH | tr ":" "\n"`

#### Lab: 
- **Examine the current `$PATH` variable**

<img width="871" alt="Variable lab1" src="https://user-images.githubusercontent.com/97931452/161654317-54c84337-6093-4fde-9dbe-37d8227bb24b.PNG">

1. Determine the current working directory.
`pwd`

2. List the contents of the current directory.
`ls`

3. List the contents of the scripts folder.
`ls scripts/`

4. Run the test.sh script, specifying the path to it.
`./scripts/test.sh`

5. Attempt to run the test.sh script without specifying the path to it.
`test.sh`

6. List the current environment variables, and locate the $PATH variable.
`env`

7. Examine the $PATH variable.
`echo $PATH`

- **Append the Path to the scripts Directory to the $PATH Variable**

<img width="270" alt="Variable lab2" src="https://user-images.githubusercontent.com/97931452/161654345-abf43f69-490e-4e06-9db2-4db769dd830e.PNG">

1. Run the following command:
`PATH="$PATH:$HOME/scripts"`

2. Run the test.sh script again without specifying the path.
`test.sh`

- **Make the New Path Persist**

<img width="943" alt="Variable lab3" src="https://user-images.githubusercontent.com/97931452/161654364-410d7aeb-4333-4671-a7ce-407e634ad7f0.PNG">


1. View the contents of the .profile file.
`cat .profile`

2. View the $PATH variable.
`echo $PATH`

3. Source the .profile file.
`source .profile`

4. Modify the ~/.profile file to make our change permanent.
`echo 'PATH="$PATH:$HOME/scripts"' >> ~/.profile`

5. Source the .profile file again.
`. .profile`

6. View the $PATH variable again.
`echo $PATH`

7. Run the test.sh script without specifying the path again.
`test.sh`

- [Source command](https://linuxize.com/post/bash-source-command/) 
- [Login shell](https://linuxhandbook.com/login-shell/)


### Quoting
Quoting preserves input that contains special characters or spaces. 

- **Escape Character** is a a non-quoted backslash `\` and it preserves the literal value of the next following character       with a single exception of newline. Newline is represented by \ followed by an N.
  
- **Single Quotes** preserve the literal value of every character contained within the quotes, including the escape             character. Let's say we already know we have a variable in var1. Let's echo out and we're going to use single quotes, 'this   is $var1', and we'll close that single quote. Now, when I hit Enter, it's going to preserve the literal value of the dollar   sign var1. It's not going to expand it out as the variable itself.

- Double Quotes preserve the literal value of most characters contained within the quotes, exceptions for the dollar sign for   variables, single quotes for single quoting, and the backslash for escaping a character.

![image](https://user-images.githubusercontent.com/97931452/161565757-cecd1fd6-92e1-478e-92fa-8988a057a216.png)


## Getting Help

### Man Pages 

Man pages are the traditional package documentation for application usage. They are typically installed when you install a package. So if we install a package to do some task or to perform some process. The man page for that package will typically be installed at the same time. This gives us the ability to take a look at that documentation and make sure that we're using it in a manner consistent with its design.

Tip: To search through the man page, enter forward slash and the keyword, it's going to highlight every instance of the keyword in this man page

### Info Pages

Info pages are additional documentation with more robust capability in detail than a man page. Additionally, info uses a structure for linking these pages together and they may be assembled into a larger collection.


## Using Directories and Listing Files

### Files and Directories

The Filesystem Hierarchy Standard (FHS) defines structure of the file systems on Linux. 

| Directory  | Name | 
| ------------- | ------------- | 
| /  | the root directory | 
| /bin | user binaries |
| /boot | static boot files |
| /dev | device files | 
| /etc | configuration files |
| /home | home directories |
| /lib | device files | 
| /mnt | temporary mount files |
| /opt | optional packages |
| /proc | kernel and process files | 
| /root | root user home directory |
| /run | application state files |
| /sbin | system administration binaries | 
| /srv | service data |
| /tmp | temporary files |
| /usr | user binaries | 
| /var | variable data files |

![Linux directories](https://user-images.githubusercontent.com/97931452/161870304-9b865c92-4a33-4e54-a2f4-b812352ac919.jpg)

`/` is the top of the file system, equivalent of the C drive in Windows. `/bin` contains commands that can be used by user. `/boot` contains boot files to boot the system.  `/etc` contains configuration files. `/mnt` mount drives. `/tmp` contains transient files. You can have many filesystem on your disks, depending on how they are partitioned. `ext4` is the most current version of the native Linux filesystems. 

![image](https://user-images.githubusercontent.com/97931452/162121745-bb600338-4091-468d-88be-8fc8ab4691ce.png)

The `df` command reports file system disk space usage and other details about your disk.

Disks are comprised of **partitions** that help us organize our data. You can have multiple partitions on a disk and they can't overlap each other. If there is space that is not allocated to a partition, then it is known as free space. The types of partitions depend on your **partition table**. Inside a partition, you can have a filesystem or dedicate a partition to other things like swap (used to allocate virtual memory to our system). Every disk will have a **partition table**, this table tells the system how the disk is partitioned. This table tells you where partitions begin and end, which partitions are bootable, what sectors of the disk are allocated to what partition, etc. There are two main partition table schemes used, Master Boot Record (MBR) and GUID Partition Table (GPT).

![image](https://user-images.githubusercontent.com/97931452/162125230-8c434bfb-2523-49be-bde2-96df8f604391.png)

`sudo parted -l` to check partition tables. 

### Moving around ###

- `cd .` (current directory). This is the directory you are currently in.
- `cd ..` (parent directory). Takes you to the directory above your current.
- `cd ../..` (parent directory). Go up two levels above current.
- `cd ~` (home directory). This directory defaults to your “home directory”. Such as /home/pete.
- `cd -` (previous directory). This will take you to the previous directory you were just at.

### Hidden Files and Directories

Files and directories that are hidden from basic listing by preceding their name with a period. Hidden files may be listed via `ls` using the `-a` option, to show all files. 

### Home Directories 

A home directory is typically created for every ordinary user on a Linux system under `/home`.

``` bash
cat /etc/passwd
```
![image](https://user-images.githubusercontent.com/97931452/161575462-6a408802-1d8e-4ee3-8893-446f679c407f.png)


So if I take a look at the file and I'm using the cat command here `/etc/passwd`, this is a file that contains all of the users on a Linux system. These are going to be unique and so the reason we have this is because if we're using non-local authentication, we could have multiple users named michael, each one needs to have a unique ID. `/etc/passwd` just shows us the local users for this Linux system. And so the username maps to the user ID 1000, `/home/ailin`, this is the home directory. `/bin/bash` is the default shell that I received. So here's an example of a service account, sshd. It has the UID of 109. It has the home directory of `/run/sshd`, so files it generates will be placed there and remember /run is application data and then it's log in shell is `/usr/sbin/nologin`. It doesn't get a login shell. This is a shell that prevents login. `/etc/passwd` is basically the master mapping on a Linux system of users to user IDs, which are all unique, as well as the home directory and the login shell. So this is where the home directory is defined.

![etc-passwd-file-explained](https://user-images.githubusercontent.com/97931452/161656889-5ed3ecff-fd33-4e25-8740-317d10192ef9.png)


### Absolute and Relative Paths

The path to the unique location of a file or directory. 

<img src="https://user-images.githubusercontent.com/97931452/161577992-aaef35e0-7712-4b69-a4bb-817d360f530b.jpg" width=50% height=50%>

If working directory is user, then

- Relative path: file1
- Absolute path: /home/user/file1

## Working with Files and Directories

### Creating, Moving, Deleting 

`mkdir <NAME>` Create new directory

`cp -r <SOURCE> <DESTINATION>` Copy a directory

`mv <SOURCE> <DESTINATION>` Move a directory

`rm -r <DIRECTORY>` Delete a directory
  
`touch <NAME>` Create a new file

`cp <SOURCE> <DESTINATION>` Copy a file

`mv <FILE> <NEW LOCATION>` Move a file

`rm <FILE>` Delete a file

### Case Sensitivity 
  
Most of the common Linux file systems are case sensitive. Lower-case and upper-case letters have different ASCII representation. 

### Simple Globbing

Globbing is primarily used to match patterns in file names or text by using a wildcard character to create the pattern.
  
- `*` the wildcard of wildcards, it's used to represent all single characters or any string.
  
![image](https://user-images.githubusercontent.com/97931452/161581370-87271ac8-b129-4ffd-8ee2-256d6d7a43c0.png)

- `?` used to represent one character
  
![image](https://user-images.githubusercontent.com/97931452/161581201-92e967be-ebed-4277-aa21-6869d495fb17.png)

- `[]` used to represent any character from range within the brackets
  
![image](https://user-images.githubusercontent.com/97931452/161581433-64deda82-8593-4026-8b27-4ff6933a316f.png)

```bash
$ cp *.jpg /home/pete/Pictures
```
This will copy all files with the .jpg extension in your current directory to the Pictures directory.

A useful command is to use the `-r` flag, this will recursively copy the files and directories within a directory.
 
```bash
$ cp -r Pumpkin/ /home/pete/Documents
```
One thing to note, if you copy a file over to a directory that has the same filename, the file will be overwritten with whatever you are copying over. If you have a file that you don’t want to get accidentally overwritten. You can use the `-i` flag (interactive) to prompt you before overwriting a file.

```bash
$ cp -i mycoolfile /home/pete/Pictures

``` 
  
# Command Line
  
## Archiving Files on the Command Line
  
**Archive** to make backups, save space. So archiving is the process of combining multiple files and or directories into a single file. This is generally done as part of a backup process. The most common utility for creating and working with archives in Linux is `tar`, which is short for tape archive.
  
**Options**
  
 `-c` create archive
  
 `-x` extract archive
  
 `-r` append to an archive
 
 `-t` list the contents of an archive
  
 `-f` read from or write to a file 
 
**Compression** is the process of reducing the amount of storage that files or archives consume. Compression is typically used during archiving to reduce storage space. The three most common compression algorithms are: 
  
- **gzip** the default compression used by `tar` via (`-z`), a good balance of speed and size reduction
  
- **bzip2** an alternative compression algorithm, typically slower than gzip due to higher compression

- **zip** the algorithm used by zip command, and all-in-one compression and archiving utility popular with other operatiing systems.   

## Searching and Extracting Data from Files

### Command Line Pipes   

**Piping** is the process of using the output of one command as the input for another. 

- `|` The pipe symbol  

- `grep` Utility that searches any input files, selecting lines that match one or more patterns. 
  
Tip: If I wanted to rerun say this command here, wc -l american-english.
It was the last time I ran the wc command,
not including when it was piped.
I can use a bang or a exclamation point
wc and it will rerun the last command I
used starting with wc.
I can use a bang and cat.
It's going to rerun the last time I started a command with cat.


### I/O Redirection 
  
**I/O redirection** may be used to feed input to a command from a file or to send the output of a command to a file. 

`[COMMAND] < [FILE]` Read input from a file
                  
`[COMMAND] > [FILE]` Send output to a file
 
### Basic Regular Expressions  

**Regular expressions** (or regex) are used to match patterns in text. 

`"^Apple"` Match start of line
 
`"Apple$"` Match end of line

`"^Apple$"` Match start and end of line

`"^Apple|Ball"` Match either string or character

`"Ap*le"` Match A, followed by zero *or* more p's, followed by le

`"Ap+le"` Match A, followed by one *or* more p's, followed by le

`"Ap?le"` Match A, followed by maybe a p, followed by le

`"Ap{p-z}le"` Match Ap, followed by a letter between p and z, followed by le

Regular Expressions Cheatsheet: 

https://regexr.com/

https://regexone.com/

## Turning Commands into Scripts

### Basic Shell Scripting

**Anatomy of a Shell Script**

```bash 
#!/bin/bash

echo "Please enter your name: "
read name 
echo -e "Hello $name!\n"

```

`#!/bin/bash` This line defines the interpretor to be used by the shell script


### Common Text Editors 

**vim** 

To fire up vim just type:
   
```bash
vim
```
   
**Useful commands**

To navigate a text document in vim, use the following keys:

`h` or the left arrow - will move you left one character
`k` or the up arrow - will move you up one line
`j` or the down arrow - will move you down one line
`l` or the right arrow - will move you right one character
   
`gg` Go to the first line of the file
 
`G` Go to the last line of the file 
  
`10G` Go to the 10th line of the file

Now you may have noticed if you tried to type something you wouldn't be able to. That's because you are in *command mode*. This can get pretty confusing especially if you just want to open a file and enter text. The command mode is used for when you enter commands like `h,j,k.l` etc. To insert text you'll need to enter *insert mode* first.

`i` Insert at cursor
  
`l` Insert at start of line
  
`o` Append line under cursor

Notice how when you type any of these insertion modes, you'll see that vim has entered insert mode at the bottom of the shell. To exit insert mode and go back to command mode, just hit the Esc key.

`:w` Write file 
  
`:q` Quit vim

`:wq` Write and quit

`u` undo your last action
   
`Ctrl-r` redo your last action

# Operating Systems

## Choosing an OS

### Differences between Operating Systems

| OS | Linux | macOS | Windows |
| --- | --- | --- | --- |
| Open Source | Yes | No | No |   
| Purchase Price | Free | Free | Varies |  
| Supported Hardware | Excellent | Proprietary | Good |
| Shell Interpreter | Bash | Bash | Powershell |  
| GUI | Multiple | macOS | Windows |

Linux has enterprise licensing and support like RedHat. macOS is only available on proprietary hardware. 

### Distribution Lifecycle

**Standard distribution release**, also known as the point release or a stable release is made available after a development period. During this development period, all software is updated to a specific version and then frozen.
It is then tested to verify that all software versions work well together and then updates are released to address important bugs and security concerns. Now on the other end of the spectrum, we have more of a cutting edge and that is the **rolling release**. So some distributions are always kept up to date using small and constant updates to the core of the OS and then new versions of the software are added as they arrive. These are generally more cutting edge and you are constantly updating the software. So for instance, Arch Linux is an example of that. There is no Arch Linux 18.04, you know, there is only Arch Linux. It's always the newest version. Whereas you have a Ubuntu 18.04, you have Red Hat Enterprise Linux 7.5, Red Hat Enterprise Linux 8.0. 

## Computer Hardware

Hardware is the physical component used for computing. 

| Hardware | Function | 
| --- | --- | 
| Central Processing Unit (CPU) | Processes computer functions and performs calculations | 
| Random Access Memory (RAM) | High-performance, volatile storage | 
| Secondary Storage (HDD/SSD) | Persistent storage for data not currently in use | 
| Network Interface Card (NIC) | Permits connections to a network | 
| Input Devices (Mouse/Keyboard) | Send data into the computer via human interaction | 
| Output Devices (Monitor) | Send information from the computer to the user | 


<img src="https://user-images.githubusercontent.com/97931452/162002614-f9c17ccb-b273-41a2-b4dc-e07f1a544c05.jpg" width=50% height=50%>

Hardware drivers reside in the running kernel (or are loaded as a module) and enable the operating system to use the hardware. The kernel in itself is a monolithic piece of software, when we want to add support for a new type of keyboard, we don't write this code directly into the kernel code. Just as we wouldn't meld a bike rack to our car. Kernel modules are pieces of code that can be loaded and unloaded into the kernel on demand. They allow us to extend the functionality of the kernel without actually adding to the core kernel code.

## Data Storage 

### Programs and Configuration

| File  | Description | 
| --- | --- | 
| System Boot Configuration `/boot` | Contains boot loader configuration files and parameters, Linux kernel, and initial RAM disk |
| Partition Mount Points `/etc/fstab` | Contains a list of partitions to mount automatically and where they mount in the filesystem |
| User Attributes `/etc/passwd` | Contains a list of local users and their attributes |
| Groups  `/etc/group` | Contains a list of local users and attributes |
| Hosts File  `/etc/hosts` | Contains a list of IP addresses and the hostname we want the system to associate with them |
| Application Configuration `/etc/<APPLICATION>` | Applications place their respective configuration files in the `/etc` directory, normally as a .conf file | 
 
These are common locations for system and configuration data. Everything in `/etc` is configuration-related. 


![image](https://user-images.githubusercontent.com/97931452/162192512-a61a10cf-4c87-4c99-b72d-73c98bbb6e25.png)

- `/boot` directory contrains  `GRUB` folder which is the default boot loader. There are config, initial RAM disks, system map and vmlinuz file which is kernel 5.4.0-91. Use `uname -r` to see which kernel I'm currently running. The kernel has a corresponding system map and initial RAM disk. 
`cat config-5.4.0-91-generic` to see the configuration parameters that have been set.

![image](https://user-images.githubusercontent.com/97931452/162193527-15ec3c68-938e-4f69-a289-0acd6f1815b9.png)

- When we want to automatically mount filesystems at startup we can add them to a file called `/etc/fstab` (pronounced "eff es tab") short for filesystem table. This file contains a permanent list of filesystems that are mounted.

![image](https://user-images.githubusercontent.com/97931452/162199372-6249630e-b342-4279-ba8f-0719deb212e1.png)

- Each line represents one filesystem, the fields are:

  - UUID - Device identifier
  - Mount point - Directory the filesystem is mounted to
  - Filesystem type
  - Options - other mount options
  - Dump - used by the dump utility to decide when to make a backup, you should just default to 0
  - Pass - Used by fsck to decide what order filesystems should be checked, if the value is 0, it will not be checked

- `blkid`: To view the UUIDS on your system for block devices

![image](https://user-images.githubusercontent.com/97931452/162200389-96191640-9794-4bfa-84a3-9bb25c02a39a.png)

- `/etc/hosts` a mapping of IP addresses to host names.

![image](https://user-images.githubusercontent.com/97931452/162209939-eb2c2c3f-2c19-4ff6-9d29-51b204b9f6e2.png)

- `ll /etc/` configuration files for applications

![image](https://user-images.githubusercontent.com/97931452/162218261-d5a9bc76-e646-4bf8-811c-da115a56b5f2.png)


### Processes

Processes are the programs that are running on your machine. They are managed by the kernel and each process has an ID associated with it called the **process ID (PID)**. This **PID** is assigned in the order that processes are created.

![image](https://user-images.githubusercontent.com/97931452/162226381-ff0205e7-bba9-4589-891b-362effadd225.png)

`ps` command to see a list of running processes.

This shows you a quick snapshot of the current processes:

**PID**: Process ID

**TTY**: Controlling terminal associated with the process

**TIME**: Total CPU usage time

**CMD**: Name of executable/command

`ps aux` 

**USER**: The effective user (the one whose access we are using)
**PID**: Process ID
**%CPU**: CPU time used divided by the time the process has been running
**%MEM**: Ratio of the process's resident set size to the physical memory on the machine
**VSZ**: Virtual memory usage of the entire process
**RSS**: Resident set size, the non-swapped physical memory that a task has used
**TTY**: Controlling terminal associated with the process
**STAT**: Process status code
**START**: Start time of the process
**TIME**: Total CPU usage time
**COMMAND**: Name of executable/command

`top` command gives you real time information about the processes running on your system instead of a snapshot. By default you'll get a refresh every 10 seconds. It is a useful tool to see what processes are taking up a lot of your resources.

Process information is stored in a special filesystem known as the **/proc filesystem**.

`ls /proc` You should see multiple values in here, there are sub-directories for every PID. 

`cat /proc/<PID>/status` You should see running process information and well as more detailed information. 

`/sys` provides system information regarding attached hardware

`/dev` contains device files 

### System Messaging 

System messages are messages from the running kernel. 

![image](https://user-images.githubusercontent.com/97931452/162237914-b5665fba-8431-44fa-bea4-be513a76c35d.png)

### Logging 

The services, kernel, daemons, etc on your system are constantly doing something, this data is actually sent to be saved on your system in the form of logs. This allows us to have a human readable journal of the events that are happening on our system. This data is usually kept in the `/var` directory where we keep our variable data, such as logs. How are these messages getting received on your system? There is a service called **syslog** that performs log message collection. 

## Network 

### Networks and Routers 

### DNS Client Configuration

### Network Configuration


_[Back to the top](#table-of-contents)_

  
  
  

  
  

