from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
#importing the forms created
from Hibah.forms import DepartmentForm,EmployeeForm,CustomerForm,SalesorderForm,CustomerSupportTicketForm,ProductForm,FinancialtransactionForm
from Hibah.models import Department,Employee,Customer,Salesorder,CustomerSupportTicket,Product,Financialtransaction

# Create your views here.
def index_view(request):
    return render (request, "index.html")

def DepartmentFormView(request):
    message = ''
    if request.method =="POST":
        departmentform =DepartmentForm(request.POST)

        if departmentform.is_valid():
            departmentform.save()
            if departmentform.save():
                departmentform= DepartmentForm()
           
    else:
        departmentform= DepartmentForm()

   
 
    context ={
        "form": departmentform,
        

    }
    return render(request,"department.html",context)

def Department_List_View(request):
    departments_list=Department.objects.all()

    context={
            "list":departments_list
        }
    return render (request,"departmentlist.html",context)

def Employee_Form_View(request):
        if request.method=="POST":
            employeeform=EmployeeForm(request.POST)
            if employeeform.is_valid():
                employeeform.save()

        else:
            employeeform=EmployeeForm()

        context={
            "form":employeeform
        }
        return render(request,"Employee.html",context)

def Employee_List_View(request):
    employees_list=Employee.objects.all()

    context={
        "list":employees_list
    }
    return render(request,"employeelist.html",context)

def Customer_Form_View(request):
    if request.method=="POST":
        customerform=CustomerForm(request.POST)
        if customerform.is_valid():
            customerform.save()

    else:
        customerform=CustomerForm()

    context={
        "form":customerform
    }
    return render(request,"Customer.html",context)

def Customer_List_View(request):
    customers_list=Customer.objects.all()

    context={
        "list":customers_list
    }
    return render(request,"customerlist.html",context)

def Salesorder_Form_View(request):
    if request.method=="POST":
        salesorderform=SalesorderForm(request.POST)
        if salesorderform.is_valid():
            salesorderform.save()

    else:
        salesorderform=SalesorderForm()

    context={
        "form":salesorderform
    }
    return render(request,"salesorder.html",context)

def Salesorder_List_View(request):
    salesorders_list=Salesorder.objects.all()

    context={
        "list":salesorders_list
    }
    return render(request,"salesorderlist.html",context)

def CustomerSupportTicket_Form_View(request):
    if request.method=="POST":
        customersupportticketform=CustomerSupportTicketForm(request.POST)
        if customersupportticketform.is_valid():
            customersupportticketform.save()

    else:
        customersupportticketform=CustomerSupportTicketForm()
    context={
        "form":customersupportticketform
    }
    return render(request,"CustomerSupportTicket.html",context)

def CustomerSupportTicket_List_View(request):
    customersupportticket_list=CustomerSupportTicket.objects.all()

    context={
        "list":customersupportticket_list
    }
    return render(request,"customersupportticketlist.html",context)

def Product_Form_View(request):
    if request.method=="POST":
        productform=ProductForm(request.POST)
        if productform.is_valid():
            productform.save()

    else:
        productform=ProductForm()

    context={
        "form":productform
    }
    return render(request,"Product.html",context)

def Product_List_View(request):
    product_list=Product.objects.all()

    context={
        "list":product_list
    }
    return render(request,"productlist.html",context)

def Financialtransaction_Form_View(request):
    if request.method=="POST":
        financialtransanctionform=FinancialtransactionForm(request.POST)
        if financialtransanctionform.is_valid():
            financialtransanctionform.save()

    else:
        financialtransanctionform=FinancialtransactionForm()

    context={
        "form":financialtransanctionform
    }
    return render(request,"Financialtransaction.html",context)

def Financialtransaction_List_View(request):
    financialtransanction_list=Financialtransaction.objects.all()

    context={
        "list":financialtransanction_list
    }
    return render(request,"financialtransactionlist.html",context)

def edit_Department_View(request,department_id):
    department=Department.objects.get(id=department_id)

    if request.method == "POST":
        departmentform = DepartmentForm(request.POST,instance=department)

        if departmentform.is_valid():
            departmentform.save()

    else:
            departmentform=DepartmentForm(instance=department)

    context={
        "form":departmentform,
        "department":department
    } 
    return render(request,"EditDepartment.html",context)

def edit_Employee_View(request,employee_id):
    employee=Employee.objects.get(id=employee_id)
    if request.method=="POST":
        employeeform=EmployeeForm(request.POST,instance=employee)
        if employeeform.is_valid():
                employeeform.save()
    else:
        employeeform=EmployeeForm(instance=employee)
    context={
        "form":employeeform,
        "employee":employee
    }
    return render(request,"EditEmployee.html",context)

def edit_Customer_View(request,customer_id):
    customer=Customer.objects.get(id=customer_id)
    if request.method=="POST":
        customerform=CustomerForm(request.POST,instance=customer)
        if customerform.is_valid():
            customerform.save()
    else:
        customerform=CustomerForm(instance=customer)
    context={
        "form":customerform,
        "customer":customer
    }
    return render(request,"EditCustomer.html",context)

def edit_CustomerSupportTicket_View(request,customersupportticket_id):
    customersupportticket=CustomerSupportTicket.objects.get(id=customersupportticket_id)
    if request.method=="POST":
        customersupportticketform=CustomerSupportTicketForm(request.POST,instance=customersupportticket)
        if customersupportticketform.is_valid():
            customersupportticketform.save()
    else:
        customersupportticketform=CustomerSupportTicketForm(instance=customersupportticket)
    context={
        "form":customersupportticketform,
        "customersupportticket":CustomerSupportTicket
    }
    return render(request,"EditSupportTickets.html",context)

def edit_Financialtransaction_View(request,financialtransaction_id):
    financialtransaction=Financialtransaction.objects.get(id=financialtransaction_id)
    if request.method=="POST":
        financialtransactionform=FinancialtransactionForm(request.POST,instance=financialtransaction)
        if financialtransactionform.is_valid():
            financialtransactionform.save()
    else:
        financialtransactionform=FinancialtransactionForm(instance=financialtransaction)
    context={
        "form":financialtransactionform,
        "financialtransaction":Financialtransaction
    }
    return render(request,"EditFinancialtransaction.html",context)

def edit_Product_View(request,product_id):
    product=Product.objects.get(id=product_id)
    if request.method=="POST":
        productform=ProductForm(request.POST,instance=product)
        if productform.is_valid():
            productform.save()
    else:
        productform=ProductForm(instance=product)
    context={
        "form":productform,
        "product":Product
    }
    return render(request,"EditProduct.html",context)

def edit_SalesOrder_View(request,salesorder_id):
    salesorder=Salesorder.objects.get(id=salesorder_id)
    if request.method=="POST":
        salesorderform=SalesorderForm(request.POST,instance=salesorder)
        if salesorderform.is_valid():
            salesorderform.save()
    else:
        salesorderform=SalesorderForm(instance=salesorder)
    context={
        "form":salesorderform,
        "salesorder":Salesorder
    }
    return render(request,"EditSalesorder.html",context)

def Department_Delete_View(request,department_id):
    department=Department.objects.get(id=department_id)
    department.delete()
    return redirect(Department_List_View)

def Employee_Delete_View(request,employee_id):
    employee=Employee.objects.get(id=employee_id)
    employee.delete()
    return redirect(Employee_List_View)

def Customer_Delete_View(request,customer_id):
    customer=Customer.objects.get(id=customer_id)
    customer.delete()
    return redirect(Customer_List_View)

def Customersupportticket_Delete_View(request,customersupportticket_id):
    customersupportticket=CustomerSupportTicket.objects.get(id=customersupportticket_id)
    customersupportticket.delete()
    return redirect(CustomerSupportTicket_List_View)

def Financialtransaction_Delete_View(request,financialtransaction_id):
    financialtransaction=Financialtransaction.objects.get(id=financialtransaction_id)
    financialtransaction.delete()
    return redirect(Financialtransaction_List_View)

def Salesorder_Delete_View(request,salesorder_id):
    salesorder=Salesorder.objects.get(id=salesorder_id)
    salesorder.delete()
    return redirect(Salesorder_List_View)

def Product_Delete_View(request,product_id):
    product=Product.objects.get(id=product_id)
    product.delete()
    return redirect(Product_List_View)

def Sign_up_View(request):
    if request.method=="POST":
        signupform=UserCreationForm(request.POST)
        if signupform.is_valid():
            signupform.save()
    else:
        signupform=UserCreationForm()
    context={
        "form":signupform
    }
    return render(request,"registration/sign_up.html",context)




