from colorama import init, Fore, Back, Style
import os
import subprocess
from tools import *
init(autoreset=True)
def check_sources():
    with open("/etc/apt/sources.list", "r") as sources:
        for line in sources:
            if "kali-rolling" in line:
                return True
    return False

def addKaliRepository():
    if check_sources():
            print(Fore.BLUE + "Kali sources already exist. Run the script again and install the tools")
    else:
        print("Adding Kali sources")
        with open("/etc/apt/sources.list", "a") as sources:
            sources.write("deb http://http.kali.org/kali kali-rolling main non-free contrib")
            os.system("apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ED444FF07D8D0BF6")
        os.system("apt update")
        os.system("apt autoremove --purge")
        print("Kali sources added")
def installCommand(category,tool):
    if category == "InformationGathering":
         subprocess.call('apt install -y '+InformationGathering[tool-1], shell=True)
    elif category == "VulnerabilityAnalysis":
         subprocess.call('apt install -y '+VulnerabilityAnalysis[tool-1], shell=True)
    elif category == "PasswordAttacks":
         subprocess.call('apt install -y '+PasswordAttacks[tool-1], shell=True)
    elif category == "Forensics":
         subprocess.call('apt install -y '+Forensics[tool-1], shell=True)
    elif category == "WebApplicationAnalysis":
         subprocess.call('apt install -y '+WebApplicationAnalysis[tool-1], shell=True)
    elif category == "WirelessAttacks":
         subprocess.call('apt install -y '+WirelessAttacks[tool-1], shell=True)
    elif category == "ReverseEngineering":
         subprocess.call('apt install -y '+ReverseEngineering[tool-1], shell=True)
    elif category == "SniffingSpoofing":
         subprocess.call('apt install -y '+SniffingSpoofing[tool-1], shell=True)

def installAll(category):
     print('Installing all tools')
     for i in range(1,58):
         installCommand(category,i)
     print(f'All tools of {category} installed')
def installTools():
     print(Fore.CYAN+'''
        Select Category:
           
         1 - Information Gathering
         2 - Vulnerability Analysis
         3 - Password Attacks
         4 - Database Assessment
         5 - Web Applications Analysis
         6 - Wireless Attacks
         7 - Reverse Engineering
         8 - Exploitation Tools
         9 - Sniffing & Spoofing
        10 - Post Exploitation
        11 - Forensics
        12 - Social Engineering Tools
        13 - Most Used Tools
    ''')
     option = int(input("Enter your option: "))
     if option == 1:
          category = "InformationGathering"
          print(Fore.CYAN+'''
                1) acccheck
                2) amap
                3) nmap
                4) dnsenum
                5) dnsmap
                6) dnsrecon
                7) dnstracer
                8) dnswalk
                9) enum4linux
               10) fierce
               11) fragroute
               12) fragrouter
               13) goofile
               14) lbd
               15) masscan
               16) metagoofil
               17) ntop
               18) p0f
               19) recon-ng
               20) set
               21) smtp-user-enum
               22) snmpcheck
               23) sslcaudit
               24) sslsplit
               25) sslstrip
               26) sslyze
               27) theharvester
               28) urlcrazy
               29) wireshark
               30) xplico
               31) intrace
               32) hping3
                0) INSTALL ALL TOOLS
        ''')
          tool = int(input('Enter a option:'))
          if tool != 0:
                installCommand(category,tool)
          elif tool == 0:
               installAll(category)
          else:
               print("Invalid option")
     elif option == 2:
          category = "VulnerabilityAnalysis"
          print(Fore.CYAN+'''
            1) cisco-auditing-tool
            2) commix
            3) lynis
            4) nmap
            5) sqlmap
            6) nikto
            7) unix-privesc-check
            8) legion
            9) spike
            0) INSTALL ALL TOOLS
             ''')    
          tool = int(input('Enter a option:'))
          if tool != 0:
                installCommand(category,tool)
          elif tool == 0:
               installAll(category)
          else:
               print("Invalid option")
     elif option == 3:
          category = "PasswordAttacks"
          print(Fore.CYAN+'''
             1) cewl
             2) cisco-auditing-tool
             3) chntpw
             4) cmospwd
             5) creddump
             6) crunch
             7) findmyhash
             8) impacket
             9) hydra
            10) john
            11) johnny
            12) ncrack
            13) patator
            14) rainbowcrack
            15) rsmangler
            16) wordlists
            17) zaproxy
             0) INSTALL ALL TOOLS
         ''')
          tool = int(input("Enter a option:"))
          if tool != 0:
                installCommand(category,tool)
          elif tool == 0:
               installAll(category)
          else:
               print("Invalid option")
     
     elif option == 4:
          category = "DatabaseAssessment"
          print(Fore.CYAN+'''
               1) sqlite
               2) sqlmap
             ''')
          tool = int(input('Enter a option:'))
          if tool != 0:
                if tool ==1:
                     subprocess.call('apt install -y sqlite', shell=True)
                     print('Selected tool installed')
                elif tool == 2:
                     subprocess.call('apt install -y sqlmap', shell=True)
                     print('Selected tool installed')
                else :
                     print("Invalid option")
          elif tool == 0:
               subprocess.call('apt install -y sqlite sqlmap', shell=True)
               print(f'All tools of {category} installed')
          else:
               print("Invalid option")
     elif option == 5:
          category = "WebApplicationsAnalysis"
          print(Fore.CYAN+'''
                1) burpsuite
                2) wpscan
                3) dirbuster
                4) dirb
                5) gobuster
                6) cadaver
                7) nikto
                8) davtest
                9) wafw00f
               10) wapiti
               11) whatweb
               12) commix
                0) INSTALL ALL TOOLS''')
          tool = int(input('Enter a option:'))
          if tool != 0:
                installCommand(category,tool)
          elif tool == 0:
               installAll(category)
          else:
               print("Invalid option")
     elif option == 6:
          category = "WirelessAttacks"
          print(Fore.CYAN+'''
               1) bully
               2) fern-wifi-cracker
               3) spooftooph
               4) aircrack-ng 
               5) kismet
               6) wifite
               7) pixiewps
               8) reaver
               0) INSTALL ALL TOOLS
                ''')
          tool = int(input('Enter a option:'))
          if tool != 0:
                installCommand(category,tool)
          elif tool == 0:
               installAll(category)
          else:
               print("Invalid option")
     elif option == 7:
          category = "ReverseEngineering"
          print(Fore.CYAN+'''
               1) clang
               2) clang++
               3) ghidra
               4) NASM shell
               5) radare2
               0) INSTALL ALL TOOLS
                ''')
          tool = int(input('Enter a option:'))
          if tool != 0:
                installCommand(category,tool)
          elif tool == 0:
               installAll(category)
          else:
               print("Invalid option")
     elif option == 8:
          category = "ExploitTools"
          print(Fore.CYAN+'''
          1) exploitdb
          2) metasploit-framework
          3) searchsploit
          4) sqlmap
          5) crackmapexec
          6) social engineering toolkit
          0) INSTALL ALL TOOLS
          ''')
          tool = int(input('Enter a option:'))
          if tool != 0:
               if tool == 1:
                    subprocess.call('apt install -y exploitdb', shell=True)
                    print('Selected tool installed')
               elif tool == 2:
                    subprocess.call('apt install -y metasploit-framework', shell=True)
                    print('Selected tool installed')
               elif tool == 3:
                    subprocess.call('apt install -y searchsploit', shell=True)
                    print('Selected tool installed')
               elif tool == 4:
                    subprocess.call('apt install -y sqlmap', shell=True)
                    print('Selected tool installed')
               elif tool == 5:
                    subprocess.call('apt install -y crackmapexec', shell=True)
                    print('Selected tool installed')
               elif tool == 6:
                    subprocess.call('git clone https://github.com/trustedsec/social-engineer-toolkit setoolkit/ && cd setoolkit && python3 setup.py', shell=True)
                    print('Selected tool installed')
          elif tool == 0:
               subprocess.call('apt install -y exploitdb metasploit-framework searchsploit sqlmap crackmapexec', shell=True)
               subprocess.call('git clone https://github.com/trustedsec/social-engineer-toolkit setoolkit/ && cd setoolkit && python3 setup.py', shell=True)
               print(f'All tools of {category} installed')
          else: 
               print("Invalid option")
     elif option == 9:
          category="SniffingSpoofing"
          print(Fore.CYAN+'''
               1) dnschef
               2) dsniff
               3) netsniff-ng
               4) rebind
               5) sslsplit
               6) tcpreplay
               7) ettercap
               8) macchanger
               9) minicom
               10) mitmproxy
               11) responder
               12) scapy
               13) tcpdump
               14) wireshark
          ''')
          tool = int(input('Enter a option:'))
          if tool != 0:
               installCommand(category,tool)
          elif tool == 0:
               installAll(category)
          else:
               print("Invalid option")
     elif option == 10:
          category = "PostExploitation"
          print(Fore.CYAN+'''
             1) dbd
             2) powersploit
             3) sbd
             4) proxychains4
             5) weevely
             0) INSTALL ALL TOOLS
          ''')
          tool = int(input('Enter a option:'))
          if tool != 0:
               if tool == 1:
                    subprocess.call('apt install -y dbd', shell=True)
                    print('Selected tool installed')
               elif tool == 2:
                    subprocess.call('apt install -y powersploit', shell=True)
                    print('Selected tool installed')
               elif tool == 3:
                    subprocess.call('apt install -y sbd', shell=True)
                    print('Selected tool installed')
               elif tool == 4:
                    subprocess.call('apt install -y proxychains4', shell=True)
                    print('Selected tool installed')
               elif tool == 5:
                    subprocess.call('apt install -y weevely', shell=True)
                    print('Selected tool installed')
          elif tool == 0:
               subprocess.call('apt install -y dbd powersploit sbd proxychains4 weevely', shell=True)
               print(f'All tools of {category} installed')
          else: 
               print("Invalid option")
     elif option == 11:
          category = "Forensics"
          print(Fore.CYAN+'''
               1) autopsy
               2) scalpel
               3) scrounge-ntfs
               4) guymager
               5) pdf-parse
               6) binwalk
               7) sleuthkit
               8) bulk-extractor
               0) INSTALL ALL TOOLS
          ''')
          tool = int(input("Enter a option: "))
          if tool != "0":
               installTools(category,tool)
          elif tool == "0":
               installAll(category)
          else:
               print("Invalid option")
     elif option  == 12:
          category = " SocialEngineeringTools"
          print(Fore.CYAN+'''
               1) beef-xss
               2) maltego
               3) sherlock
               4) social engineering tool kit

               0) INSTALL ALL TOOLS
               ''')
          tool = int(input("Enter a option: "))
          if tool != "0":
               if tool == "1":
                    subprocess.call('apt install -y beef-xss', shell=True)
                    print('Selected tool installed')
               elif tool == "2":
                    subprocess.call('apt install -y maltego', shell=True)
                    print('Selected tool installed')
               elif tool == "3":
                    subprocess.call('apt install -y sherlock', shell=True)
                    print('Selected tool installed')
               elif tool == "4":
                    subprocess.call('git clone https://github.com/trustedsec/social-engineer-toolkit setoolkit/ && cd setoolkit && python3 setup.py', shell=True)
                    print('Selected tool installed')
               else:
                    print("Invalid option")
                    exit()
     elif option == 13:
          subprocess.call("apt install -y nmap metasploit-framework sqlmap burpsuite wpscan dirb gobuster ghidra wireshark macchanger minicom mitmproxy responder scapy tcpdump nikto enum4linux hydra john hashcat autopsy recon-ng netdiscover theharvester aircrack-ng wifite proxychains4 cewl crunch exploitdb amass beef-xss", shell=True)
def main():
     print(Fore.GREEN + '''
         ____  _____ ____ _____ ___   ___  _     ____  
        / ___|| ____/ ___|_   _/ _ \ / _ \| |   / ___| 
        \___ \|  _|| |     | || | | | | | | |   \___ \ 
         ___) | |__| |___  | || |_| | |_| | |___ ___) |
        |____/|_____\____| |_| \___/ \___/|_____|____/  v1.0
                                                        - Code.zer001

''')
     print(Fore. BLUE + '''
        Select an option:
        1. Add Kali repository
        2. Install Tools
        0. Exit
    ''')
     option = input("Enter your option: ")
     if option == "1":
          addKaliRepository()
     elif option == "2":
          installTools()
     elif option == "0":
          print(Fore.RED+"Exiting...")
          exit()
     else:
          print(Fore.RED+"Invalid option. Please try again.")
          main()


while True:
    if os.geteuid() == 0:
          main()
          exit()
    else:
         print('RUN THE PROGRAM AS ROOT!!')
         exit()

