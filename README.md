# Port Scanner

Port scanning is a method for determining which ports on a network are open. As ports on a computer are the place where information is sent and received, port scanning is analogous to knocking on doors to see if someone is home.

By using this tool we can find the **OPEN** ports of an IP/Domain, so that we can manually check for the following vulnerabilities in the **OPEN** ports.

1. Check by connecting to the Open port.
2. Google the open port's banner for CVEs [https://www.cvedetails.com/].
3. Check to bypass the authentication of the Open Ports if any. 

### How to use the tool

- At first clone the repository to your local machine using:
  - ┌──(root💀kali)-[~/Desktop]<br>
    └─# git clone https://github.com/harimypala/portscanner.git

- Run the main.py using python3 in the cmd.
  -   ┌──(root💀kali)-[~]<br>
      └─# _python3 main.py_

- Provide the IP/Domain.
  - Can supply a single IP/Domain.<br>
    OR
  - Can supply Multiple IPs/Domains with a separation of ",".
- Hit Enter and this may take some time for better accuracy.

**_Note_**: _**Make sure to install all the supporting libraries (socket, termcolor, IPy, etc....) for successful execution of the code.**_ 

<br>
**_THANK YOU_**<br>
**_- Hari Mypala_**
