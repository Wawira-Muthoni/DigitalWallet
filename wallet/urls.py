from django.urls import path
from .view import register_Account, register_Receipt, register_Transaction, register_customer,register_Account
from .view import register_wallet,register_Card,register_ThirdParty,register_Loan,register_Reward

urlpatterns = [
    path("register/",register_customer,name="registration"),]
urlpatterns = [
    path("register/",register_wallet,name="registration"),]
urlpatterns = [
    path("register/",register_Receipt,name="registration"),]    
urlpatterns = [
    path("register/",register_Account,name="registration"),]     

urlpatterns = [
    path("register/",register_Transaction,name="registration"),] 
urlpatterns = [
    path("register/",register_Card,name="registration"),]     
urlpatterns = [
    path("register/",register_ThirdParty,name="registration"),]         
urlpatterns = [
    path("register/",register_Loan,name="registration"),]
urlpatterns = [
    path("register/",register_Reward,name="registration"),]                   