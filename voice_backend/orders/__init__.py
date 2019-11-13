APP_ID = 'POCTESTENV'
APP_SECRET = 'Du2reeaUzJTclcPqGHNmbrXxORJmBJWJ'
TRANSFER_HEADERS = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Accept-Encoding': '',
    'Accept': 'application/json'
}
TRANSFER_URL = "http://10.242.26.20:8000/api/newCustService/intelligence/voiceConvertWrite/v1"
ORDER_URL = "http://10.242.26.20:8000/api/sendBox/floworder/v1"
VOICE_DATA ={
   "UNI_BSS_HEAD" : {
    "APP_ID": "POCTESTENV",
    "TIMESTAMP": "",
    "TRANS_ID": "20191031085036280576720",
    "TOKEN": "0538e776dfafc53ec5f7a1451c010537",
    "RESERVED": []
  },
  "UNI_BSS_ATTACHED" : {
    "MEDIA_INFO" : ""
  },
  "UNI_BSS_BODY" : {
    "VOICE_CONVERT_WRITE_REQ" : {
		"Header": {
			"Version": "",
			"TestFlag": "0",
			"TaskNo": "1234567890",
			"AreaCode": "",
			"BusinessType": "OfflineVoiceTransfer",
			"BusNo": "13269223021",
			"tokenCode": ""
		},
		"RequestBody": {
			"pid": "10000",
			"format": "pcm",
			"rate": "8000",
			"cuid": "testcuid",
			"audiolen": "154640",
			"b64audio": ""
		}
	
}
  }
}

ORDER_DATA = {
"UNI_BSS_HEAD": {
		"APP_ID": "POCTESTENV", 
		"TIMESTAMP": "", 
		"TRANS_ID": "", 
		"TOKEN": ""
  },
  "UNI_BSS_BODY": {
    "FLOWORDER_REQ": {
      "MSG": {
		"SERIAL_NUMBER" : "13256152122",
        "DISCNT_NAME" : "0元1000G流量包",
        "DISCNT_ID" : "426548254",
        "START_TYPE" : "1",
        "OPER_CODE" : "1",
        "FLOW_TYPE" : "0"

      }
    }
  }
}