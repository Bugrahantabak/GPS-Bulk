comment = {
  "how_to_use" : ""

  }

config =  {
    "prov_user_name" : "admin",
    "prov_user_password" : "admin",
    "prov_url"  :"http://47.168.155.134:8080/prov/services/UserAdminService",
    "success_log_file_name" : "success_log.txt",
    "fail_log_file_name" : "fail_log.txt",
    "input_file_name" : "input.txt"
    }

counterBulkConfig ={
    "counter_from" : 5200,
    "counter_until" : 6000
    }

readFileBulkConfig ={
    "input_file_name" : "input.txt"
    }

xmlRequest={
    "xml" : """<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:user="user.ws.nortelnetworks.com">
       <soapenv:Header/>
       <soapenv:Body>
          <user:getUser soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
             <in0 xsi:type="com:UserNaturalKeyDO" xmlns:com="common.ws.nortelnetworks.com">
                <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">$</name>
             </in0>
          </user:getUser>
       </soapenv:Body>
    </soapenv:Envelope>"""
    }
