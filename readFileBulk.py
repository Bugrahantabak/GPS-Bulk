#! /usr/bin/python
__author__ = 'Bugrahan Tabak'
__version__ = 'v1.1'
__date__ = '12.26.2019'

import datetime
import sys
sys.path.append('./venv/Lib')
import requests

'''
#TODO: ReadFile
##########################################################
How to use:
1- Edit the PROV user name.
2- Edit the PROV user password.
3- Edit the PROV IP and service.
4- Edit the body fields with your soap request. Your request should be inside of triple quotes (""").
5- Set counter_from and counter_until for loop. 
6- Execute the program.
7- Check soapOut.txt and failOut.txt files for outputs.
##########################################################
'''

#Do not put a empty line to the end of the file.

# PROV user name
# user = 'admin'
user = 'admin'

# PROV user password
# password = 'admin'
password = 'admin'

# PROV IP and service
# url = "http://47.168.155.134:8080/prov/services/User"
url = "http://47.168.155.134:8080/prov/services/DomainAdminService"

# DO NOT CHANGE - Header of the Soap file
# headers = {'content-type': 'text/xml', 'SOAPAction': ''}
headers = {'content-type': 'text/xml', 'SOAPAction': ''}

# Soap request body between """ """
# body =  """ <soapenv:Envelope  ...  </soapenv:Envelope>"""  //TODO: update


bodyFirstPart = """<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:dom="domain.ws.nortelnetworks.com">
   <soapenv:Header/>
   <soapenv:Body>
      <dom:removeDomain soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
         <in0 xsi:type="com:DomainNaturalKeyDO" xmlns:com="common.ws.nortelnetworks.com">
            <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">bulkdomain"""

bodySecondPart = """</name>
         </in0>
      </dom:removeDomain>
   </soapenv:Body>
</soapenv:Envelope>"""


# Open output files for success logs (when the status_code is 2XX) and fail logs (when the status_code is NOT 2XX)
try:
    # file_soapOut = open('\\soapOut.txt', 'a')
    file_soapOut = open('soapOut.txt', 'a')
except OSError:
    print('Error: Unable to open soapOut.txt file')
    sys.exit(1)
try:
    # file_failOut = open('D:\\Users\\btabak\\Desktop\\soapbulk\\failOut.txt', 'a')
    file_failOut = open('failOut.txt', 'a')
except OSError:
    print('Error: Unable to open failOut.txt file')
    sys.exit(1)

try:
    #Read Input File
    fileOrj = open('input.txt', 'r')
    Lines = fileOrj.readlines()
except OSError:
    print('Error: Unable to open input.txt file')
    sys.exit(1)

# Insert local timestamp to both files
file_failOut.writelines('\n\n\n######################\n' + str(datetime.datetime.now()) + '\n######################\n\n')
file_soapOut.writelines('\n\n\n######################\n' + str(datetime.datetime.now()) + '\n######################\n\n')



# Loop
for line in Lines:
    oneLine = line.strip()
    spt = oneLine.split()
    i = spt[0]
    # Send the request
    try:
        response = requests.post(url, data=bodyFirstPart + str(i) + bodySecondPart, headers=headers,
                                 auth=(user, password))
    except requests.exceptions.HTTPError as errh:
        print(str(i) + '. Http Error: ', errh)
        file_failOut.writelines(str(i) + '. Http Error: ' + str(errh) + ')\n')
        sys.exit(1)
    except requests.exceptions.ConnectionError as errc:
        print(str(i) + '. Error Connecting: ', errc)
        file_failOut.writelines(str(i) + '. Error Connecting: ' + str(errc) + ')\n')
        sys.exit(1)
    except requests.exceptions.Timeout as errt:
        print(str(i) + '. Timeout Error: ', errt)
        file_failOut.writelines(str(i) + '. Timeout Error: ' + str(errt) + ')\n')
        sys.exit(1)
    except requests.exceptions.RequestException as err:
        print(str(i) + '. Unknown Error: ', err)
        file_failOut.writelines(str(i) + '. Unknown Error: ' + str(err) + ')\n')
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
file_soapOut.close()
file_failOut.close()
fileOrj.close()
# Done!
print('Done!')



