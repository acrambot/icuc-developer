from django.db import models

# Create your models here.

#create Department table
class Department(models.Model):
  departmentId =models.IntegerField()
  departmentname =models.CharField(max_length=200)
  salaryscale =models.IntegerField()

  #creating Employee table
class Employee(models.Model):
  employeeId = models.IntegerField()
  firstname = models.CharField(max_length=200)
  others =models.CharField(max_length=200,null=True)
  gender = models.CharField(max_length=10,choices=[("M","Male"),("F","Female")])
  DOB = models.DateField(auto_now=False,auto_now_add=False)
  email = models.EmailField()
  address = models.CharField(max_length=100)
  contact = models.CharField(max_length=100)
  position = models.CharField(max_length=100)
  maritalstatus = models.CharField(max_length=100,choices=[("S","Single"),("M","Married")])
  departmentname =models.ForeignKey(Department,on_delete=models.CASCADE)
  religion =models.CharField(max_length=100)
  salary =models.IntegerField()

  #create Customers table
class Customer(models.Model):
  customerId =models.IntegerField()
  firstname =models.CharField(max_length=100)
  lastname =models.CharField(max_length=100)
  others =models.CharField(max_length=100,null=True)
  contact =models.CharField(max_length=50)
  gender =models.CharField(max_length=100,choices=[("M","Male"),("F","Female")])
  email =models.EmailField()

  #create Salesorders table
class Salesorder(models.Model):
  orderId =models.IntegerField()
  customerId =models.ForeignKey(Customer,on_delete=models.CASCADE)
  employeeId =models.ForeignKey(Employee,on_delete=models.CASCADE)
  orderdate =models.DateField(auto_now=False,auto_now_add=False)
  totalamount =models.IntegerField()

  #create CustomerSupportTickets table
class CustomerSupportTicket(models.Model):
  ticketId =models.IntegerField()
  customerId =models.ForeignKey(Customer,on_delete=models.CASCADE)
  employeeId =models.ForeignKey(Employee,on_delete=models.CASCADE)
  customerIssueDescription =models.CharField(max_length=500)
  status =models.CharField(max_length=100,choices=[("O","Open"),("C","Closed"),("I","In-progress")])


  #create Products table
class Product(models.Model):
  productId =models.IntegerField()
  productname =models.CharField(max_length=100)
  stockquantity =models.IntegerField()
  unitprice =models.IntegerField()

  

  #create Financialtransactions table
class Financialtransaction(models.Model):
  transactionId =models.IntegerField()
  date =models.DateField(auto_now=False,auto_now_add=False)
  amount =models.IntegerField()
  description =models.CharField(max_length=200)

  
                        



