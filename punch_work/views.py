# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def punch_in(request):
#     print('aaaa')
#     return render(request,"punch_in.html") #將index.html頁面拋給使用者

from django.views.generic import TemplateView
from django.shortcuts import render
# from django.views.decorators import csrf
from django.http import HttpResponse,JsonResponse
from .models import Workpunch,LineAccount
from django.utils import timezone
import json

class punch_in(TemplateView):  
    template_name = 'punch_in.html'


# 接收POST请求数据
def postLocation(request):
    if request.method == 'POST':
        jsonData = json.loads(request.body.decode("utf-8"))
        liffID = jsonData['liffID']
        liffName = jsonData['liffname']
        liffPic = jsonData['liffPic']
        liffOs = jsonData['liffOs']
        userstatus = jsonData['status']
        username = {i[0]:i[1] for i in LineAccount.objects.values_list('LineID','name')}[liffID]
        Account = {i[0]:i[1] for i in LineAccount.objects.values_list('LineID','account')}[liffID]
        if ('lon' not in jsonData.keys()) or ('lat' not in jsonData.keys()):
            returnVal = {'str':username + "打卡失敗，請開啟手機的定位功能"}
            print(returnVal)
            return JsonResponse(returnVal)
        lon = jsonData['lon']
        lat = jsonData['lat']

        userInfo = ana_userInfo(jsonData['info'])
        userIP = userInfo['ip']
        userUag = userInfo['uag']  # 使用者使用的系統及瀏覽器
        userLoc = userInfo['loc']
        userCity = userInfo['colo']

        data = Workpunch()
        data.userid = Account
        data.name = username
        data.time = timezone.now()
        data.status = userstatus  # 1:上班 2:私事上班 3:私事下班 ＃4:下班    #-99:非使用手機 
        data.lon = lon
        data.lat = lat
        data.ip = userIP
        data.system = userUag
        data.loc = userLoc
        data.city = userCity

        check = ana_userUag(data.system)
        if data.status == '1':
            flag = '上班'
        elif data.status == '2':
            flag = '私事回來'
        elif data.status == '3':
            flag = '私事離開'
        elif data.status == '4':
            flag = '下班'
        else:
            flag = 'ERROR'
        if check:
        # returnVal = {"name":data.name,"time":data.time,"ip":data.ip,"tag":flag+"打卡成功"}
            returnVal = {'str':data.name + '\n' + str(data.time) + '\n' + data.ip + '\n' + flag + "打卡成功"}
        else:
        # returnVal = {"name":data.name,"time":data.time,"ip":data.ip,"tag":"請使用手機重新打卡"}
            returnVal = {'str':data.name + '\n' + str(data.time) + '\n' + data.ip + '\n' + "請使用手機重新打卡"}
            data.status = -99
        
        data.save()

    return JsonResponse(returnVal)
    # return HttpResponse(returnVal)
    # return render(request,'punch_in.html',{'aaaa':'0'})

def getUserName(request):
    if request.method == 'GET':
        userID = request.GET.get("data")
        LineIDDict = {i[0]:i[1] for i in LineAccount.objects.values_list('LineID','name')}
        return HttpResponse(LineIDDict[userID])

def ana_userInfo(data):
    data = {i.split('=')[0]:i.split('=')[1] for i in data.split('\n') if len(i)!=0}
    return data

def ana_userUag(data):
    # keyWords = ['Mac OS', 'Windows']
    tag = True
    if 'Mac OS' in data:
        if 'iPhone' not in data: tag = False
    elif 'Windows' in data:
        tag = False
    return tag
