from django.contrib import admin
# from jmespath import search
from .models import Account, Currency, Customer, Notification, Receipt, Reward, Third_Party,Wallet,Transaction,Card,Loan,Reward

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name",)
    search_field = ("first_name","last_name")
admin.site.register(Customer,CustomerAdmin) 

# class WalletAdmin(admin.ModelAdmin):
#     list_display =("balance","amount","pin","currency","date_created","isActive")
admin.site.register(Wallet)
admin.site.register(Currency)
admin.site.register(Account)
admin.site.register(Transaction)
admin.site.register(Card)
admin.site.register(Third_Party)
admin.site.register(Notification)
admin.site.register(Receipt)
admin.site.register(Loan)
admin.site.register(Reward)

# admin.site.register(Account)
# admin.site.register(Transaction)
