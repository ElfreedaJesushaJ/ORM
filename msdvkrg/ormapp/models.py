from django.db import models
from django.contrib import admin
class Loan(models.Model):
  acno=models.IntegerField(primary_key="acno")
  name=models.CharField(max_length=25)
  collateral=models.Charfield(max_length=3)
  occupation=models.CharField(max_length=20)
  loanid=models.IntegerField()

class LoanAdmin(admin.ModelAdmin)
 list_display=('acno','name','collateral','occupation','loanid')
  
  
  
