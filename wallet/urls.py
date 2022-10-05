from django.urls import path
from .view import edit_customer,customer_profile,list_currencys ,list_rewards,list_rewards, list_thirdpartys, list_transactions,list_receipts,list_accounts, list_customers, register_Account,list_notifications, register_Currency, register_Receipt, register_Transaction, register_customer,register_Account,register_wallet,register_Card,register_ThirdParty,register_Loan,register_Reward,register_Notification

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
    path("currency/",register_Currency, name="registration_twelve"),
    
    path("list/",list_customers,name="list_customers"),
    path("list/",list_accounts,name="list_account"),
    path("list/", list_receipts,name="list_receipts"),
    path("list/",list_transactions,name = "list_transactions"),
    path("list/",list_rewards,name="list_rewards"),
    path("list/",list_thirdpartys,name="list_thirdpartys"),
    path("list/",list_notifications,name="list_notifications"),
    path("list/",list_currencys,name="list_currencys")
    ]
    # path("list/",list_wallets,name="list_wallets")


    # path("customers/<int:id>/",customer_profile, name="customer_profile"),

    # path("customers/edit/<int:id>/",edit_customer,name ="edit_customer")
     



        