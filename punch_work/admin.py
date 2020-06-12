from django.contrib import admin

# Register your models here.
from .models import Workpunch

class AccountAdmin(admin.ModelAdmin):
    list_display = ('name','userid','status','time','lon','lat','ip','loc','city')

admin.site.register(Workpunch)       #註冊至Administration(管理員後台)
