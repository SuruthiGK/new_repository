import json
import datetime
import commands

finalOutput=[]
start_date = '<start_date>'
start_date = long(start_date) / 1000.0
start_date = datetime.datetime.fromtimestamp(start_date).strftime('%Y-%m-%d %H:%M:%S')
end_date = '<end_date>'
end_date = long(end_date) / 1000.0
end_date = datetime.datetime.fromtimestamp(end_date).strftime('%Y-%m-%d %H:%M:%S')
import appviewx
reload(appviewx)
connect_db = appviewx.db_connection()
db = connect_db.appviewx
settings_db = connect_db.appviewx.appSettings.find_one({"properties.TICKETING_VENDOR":"serviceNow"})
snow_url = settings_db['properties']['TICKETING_VENDOR_URL']

RequesterName = '<appviewx_username>'
description = 'Created by AppViewX'
short_description = 'VIP Deletion'
device='<device_list>'
device_ip = db.device.find_one({"name":device})
ip=device_ip['ip']
commands_to_push='<commands_to_push>'
commands_split = commands_to_push.split('\n')
command_push = ','.join(commands_split)
vs_name='<disabled_vip>'
snow_user = '<snow_user>'
snow_pw = '<snow_pw>'
if __name__ == '__main__':
	
	curlCommand='''curl  --silent  '''+snow_url+'''/api/now/table/change_request \
						--request POST \
						--header "Accept:application/json"\
						--header "Content-Type:application/json" \
						--data "{'end_date':\'''' +str(end_date)+ '''\','start_date':\'''' +str(start_date)+ '''\','state':'2',\
						'requested_by':\'''' + RequesterName + '''\',
						'description':\'''' + command_push + '''\',
						'approval':'requested','category':'Hardware',\'cmdb_ci':\'''' + device + '''\',
						'short_description':\'''' + short_description + '''\','priority':'2','risk':'4',
\'change_plan':\'''' + ip + '''\',\'backout_plan':\'''' + command_push+ '''\','type':'Comprehensive',
\'review_comments':\'''' + vs_name + '''\'}" \
						--user "'''+snow_user+'''":"'''+snow_pw+'''"'''
	status, cmdOutput = commands.getstatusoutput(str(curlCommand))
	outputJson=json.loads(str(cmdOutput))
	change_number = str(outputJson['result']["number"])
	finalOutput.append({'change_id': str(change_number)}) 
	print json.dumps(finalOutput)

	
	
	
