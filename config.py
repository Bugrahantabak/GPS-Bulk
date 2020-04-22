config =  {
    "prov_user_name" : "admin",
    "prov_user_password" : "admin",
    "prov_url"  :"http://47.168.90.122:8080/prov/services/sipPbxAdminService",
    "success_log_file_name" : "success_log.txt",
    "fail_log_file_name" : "fail_log.txt",
    "input_file_name" : "input.txt"
    }

counterBulkConfig ={
    "counter_from" : 1,
    "counter_until" : 2
    }

readFileBulkConfig ={
    "input_file_name" : "input.txt"
    }
#	 C:\Python26\python.exe .\counterBulk.py
xmlRequest={"xml" : """<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:sip="sippbx.ws.nortelnetworks.com"> 
   <soapenv:Header/> 
   <soapenv:Body> 
      <sip:modifyTrunkGroupProperties soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"> 
         <in0 xsi:type="pool:SipPbxNaturalKeyDO" xmlns:pool="pool.data.ws.nortelnetworks.com"> 
            <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">fozsapbx$node</name> 
         </in0> 
         <in1 xsi:type="sip:TrunkGroupPropertiesNaturalKeyDO"> 
            <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">abcd</name> 
         </in1> 
         <in2 xsi:type="sip:TrunkGroupPropertiesDO"> 
            <defaultPublicNumber xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></defaultPublicNumber> 
            <homeCountry xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></homeCountry> 
            <homeLanguage xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></homeLanguage> 
            <locale xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></locale> 
            <maxOrigSessions xsi:type="soapenc:int" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></maxOrigSessions> 
            <maxTermSessions xsi:type="soapenc:int" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></maxTermSessions> 
            <maxTgrpSessions xsi:type="soapenc:int" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></maxTgrpSessions> 
            <nodeType xsi:type="pool:SvcNodeTypeNaturalKeyDO" xmlns:pool="pool.data.ws.nortelnetworks.com"> 
               <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">A2PC</name> 
            </nodeType> 
            <overrideFromHeader xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></overrideFromHeader> 
            <tgrpTrustPai xsi:type="xsd:boolean">false</tgrpTrustPai> 
            <trunkGroup xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">abcd</trunkGroup> 
         </in2> 
      </sip:modifyTrunkGroupProperties> 
   </soapenv:Body> 
</soapenv:Envelope>"""}
