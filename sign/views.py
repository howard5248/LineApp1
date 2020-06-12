from django.shortcuts import render
from django.http import HttpResponse
from .models import Account,Employee

# Create your views here.
def index(request):
    Accounts = Account.objects.all()
    # print(Accounts)
    # return HttpResponse("My First Django App.")
    #return render(request,"index.html") #將index.html頁面拋給使用者
    
    return render(request, "index.html", {"Accounts": Accounts})

    if request.is_ajax():
        #do something
        request_data = request.POST
        print(request_data)
        return HttpResponse("OK")


