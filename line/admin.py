from django.contrib import admin

# Register your models here.
from .models import Account,LineAccount

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account', 'name')

admin.site.register(Account, AccountAdmin)       #註冊至Administration(管理員後台)
admin.site.register(LineAccount)                    #註冊至Administration(管理員後台)
