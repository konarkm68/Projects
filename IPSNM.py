from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

class IPSNM_calc():
    def ipv4():
        print(f"{Fore.BLUE}\n\t1. IPv4 {Style.RESET_ALL}")
        ip_add=input(f"Enter the Decimal IP address : {Fore.YELLOW}")

        ip_add=ip_add.split(".") #split the IP address into 4 octets
        for i in range(0,4):
            ip_add[i]=bin(int(ip_add[i]))
            ip_add[i]=ip_add[i].replace("0b","")
            while len(ip_add[i])<8:
                ip_add[i]="0"+ip_add[i]
            ip_add[i]=str(ip_add[i])

        ip_add_bin=".".join(ip_add)
        print(f"{Fore.BLUE}Binary IP address{':':>13} {ip_add_bin}")

        SN_mask=int(input(f"Enter the Sub-Net Mask (1-32): {Fore.YELLOW}"))

        SNM_bin=""
        for i in range(0,SN_mask):
            SNM_bin=SNM_bin+"1"
        while len(SNM_bin)<32:
            SNM_bin=SNM_bin+"0"

        SNM_bin_list=[]
        for i in range(0,4):
            SNM_bin_list.append(SNM_bin[8*i:8*(i+1)])

        SNM_dec_list=[]
        for i in range(0,4):
            SNM_dec_list.append(str(int(SNM_bin_list[i],2)))

        SNM_dec=".".join(SNM_dec_list)
        print(f"{Fore.BLUE}Decimal Sub-Net Mask{':':>10} {SNM_dec}")

        SNM_bin=".".join(SNM_bin_list)
        print(f"{Fore.BLUE}Binary Sub-Net Mask{':':>11} {SNM_bin}")

    def ipv6():        
        print(f"{Fore.BLUE}\n\t2. IPv6 {Style.RESET_ALL}")

        ip_add=input(f"Enter the Hexa-Decimal IP address : {Fore.YELLOW}")

        ip_add=ip_add.split(":") #split the IP address into 8 octets
        for i in range(0,8):
            ip_add[i]=bin(int(ip_add[i],16))
            ip_add[i]=ip_add[i].replace("0b","")
            while len(ip_add[i])<16:
                ip_add[i]="0"+ip_add[i]
            ip_add[i]=str(ip_add[i])

        for i in range(0,8):   
            octet = f"{Fore.BLUE}Binary IP address Octet-{i+1}:"
            print(f"{octet:>40} {ip_add[i]}")

        SN_mask=int(input(f"Enter the Sub-Net Mask (1-128){':':>5} {Fore.YELLOW}"))

        SNM_bin=""
        for i in range(0,SN_mask):
            SNM_bin=SNM_bin+"1"
        while len(SNM_bin)<128:
            SNM_bin=SNM_bin+"0"


        SNM_bin_list=[]
        for i in range(0,8):
            SNM_bin_list.append(SNM_bin[16*i:16*(i+1)])

        SNM_hex_list=[]
        for i in range(0,8):
            SNM_hex_list.append(hex(int(SNM_bin_list[i],2)))
            SNM_hex_list[i]=SNM_hex_list[i].replace("0x","")
            while len(SNM_hex_list[i])<4:
                SNM_hex_list[i]="0"+SNM_hex_list[i]

        SNM_hex=":".join(SNM_hex_list)
        print(f"{Fore.BLUE}Hexa-Decimal Sub-Net Mask{':':>10} {SNM_hex}")

        for i in range(0,8):    
            octet = f"{Fore.BLUE}Binary Sub-Net Mask Octet-{i+1}:"
            print(f"{octet:>40} {SNM_bin_list[i]}")

    def main():
        colorama_init(autoreset=True)
        print(f"\t\t  {Fore.BLUE}IP Sub-Net Calculator{Style.RESET_ALL}")
        IPSNM_calc.ipv4()
        IPSNM_calc.ipv6()

    def __init__(self):
        IPSNM_calc.main()

if __name__ == "__main__":
    IPSNM_calc()