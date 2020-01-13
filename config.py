config =  {
    "prov_user_name" : "admin",
    "prov_user_password" : "admin",
    "prov_url"  :"http://47.168.58.197:8080/prov/services/UserAdminService",
    "success_log_file_name" : "success_log.txt",
    "fail_log_file_name" : "fail_log.txt",
    "input_file_name" : "input.txt"
    }

counterBulkConfig ={
    "counter_from" : 1,
    "counter_until" : 1000
    }

readFileBulkConfig ={
    "input_file_name" : "input.txt"
    }

xmlRequest={
    "xml" : """<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:user="user.ws.nortelnetworks.com">
   <soapenv:Header/>
   <soapenv:Body>
      <user:addSingleUserWithServiceSet soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
         <in0 xsi:type="com:DomainNaturalKeyDO" xmlns:com="common.ws.nortelnetworks.com">
            <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">sub1.nl15sip1.com</name>
         </in0>
         <in1 xsi:type="core:ServiceSetNaturalKeyDO" xmlns:core="core.data.ws.nortelnetworks.com">
            <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">basit_paket</name>
         </in1>
         <in2 xsi:type="user:UserSecurityDO">
            <password xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">u1234</password>
         </in2>
         <in3 xsi:type="user:UserDO">
            <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">userbulk$</name>
            <cellPhone xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">00000</cellPhone>
            <email xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">userbulk@userbulk</email>
            <fax xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></fax>
            <firstName xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">userbulk</firstName>
            <homeCountry xsi:type="hom:HomeCountryNaturalKeyDO" xmlns:hom="homelocale.ws.nortelnetworks.com">
               <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></name>
            </homeCountry>
            <homeLanguage xsi:type="hom:HomeLanguageNaturalKeyDO" xmlns:hom="homelocale.ws.nortelnetworks.com">
               <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></name>
            </homeLanguage>
            <homePhone xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></homePhone>
            <lastName xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></lastName>
            <locale xsi:type="com:LocaleNaturalKeyDO" xmlns:com="common.ws.nortelnetworks.com">
               <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></name>
            </locale>
            <officePhone xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></officePhone>
            <pager xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></pager>
            <picture xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></picture>
            <status xsi:type="core:StatusNaturalKeyDO" xmlns:core="core.data.ws.nortelnetworks.com">
               <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">ACTIVE</name>
            </status>
            <statusReason xsi:type="core:StatusReasonNKDO" xmlns:core="core.data.ws.nortelnetworks.com">
               <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></name>
            </statusReason>
            <subDomainName xsi:type="com:DomainNaturalKeyDO" xmlns:com="common.ws.nortelnetworks.com">
               <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></name>
            </subDomainName>
            <timezone xsi:type="com:TimeZoneNaturalKeyDO" xmlns:com="common.ws.nortelnetworks.com">
               <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">Eastern Standard Time</name>
            </timezone>
            <type xsi:type="core:UserTypeNaturalKeyDO" xmlns:core="core.data.ws.nortelnetworks.com">
               <name xsi:type="soapenc:string" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"></name>
            </type>
         </in3>
      </user:addSingleUserWithServiceSet>
   </soapenv:Body>
</soapenv:Envelope>"""
    }
