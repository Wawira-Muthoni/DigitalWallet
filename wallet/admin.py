
from django.contrib import admin
# from jmespath import search
from .models import Account, Currency, Customer, Notification, Receipt, Reward, ThirdParty,Wallet,Transaction,Card,Loan,Reward

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

class ThirdPartyAdmin(admin.ModelAdmin):
     list_display=("full_name","email","user_id","location","isActive","currency","account")
     search_field = ("full_name","email","user_id","location","isActive","currency","account")
admin.site.register(ThirdParty,ThirdPartyAdmin)

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

# from django.contrib import admin
# from.models import Account, Customer,Currency, Notification, Receipt, Reward, Transaction, Wallet,Card,ThirdParty,Loan
# class CustomerAdmin(admin.ModelAdmin):
#     list_display=("firstname","lastname","email","gender","address")
#     search_fields=("fistname","lastname","gender","address","email")
# admin.site.register(Customer,CustomerAdmin)
# class CurrencyAdmin(admin.ModelAdmin):
#     list_display=("amount","symbol","country_of_origin")
#     search_fields=("amount","country_of_origin")
# admin.site.register(Currency,CurrencyAdmin)
# class WalletAdmin(admin.ModelAdmin):
#     list_display=('pin','status','date','amount','customer','balance')
#     search_fields=('status','date','amount','balance')
# admin.site.register(Wallet,WalletAdmin)
# class AccountAdmin(admin.ModelAdmin):
#     list_display=('account_name','account_type','balance','wallet')
#     search_fields=('account_name','balance','wallet')
# admin.site.register(Account,AccountAdmin)
# class TransactionAdmin(admin.ModelAdmin):
#     list_display=('wallet','transaction_amount','transaction_type','transaction_charge')
#     search_fields=('wallet','transaction_amount','transaction_charge')
# admin.site.register(Transaction,TransactionAdmin)
# class CardAdmin(admin.ModelAdmin):
#     list_display=('date_issued','card_name','card_type')
#     search_fields=(" issuer",'card_name')
# admin.site.register(Card,CardAdmin)
# class ThirdpartyAdmin(admin.ModelAdmin):
#     list_display=('account','name','thirdparty_id','phone_number',)
#     search_fields=("account",'name')
# admin.site.register(ThirdParty,ThirdpartyAdmin)
# class NotificationsAdmin(admin.ModelAdmin):
#     list_display=('notifications_id','name','date_and_time')
#     search_fields=("receipt",'notifications_id')
# admin.site.register(Notification,NotificationsAdmin)
# class ReceiptAdmin(admin.ModelAdmin):
#     list_display=('receipt_type','receipt_date','receipt_file','total_amount','transaction',)
#     search_fields=("transaction",'receipt_type')
# admin.site.register(Receipt,ReceiptAdmin)

# class LoanAdmin(admin.ModelAdmin):
#     list_display=('loan_number','loan_type','date_and_time','interest_rate')
#     search_fields=("loan_number",'loan_type')
# admin.site.register(Loan,LoanAdmin)
# class RewardAdmin(admin.ModelAdmin):
#     list_display=('transaction','date_and_time','customer_id','gender','bonus',)
#     search_fields=("bonus",'date_and_time')
# admin.site.register(Reward,RewardAdmin)