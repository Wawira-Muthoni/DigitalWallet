
from datetime import datetime
from email import message
from inspect import signature
from locale import currency
# from tkinter import CASCADE
from django.db import models

# Create your models here.

class Customer (models.Model):
        first_name = models.CharField(max_length = 7)
        last_name = models.CharField(max_length = 7) 
        gender = models.CharField(max_length = 6)
        age = models.PositiveSmallIntegerField ()
        nationality = models.CharField(max_length = 10)
        user_id = models.CharField(max_length = 7)
        nationality= models.CharField(
                max_length= 12,
                null= True
        )
        occupation=models.BooleanField()


class Currency(models.Model):
        symbol = models.CharField(
                max_length= 5,
                null = True
        )
        nationality = models.CharField(max_length=12,
                null=True)
       

class Wallet(models.Model):
        balance = models.PositiveIntegerField(default=0)
        pin = models.SmallIntegerField(default=0)
        currency = models.ForeignKey(
                Currency,
         on_delete= models.CASCADE,
         null= True
               
        )                
class Receipt(models.Model):
        receipt_date = models.DateTimeField()
        bill_number = models.PositiveIntegerField(default=0)
        receipt_file = models.FileField()
        total_amount = models.IntegerField(default=0) 

class Account(models.Model):
        account_number = models.TextField()
        account_name = models.CharField(max_length=10)
        deposit = models.PositiveIntegerField(default=0)
        withdrawals = models.PositiveIntegerField(default=0)
        balance = models.PositiveIntegerField(default=0)
        
class Transaction(models.Model): 
        transaction_code =models.CharField(max_length = 15)
        transaction_number = models.PositiveIntegerField(default=0)
        transaction_amount = models.PositiveIntegerField(default=0)
        transaction_type = models.CharField(max_length=10)
        datetime = models.DateTimeField(
                null=True)
        transaction_charge = models.PositiveIntegerField(default=0) 
        wallet = models.ForeignKey(
                Wallet,
                on_delete=models.CASCADE,
                null= True) 
        account = models.ForeignKey(
                Account,
                on_delete= models.CASCADE,
                null= True
        )
        receipt = models.ForeignKey(
                Receipt,
                on_delete=models.CASCADE,
                null = True
        )
        destination_account = models.ForeignKey(
                   'Account',
                   on_delete=models.CASCADE,
                    related_name='Transaction_destination_account', default= None
            )

class Card(models.Model):
        card_number = models.CharField(max_length = 8)
        expiry_date = models.DateTimeField()
        card_type = models.CharField(max_length = 6)
        date_issued = models.DateTimeField()
        issuer =models.CharField(max_length = 6)
        security_code = models.SmallIntegerField(null=True)
        signature = models.ImageField()

class ThirdParty(models.Model):
        full_name = models.CharField(max_length=12,
              null = True)
        user_id = models.PositiveSmallIntegerField(
                null = True
        )
        transaction_cost =models.IntegerField(
                null = True
        )
        email = models.EmailField(
                null = True
        )
        location = models.CharField(max_length=10)
        isActive = models.BooleanField(max_length=3)
        currency = models.ForeignKey(
                Currency,
                on_delete= models.CASCADE,
                null=True
               
        )
        account = models.ForeignKey(
                Account,
                on_delete= models.CASCADE,
                null= True
        )

class Notification(models.Model):
        full_name = models.CharField(max_length= 20,
        null = True)
        time = models.DateTimeField(
                null = True
        )
        message = models.TextField()
        date_created = models.DateTimeField()
        customer = models.ForeignKey(
                'Customer',
                on_delete=models.CASCADE
                )
        status = models.CharField(max_length=12)

class Loan(models.Model):
        loan_id = models.IntegerField(default=0)
        loan_type= models.CharField(max_length = 10)
        balance = models.IntegerField()
        payment_due_date = models.DateTimeField()
        customer = models.ForeignKey(
                Customer,
                on_delete=models.CASCADE,
                null=True

        )
        loan_terms = models   
        status = models.BooleanField()
        datetime = models.DateTimeField()

class Reward(models.Model):
        date  = models.DateTimeField()
        bonus = models.IntegerField()
        transaction = models.ForeignKey(
                'Transaction',
                on_delete=models.CASCADE,
                null = True)
        wallet = models.ForeignKey(
                'Wallet',
                on_delete=models.CASCADE,
                null= True)       

# from locale import currency
# from symtable import Symbol
# from django.db import models
# from django.utils import timezone
# class Customer(models.Model):
#     firstname=models.CharField(max_length=15,null=True)
#     lastname=models.CharField(max_length=15,null=True)
#     GENDER_CHOICE=(("M","Male"),("F","Female"))
#     gender=models.CharField(max_length=1,choices=GENDER_CHOICE,null=True)
#     address=models.CharField(max_length=15,null=True)
#     age=models.PositiveSmallIntegerField()
#     nationality=models.CharField(max_length=15,null=True)
#     id_number=models.CharField(max_length=15,null=True)
#     phone_number=models.CharField(max_length=15,null=True)
#     email=models.EmailField(max_length=30,null=True)
#     pin=models.TextField(max_length=8,null=True)
# class Currency(models.Model):
#     amount=models.IntegerField()
#     symbol=models.CharField(max_length=15,null=True)
#     country_of_origin=models.CharField(max_length=24,null=True)
# class Wallet(models.Model):
#     currency=models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='Wallet_currency')
#     customer=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Wallet_customer')
#     balance=models.IntegerField()
#     amount=models.IntegerField()
#     date=models.DateTimeField(default=timezone.now)
#     status=models.CharField(max_length=15,null=True)
#     pin=models.TextField(max_length=8,null=True)
# class Account(models.Model):
#     account_type=models.CharField(max_length=15,null=True)
#     balance=models.IntegerField()
#     account_name=models.CharField(max_length=20,null=True)
#     wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Account_wallet')
# class Transaction(models.Model):
#     wallet=models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Transaction_wallet')
#     transaction_amount=models.IntegerField()
#     transaction_type=models.CharField(max_length=15,null=True)
#     transaction_charge=models.IntegerField()
#     transaction_date=models.DateTimeField(default=timezone.now)
#     receipt=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Transaction_receipt')
#     origin_account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Transaction_receipt')
#     destination_account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Transaction_destination_account')
# class Card(models.Model):
#     date_issued=models.DateTimeField(default=timezone.now)
#     card_name=models.CharField(max_length=15,null=True)
#     card_number=models.IntegerField()
#     card_type=models.CharField(max_length=15,null=True)
#     exipry_date=models.DateTimeField(default=timezone.now)
#     card_status=models.CharField(max_length=15,null=True)
#     security_code=models.IntegerField()
#     wallet=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Card_wallet')
#     account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Card_account')
#     issuer=models.CharField(max_length=15,null=True)
# class Thirdparty(models.Model):
#     account=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Thirdparty_account')
#     name=models.CharField(max_length=15,null=True)
#     thirdparty_id=models.IntegerField()
#     phone_number=models.IntegerField()
# class Notification(models.Model):
#     notifications_id=models.IntegerField()
#     name=models.CharField(max_length=15,null=True)
#     status=models.CharField(max_length=15,null=True)
#     date_and_time=models.DateTimeField(default=timezone.now)
#     receipt=models.ForeignKey('Thirdparty',on_delete=models.CASCADE,related_name='Notifications_receipt')
# class Receipt(models.Model):
#     receipt_type=models.CharField(max_length=15,null=True)
#     receipt_date=models.DateField(default=timezone.now)
#     receipt_file=models.FileField()
#     total_amount=models.IntegerField()
#     transaction=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Receipt_transaction')
# class Loan(models.Model):
#     loan_number=models.IntegerField()
#     loan_type=models.CharField(max_length=15,null=True)
#     amount=models.IntegerField()
#     date_and_time=models.DateTimeField(default=timezone.now)
#     wallets=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Loan_wallet')
#     interest_rate=models.IntegerField()
#     guarantor=models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Loan_guarantor')
#     pay_due_date=models.DateTimeField(default=timezone.now)
#     loan_balance=models.IntegerField()
    
# class Reward(models.Model):
#     transaction=models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Reward_transaction')
#     date_and_time=models.DateTimeField(default=timezone.now)
#     customer_id=models.IntegerField()
#     GENDER_CHOICES=(("M","Male"),("F","Female"))
#     gender=models.CharField(max_length=1,choices=GENDER_CHOICES,null=True)
#     bonus=models.IntegerField()









