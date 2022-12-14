
from datetime import datetime
from email import message
from inspect import signature
from locale import currency
# from tkinter import CASCADE
from django.db import models

# Create your models here.

class Customer (models.Model):
        first_name = models.CharField(max_length = 40)
        last_name = models.CharField(max_length = 40) 
        gender = models.CharField(max_length = 20)
        age = models.PositiveSmallIntegerField ()
        nationality = models.CharField(max_length = 20)
        user_id = models.CharField(max_length = 15)
        email = models.EmailField(
                null = True
        )
        nationality= models.CharField(
                max_length= 15,
                null= True
        )
        occupation=models.BooleanField()


class Currency(models.Model):
        symbol = models.CharField(
                max_length= 20,
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
        account_name = models.CharField(max_length=40)
        deposit = models.PositiveIntegerField(default=0)
        withdrawals = models.PositiveIntegerField(default=0)
        balance = models.PositiveIntegerField(default=0)
        
class Transaction(models.Model): 
        transaction_code =models.CharField(max_length = 30)
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
        card_number = models.CharField(max_length = 20)
        expiry_date = models.DateTimeField()
        card_type = models.CharField(max_length = 20)
        date_issued = models.DateTimeField()
        issuer =models.CharField(max_length = 20)
        security_code = models.SmallIntegerField(null=True)
        signature = models.ImageField()

class ThirdParty(models.Model):
        full_name = models.CharField(max_length=20,
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
        location = models.CharField(max_length=15)
        isActive = models.BooleanField(max_length=15)
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
        loan_type= models.CharField(max_length = 30)
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
