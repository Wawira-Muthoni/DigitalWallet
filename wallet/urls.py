from django.urls import path
from .view import register_Account, register_Receipt, register_Transaction, register_customer,register_Account,register_wallet,register_Card,register_ThirdParty,register_Loan,register_Reward

urlpatterns = [
    path("register/",register_customer,name="customer"),]
urlpatterns = [
    path("register/",register_wallet,name="wallet"),]
urlpatterns = [
    path("register/",register_Receipt,name="receipt"),]    
urlpatterns = [
    path("register/",register_Account,name="account"),]     

urlpatterns = [
    path("register/",register_Transaction,name="transaction"),] 
urlpatterns = [
    path("register/",register_Card,name="card"),]     
urlpatterns = [
    path("register/",register_ThirdParty,name="thirdparty"),]         
urlpatterns = [
    path("register/",register_Loan,name="loan"),]
urlpatterns = [
    path("register/",register_Reward,name="reward"),]                   