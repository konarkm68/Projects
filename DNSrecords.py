import dns.resolver ## py -m pip install dnspython
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

class DNSrecords():
    def get_domain():
        root_domain = input(f'Enter Root-Domain: {Fore.YELLOW}')
        ## root_domain = 'example.com'
        sub_domain = input(f"{Style.RESET_ALL}Enter Sub-Domain (Press 'Enter' for root domain search'): {Fore.YELLOW}")
        sub_domain = sub_domain + '.'
        ## sub_domain = 'www.' OR '.'

        if sub_domain == '.':
            domain = root_domain
        else:
            domain = sub_domain + root_domain
        print(f"{Fore.BLUE}\nDomain: {domain} ('{sub_domain}' + '{root_domain}'){Style.RESET_ALL}\n")

        return domain, root_domain, sub_domain

    def get_DNSrecords(domain, root_domain, sub_domain):
        record_types = ['CNAME', 'SOA', 'NS', 'A', 'AAAA', 'SRV', 'MX', 'SPF', 'TXT'] 
        """ 
        ## can be extended with the following:
        , 'AFSDB', 'APL', 'CAA', 'CDNSKEY', 'CDS', 'CERT', 'CSYNC', 'DHCID', 'DLV', 'DNAME', 
        'DNSKEY', 'DS', 'EUI48', 'EUI64', 'HINFO', 'HIP', 'HTTPS', 'IPSECKEY', 'KEY', 'KX', 
        'LOC', 'NAPTR', 'NSEC', 'NSEC3', 'NSEC3PARAM', 'OPENPGPKEY', 'PTR', 'RRSIG', 'RP', 'SIG', 
        'SMIMEA', 'SSHFP', 'SVCB', 'TA', 'TKEY', 'TLSA', 'TSIG', 'URI', 'ZONEMD']
        """
        for record in record_types:
            if record == 'TXT':              
                sec_email_TXT_DNS = [
                    '_spf.', 
                    'google._domainkey.',
                    '_dmarc.', '*._report._dmarc.',
                    '_mta-sts.', '_smtp._tls.']
                for sec_email in sec_email_TXT_DNS:
                    try:
                        sec_email_result = dns.resolver.resolve(sec_email + root_domain, 'TXT')
                        for sec_email_txt in sec_email_result:
                            print('TXT-Secure Email', f"{Fore.BLUE}{sec_email_txt.to_text()}")
                    except:
                        continue
                print()

            elif record == 'SOA':
                SOA_result = dns.resolver.resolve(root_domain, 'SOA')
                for soa in SOA_result:
                    for soa_vals in soa.to_text().split(' '):
                        print('SOA', f"{Fore.BLUE}{soa_vals}")
                print()
                continue
            
            elif record in ['NS', 'MX', 'SPF']:
                try:
                    result = dns.resolver.resolve(root_domain, record)
                    for rec in result:
                        print(record, f"{Fore.BLUE}{rec.to_text()}")
                    print()
                except:
                    continue
                continue
            
            try:                
                result = dns.resolver.resolve(domain, record)
                for rec in result:
                    print(record, f"{Fore.BLUE}{rec.to_text()}")
                print()

            except Exception as e:
                print(record, f'{Fore.RED}No {record} Records')
                print(f"{Fore.RED}Reason: {e}", '\n')

    def main():
        try:
            colorama_init(autoreset=True)
            domain = DNSrecords.get_domain()
            DNSrecords.get_DNSrecords(domain[0], domain[1], domain[2])
            
        except Exception as e:
            print(f"\n\t{Fore.RED}Exception: {e}") 

    def __init__(self):
        DNSrecords.main()

if __name__ == '__main__':
    DNSrecords()