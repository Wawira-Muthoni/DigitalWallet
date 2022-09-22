from django.urls import path
from .view import register_Account, register_Currency, register_Receipt, register_Transaction, register_customer,register_Account,register_wallet,register_Card,register_ThirdParty,register_Loan,register_Reward,register_Notification

urlpatterns = [
    path("register/",register_customer,name="registration"),
    path("wallet/",register_wallet,name="registratin_two"),
    path("receipt/",register_Receipt,name="registration-three"),  
    path("account/",register_Account,name="registration_four"),     
    path("transaction/",register_Transaction,name="registration_six"),
    path("card/",register_Card,name="registration_seven"),     
    path("thirdparty/",register_ThirdParty,name="registration_eight"),        
    path("loan/",register_Loan,name="registration_nine"),
    path("reward/",register_Reward,name="registration_ten"),
    path("notification/",register_Notification, name="registration_eleven"),
    path("currency/",register_Currency, name="registration_twelve")]                   