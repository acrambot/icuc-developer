from django.forms import ModelForm

from Hibah.models import Department,Employee,Customer,Salesorder,CustomerSupportTicket,Product,Financialtransaction

class DepartmentForm(ModelForm):
    class Meta:
        model=Department
        fields="__all__"

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields ="__all__"

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields ="__all__"

class SalesorderForm(ModelForm):
    class Meta:
        model = Salesorder
        fields ="__all__"

class CustomerSupportTicketForm(ModelForm):
    class Meta:
        model = CustomerSupportTicket
        fields ="__all__"

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields ="__all__"

class FinancialtransactionForm(ModelForm):
    class Meta:
        model = Financialtransaction
        fields ="__all__"