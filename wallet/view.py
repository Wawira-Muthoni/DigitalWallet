from django.shortcuts import render
from django .shortcuts import redirect
from wallet.models import Account, Currency,Customer,Card, Notification,Receipt, Reward, ThirdParty,Transaction, Wallet,Loan

# Create your views here.

from .form import CustomerRegistrationForm,ReceiptRegistrationForm,AccountRegistrationForm,ThirdPartyRegistrationForm,LoanRegistrationForm,WalletRegistrationForm,TransactionRegistrationForm,CardRegistrationForm,NotificationRegistrationForm,RewardRegistrationForm,CurrencyRegistrationForm


def register_customer(request):
    if request.method == "POST":
       form = CustomerRegistrationForm(request.POST)
       if form .is_valid():
        form.save()

    else:
        form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})


def register_Receipt(request):
    if request.method == "POST":
       form = ReceiptRegistrationForm(request.POST)
       if form .is_valid():
        form.save()

    else:
        form = ReceiptRegistrationForm()
    return render(request,"wallet/register_Receipt.html",{"form":form})

def register_Account(request):
    if request.method == "POST":
       form = AccountRegistrationForm(request.POST)
       if form .is_valid():
        form.save()

    else:
        form = AccountRegistrationForm()
    return render(request,"wallet/register_Account.html",{"form":form}) 

def register_Card(request):
    if request.method == "POST":
       form = CardRegistrationForm(request.POST)
       if form .is_valid():
        form.save()

    else:
        form = CardRegistrationForm()
    return render(request,"wallet/register_Card.html",{"form":form})     

def register_Transaction(request):
    if request.method == "POST":
       form = TransactionRegistrationForm(request.POST)
       if form .is_valid():
        form.save()

    else:
        form = TransactionRegistrationForm()
    return render(request,"wallet/register_Transaction.html",{"form":form})

def register_wallet(request):
    if request.method == "POST":
       form = WalletRegistrationForm(request.POST)
       if form .is_valid():
        form.save()

    else:
        form = WalletRegistrationForm()
    return render(request,"wallet/register_wallet.html",{"form":form})     

def register_Notification(request):
    if request.method == "POST":
       form = NotificationRegistrationForm(request.POST)
       if form .is_valid():
        form.save()

    else:
        form = NotificationRegistrationForm()
    return render(request,"wallet/register_Notification.html",{"form":form})



def register_ThirdParty(request):
    if request.method == "POST":
       form = ThirdPartyRegistrationForm(request.POST)
       if form .is_valid():
        form.save()

    else:
        form = ThirdPartyRegistrationForm()
    return render(request,"wallet/register_ThirdParty.html",{"form":form})


def register_Loan(request):
    if request.method == "POST":
       form = LoanRegistrationForm(request.POST)
       if form .is_valid():
        form.save()

    else:
        form = LoanRegistrationForm()
    return render(request,"wallet/register_Loan.html",{"form":form})    


def register_Reward(request):
    if request.method == "POST":
       form = RewardRegistrationForm(request.POST)
       if form .is_valid():
        form.save()

    else:
        form = RewardRegistrationForm()
    return render(request,"wallet/register_Reward.html",{"form":form})    



def register_Currency(request):
    if request.method == "POST":
       form = CurrencyRegistrationForm(request.POST)
       if form .is_valid():
        form.save()

    else:
        form = CurrencyRegistrationForm()
    return render(request,"wallet/register_Currency.html",{"form":form})    


    






# listing data

def list_customers(request):
    customers = Customer.objects.all()    
    return render(request,"wallet/customers_list.html",{"customer":customers})   

def list_accounts(request):
    accounts = Account.objects.all()    
    return render(request,"wallet/account_list.html",{"account":accounts})  

def list_cards(request):
    cards= Card.objects.all()    
    return render(request,"wallet/cards_list.html",{"cards":cards})   


def list_wallets(request):
    wallets= Wallet.objects.all()    
    return render(request,"wallet/wallets_list.html",{"wallets":wallets})     


def list_receipts(request):
    receipts= Receipt.objects.all()    
    return render(request,"wallet/receipts_list.html",{"receipts":receipts})    

def list_transactions(request):
    transactions= Transaction.objects.all()    
    return render(request,"wallet/transactions_list.html",{"transactions":transactions}) 


def list_rewards(request):
    rewards= Reward.objects.all()    
    return render(request,"wallet/rewards_list.html",{"rewards":rewards})


def list_thirdpartys(request):
    thirdpartys= ThirdParty.objects.all()    
    return render(request,"wallet/thirdpartys_list.html",{"thirdpartys":thirdpartys})           

def list_loans(request):
    loans= Loan.objects.all()    
    return render(request,"wallet/loans_list.html",{"loans":loans}) 

def list_notifications(request):
    notifications= Notification.objects.all()    
    return render(request,"wallet/notifications_list.html",{"notifications":notifications})  


def list_currencys(request):
    currencys= Currency.objects.all()    
    return render(request,"wallet/currencys_list.html",{"currencys":currencys})     

# single object view

def customer_profile(request,id):
    customers = Customer.objects.get(id=id)
    return render(request,"wallet/customer_profile.html",{
        "customer":customers
    })

def customer_profile(request,id):
    customers = Customer.objects.get(id=id)
    return render(request,"wallet/customer_profile.html",{
        "customer":customers
    })














    # editing data

def edit_customer(request,id):
    customer = Customer.objects.get(id=id)
    if request.method =="POST":
        form = CustomerRegistrationForm(request .POST, instance=customer)
        if form. is_valid():
            form.save()
            return redirect("customer_profile", id = customer.id)
    else:
        form = CustomerRegistrationForm(instance=customer)
        return render(request,"wallet/edit_customer.html",{"forms":form})
        
