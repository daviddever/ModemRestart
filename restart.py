import requests
from bs4 import BeautifulSoup
import itertools
import netifaces
from datetime import datetime

def connection_up():
    r = requests.get('google.com')
    if int(r.status_code) == 200:
        return True

def get_page(tab):
    r = requests.get('http://192.168.100.1/' + tab)

    return r.text

def build_dictionary(html):
    soup = BeautifulSoup(html)
    table = soup.find_all(['td'])

    information = []

    for item in table:
        information.append(str(item)[4:-5])

    return dict(itertools.izip_longest(*[iter(information)] * 2, fillvalue=''))


while True:
    time.sleep(60)

    for _ in range(3):
        if connection_up:
            break

        time.sleep(10)

    else:
        # Get diagnostic information about local host and from Modem
        nic = netifaces.ifaddresses('eth0')
        nic[netifaces.AF_INET]

            try:
                status_html = get_page('indexData.htm')
                status = build_dictionary(status_html)

                address_html = get_page('cmAddressData.htm')
                address = build_dictionary(address_html)

                signal_html = get_page('cmSignalData.htm')
                logs_html = get_page('cmLogsData.htm')

            except:
                # Modem power off or unreachable
                break

            # Decide whether or not to restart the Modem
            if status['Cable Modem Status'] == 'Operational'
                r = requests.get('http://192.168.1.100/reset.htm')

                f = open('incident' + datime.now() + '.html', 'a')
                    f.write(status_html)
                    f.write(address_html)
                    f.write(signal_html)
                    f.write(logs.html)

                    if check_up:
                        f.write('Connection restored after restart')
                    else:
                        f.write('Connection still down after retart')
                f.close

                time.sleep(120)
