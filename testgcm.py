from gcm import GCM
gcm = GCM('AIzaSyAJ882Hvz_hEacehne7TOIYn-uUvT0LI9s')
reg_id = 'APA91bG9CDDMm7njzdvmoKpLaQI_Y9_UnCf6E1nmh28YrVz6-xSD4wOOHBgM7SUrjp-Rundmanm9j4Ke9oz0LvQGhrH4OS1cK0QhNDtSJK4VRUt9o6Tcm3qKd3miP8NKbzFqH8E_aqtefzve8W-Zs7rElg5vay2vEx29tRAMChOmAWvBBncmOew'

data = {'message': 'hello world'}
gcm.plaintext_request(registration_id=reg_id, data=data)
