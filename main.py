import requests
from requests.structures import CaseInsensitiveDict
import time


def main():
    if __name__ == '__main__':
        try:
            # Sets Cloud Server Addresses
            ip = input('Enter IP Address: ')

            url = 'http://{0}/eidc/setoutbound?username=admin&password=admin'.format(ip)

            headers = CaseInsensitiveDict()
            
            headers["Content-Type"] = "application/json"

            data = '{"maxRandomRetryInterval":600,"primaryHostAddress":"10.10.10.10","primaryPort":18800,"primarySsl":1,"retryInterval":0,"secondaryHostAddress":"serveraddress.com","secondaryPort":18800,"secondarySsl":1,"siteKey":""}'

            resp = requests.post(url, headers=headers, data=data)

            print(resp.json())

            # reboot controller
            time.sleep(5)

            con_reboot = 'http://{0}/eidc/reboot'.format(ip)
            get_reboot = requests.get(con_reboot)
            print(get_reboot.json())

            # Repeat
            next = input('repeat?y,n: ')
            if next == 'y':
                main()
            elif next == 'n':
                exit()
        finally:
            print()


main()
