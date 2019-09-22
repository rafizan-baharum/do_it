from django.contrib import admin

# Register your models here.
from account.models import DoerWallet, Withdrawal

admin.site.register(DoerWallet)
admin.site.register(Withdrawal)