from django.shortcuts import render

# Create your views here.

from .form import CustomerRegistrationForm,ReceiptRegistrationForm,AccountRegistrationForm,ThirdPartyRegistrationForm,LoanRegistrationForm,WalletRegistrationForm,TransactionRegistrationForm,CardRegistrationForm,NotificationRegistrationForm,RewardRegistrationForm

def register_customer(request):
    form= CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})


def register_wallet(request):
    form= WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form":form})

def register_Receipt(request):
    form= ReceiptRegistrationForm()
    return render(request,"wallet/register_Receipt.html",{"form":form})

def register_Account(request):
    form= AccountRegistrationForm()
    return render(request,"wallet/register_Account.html",{"form":form}) 

def register_Transaction(request):
    form= TransactionRegistrationForm()
    return render(request,"wallet/register_Transaction.html",{"form":form})  

def register_Card(request):
    form= CardRegistrationForm()
    return render(request,"wallet/register_Card.html",{"form":form}) 

def register_ThirdParty(request):
    form= ThirdPartyRegistrationForm()
    return render(request,"wallet/register_ThirdParty.html",{"form":form}) 

def register_Card(request):
    form= NotificationRegistrationForm()
    return render(request,"wallet/register_Notification.html",{"form":form}) 

def register_Loan(request):
    form= LoanRegistrationForm()
    return render(request,"wallet/register_Loan.html",{"form":form}) 

def register_Reward(request):
    form= RewardRegistrationForm()
    return render(request,"wallet/register_Reward.html",{"form":form})                                         