import requests

tmp = requests.get('http://h5cloud.17wanxiao.com:8080/CloudPayment/user/getRoom.do?payProId=920&schoolcode=65&optype=2&areaid=1&buildid=0&unitid=0&levelid=0&businesstype=2').json()
print(tmp)
buildingNameId = {}
for i in tmp['roomlist']:
    buildingNameId[i['name']] = i['id']
    #print(i['name']+', ',end='')

buildingName = input("请选择楼宇")
buildingId = buildingNameId[buildingName]

tmp = requests.get(f'http://h5cloud.17wanxiao.com:8080/CloudPayment/user/getRoom.do?payProId=920&schoolcode=65&optype=3&areaid=1&buildid={buildingId}&unitid=0&levelid=0&businesstype=2').json()

floorNameId = {}
for i in tmp['roomlist']:
    floorNameId[i['name']] = i['id']
    
floorName = input("请选择楼层")
floorId = floorNameId[floorName]

tmp = requests.get(f'http://h5cloud.17wanxiao.com:8080/CloudPayment/user/getRoom.do?payProId=920&schoolcode=65&optype=4&areaid=1&buildid={buildingId}&unitid=0&levelid={floorId}&businesstype=2').json()

roomNameId = {}
for i in tmp['roomlist']:
    roomNameId[i['name']] = i['id']

roomName = input("请选择房间号")
roomId = roomNameId[roomName]

tmp = requests.get(f'http://h5cloud.17wanxiao.com:8080/CloudPayment/user/getRoomState.do?payProId=920&schoolcode=65&businesstype=2&roomverify={roomId}').json()

print(f"房间电量为：{tmp['quantity']}度")