#! /usr/bin/python
__author__ = 'Bugrahan Tabak'
__version__ = 'v1.3'
__date__ = '2019'

import datetime
import sys
sys.path.append('./venv/Lib')
import requests
import config
print("###### Start!")

# PROV user name
user = config.config["prov_user_name"]

# PROV user password
password = config.config["prov_user_password"]

# PROV IP and service
url = config.config["prov_url"]

# DO NOT CHANGE - Header of the Soap file
# headers = {'content-type': 'text/xml', 'SOAPAction': ''}
headers = {'content-type': 'text/xml', 'SOAPAction': ''}
print("###### Read xml")
# Soap request body between """ """
requestXML=config.xmlRequest["xml"]
body=requestXML.strip().split('$')
print(requestXML)

# Counter from
counter_from = int(config.counterBulkConfig["counter_from"])
# Counter until
counter_until = int(config.counterBulkConfig["counter_until"])
print("###### Open log files")
# Open output files for success logs (when the status_code is 2XX) and fail logs (when the status_code is NOT 2XX)
try:
    file_soapOut = open(config.config["success_log_file_name"], 'a')
except OSError:
    print('Error: Unable to open success file.')
    sys.exit(1)
try:
    file_failOut = open(config.config["fail_log_file_name"], 'a')
except OSError:
    print('Error: Unable to open fail file.')
    sys.exit(1)
print("###### Insert date: "+str(datetime.datetime.now()))
# Insert local timestamp to both files
file_failOut.writelines('\n\n\n######################\n' + str(datetime.datetime.now()) + '\n######################\n\n')
file_soapOut.writelines('\n\n\n######################\n' + str(datetime.datetime.now()) + '\n######################\n\n')

def close_files():
  # Close files
    print("###### Close files")
    file_soapOut.close()
    file_failOut.close()
print("###### Send request")
# Loop
for i in range(counter_from, counter_until):

    # Send the request
    try:
        response = requests.post(url, data=body[0] + str(i) + body[1], headers=headers,
                                 auth=(user, password))
    except requests.exceptions.HTTPError as errh:
        print(str(i) + '. Http Error: ', errh)
        file_failOut.writelines(str(i) + '. Http Error: ' + str(errh) + ')\n')
        close_files()
        sys.exit(1)
    except requests.exceptions.ConnectionError as errc:
        print(str(i) + '. Error Connecting: ', errc)
        file_failOut.writelines(str(i) + '. Error Connecting: ' + str(errc) + ')\n')
        close_files()
        sys.exit(1)
    except requests.exceptions.Timeout as errt:
        print(str(i) + '. Timeout Error: ', errt)
        file_failOut.writelines(str(i) + '. Timeout Error: ' + str(errt) + ')\n')
        close_files()
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(i) + '. Unknown Error: ', err)
        file_failOut.writelines(str(i) + '. Unknown Error: ' + str(err) + ')\n')
        close_files()
        sys.exit(1)

    # Check response status code
    if response.status_code == 200: #TODO: Update for 2XX
        file_soapOut.writelines(str(i) + '. ' + str(response.content) + '\n')
        print(str(i) + ' Success.')
    else:
        file_failOut.writelines(
            str(i) + '. Failed with code: ' + str(response.status_code) + ' ' + str(response.content) + '\n')
        print(str(i) + '. Failed with code: ' + str(response.status_code) + ' ' + str(response.content))

# Close files
close_files()

# Done!
print('###### Done!')
