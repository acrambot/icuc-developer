from django.contrib import admin

# Register your models here.
from Hibah.models import(Department,Employee,Customer,Product,Salesorder,Financialtransaction,CustomerSupportTicket)

class DepartmentAdmin(admin.ModelAdmin):
    list_display=["departmentId","departmentname","salaryscale"]

class CustomerAdmin(admin.ModelAdmin):
    list_display=["customerId","firstname","lastname","others","contact","gender","email"]

class EmployeeAdmin(admin.ModelAdmin):
    list_display=["employeeId","firstname","others","position","salary","departmentname","contact","gender","DOB","departmentname","email","maritalstatus","religion"]

class ProductAdmin(admin.ModelAdmin):
    list_display=["productId","productname","unitprice","stockquantity"]

class salesorderAdmin(admin.ModelAdmin):
    list_display=["orderId","customerId","employeeId","orderdate","totalamount"]

class FinancialtransactionAdmin(admin.ModelAdmin):
    list_display=["transactionId","date","amount","description"]

class CustomerSupportTicketAdmin(admin.ModelAdmin):
    list_display=["ticketId","customerId","employeeId","customerIssueDescription","status"]

admin.site.register(Department,DepartmentAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Salesorder,salesorderAdmin)
admin.site.register(Financialtransaction,FinancialtransactionAdmin)
admin.site.register(CustomerSupportTicket,CustomerSupportTicketAdmin)
