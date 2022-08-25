from ast import With
from datetime import datetime
from email import message
from inspect import signature
from locale import currency
from django.db import models

# Create your models here.

class Customer (models.Model):
        first_name = models.CharField(max_length = 15)
        last_name = models.CharField(max_length = 15) 
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
        balance = models.PositiveIntegerField()
        # customer = models.OneToOneRel()
        # amount = models.BigAutoField()
        pin = models.SmallIntegerField()
        currency = models.ForeignKey(
                Currency,
         on_delete= models.CASCADE,
         null= True
                # related_name= 'currency_wallet'
        )                



class Account(models.Model):
        account_number = models.TextField()
        account_name = models.CharField(max_length=10)
        deposit = models.PositiveIntegerField()
        withdrawals = models.PositiveIntegerField()
        balance = models.PositiveIntegerField()
        # transaction=models.PositiveIntegerField(
        #         "Transaction",
        #         on_delete = models.CASCADE,
        #         null = True
        # )

class Transaction(models.Model):
        # symbol= models.PositiveIntegerField(
        #         null=True) 
        transaction_code =models.CharField(max_length = 8)
        transaction_amount = models.PositiveIntegerField()
        # transaction_number = models.BigIntegerField()
        transaction_type = models.CharField(max_length=4)
        datetime = models.DateTimeField(
                null=True
        )
        # receipt = models.OneToOneField()


class Card(models.Model):
        card_number = models.CharField(max_length = 8)
        expiry_date = models.DateTimeField()
        card_type = models.CharField(max_length = 6)
        date_issued = models.DateTimeField()
        issuer =models.CharField(max_length = 6)
        secuity_code = models.SmallIntegerField()
        signature = models.ImageField()


class Third_Party(models.Model):
        first_name = models.CharField(max_length=12,
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
        # transaction_cost = models.BigAutoField()
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

class Receipt(models.Model):
        receipt_date = models.DateTimeField()
        bill_number = models.PositiveIntegerField()
        receipt_file = models.FileField()
        total_amount = models.IntegerField()

class Loan(models.Model):
        loan_type= models.CharField(max_length = 10)
        balance = models.IntegerField()
        payment_due_date = models.DateTimeField()
        customer = models.ForeignKey(
                Customer,
                on_delete=models.CASCADE
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

