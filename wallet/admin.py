
from django.contrib import admin
# from jmespath import search
from .models import Account, Currency, Customer, Notification, Receipt, Reward, Third_Party,Wallet,Transaction,Card,Loan,Reward

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name")
    search_field = ("first_name","last_name")
admin.site.register(Customer,CustomerAdmin) 

class WalletAdmin(admin.ModelAdmin):
     list_display =("balance","pin","currency")
     search_field = ("balance","pin","currency")    
admin.site.register(Wallet,WalletAdmin)

class CurrencyAdmin(admin.ModelAdmin):
     list_display=("symbol","nationality")
     search_field = ("symbol","nationality")
admin.site.register(Currency,CurrencyAdmin)

class AccountAdmin(admin.ModelAdmin):
     list_display =("account_number","account_name","deposit","withdrawals","balance")
     search_field = ("account_number","account_name","deposit","withdrawals","balance")
admin.site.register(Account,AccountAdmin)  

class TransactionAdmin(admin.ModelAdmin):
     list_display= ("transaction_code","transaction_amount","transaction_type","datetime")
     search_field = ("transaction_code","transaction_amount","transaction_type","datetime")
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
     list_display = ("card_number","signature","expiry_date","date_issued","issuer","security_code")
     search_field = ("card_number","signature","expiry_date","date_issued","issuer","security_code")
admin.site.register(Card,CardAdmin)

class Third_PartyAdmin(admin.ModelAdmin):
     list_display=("full_name","email","user_id","location","isActive","currency","account")
     search_field = ("full_name","email","user_id","location","isActive","currency","account")
admin.site.register(Third_Party,Third_PartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
     list_display = ("full_name","time","message","date_created","customer","status")
     search_field = ("full_name","time","message","date_created","customer","status")
admin.site.register(Notification,NotificationAdmin)

class ReceiptAdmin(admin.ModelAdmin):
      list_display = ("receipt_date","bill_number","receipt_file","total_amount")
      search_field= ("receipt_date","bill_number","receipt_file","total_amount")
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
      list_display = ("loan_type","balance","loan_terms","status","datetime","payment_due_date")
      search_field = ("loan_type","balance","loan_terms","status","datetime","payment_due_date")
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
     list_display = ("date","bonus","transaction","wallet")
     searc_field = ("date","bonus","transaction","wallet")
admin.site.register(Reward,RewardAdmin)


