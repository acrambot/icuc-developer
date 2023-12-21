"""
URL configuration for Practice project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Hibah.views import index_view,DepartmentFormView,Employee_Form_View,Customer_Form_View,Salesorder_Form_View,CustomerSupportTicket_Form_View,Product_Form_View,Financialtransaction_Form_View,edit_Department_View,edit_Employee_View,edit_Customer_View,edit_CustomerSupportTicket_View,edit_Financialtransaction_View,edit_Product_View,edit_SalesOrder_View,Department_Delete_View,Customer_Delete_View,Employee_Delete_View,Customersupportticket_Delete_View,Financialtransaction_Delete_View,Salesorder_Delete_View,Product_Delete_View,Sign_up_View
from Hibah.views import Department_List_View,Employee_List_View,Customer_List_View,Salesorder_List_View,CustomerSupportTicket_List_View,Product_List_View,Financialtransaction_List_View


urlpatterns = [
    path('admin/', admin.site.urls),
    #path("directory",nameofview,name=pagename)
    #path("",index_view,name="index_page"),
    path("",index_view,name="index_page"),
    path('DepartmentForm/',DepartmentFormView,name="DepartmentFormPage"),
    path('DepartmentList/',Department_List_View,name="DepartmentListPage"),
    path('EmployeeForm/',Employee_Form_View,name="EmployeeFormPage"),
    path('EmployeeList/',Employee_List_View,name="EmployeeListPage"),
    path('CustomerForm/',Customer_Form_View,name="CustomerFormPage"),
    path('CustomerList/',Customer_List_View,name="CustomerListPage"),
    path('SalesorderForm/',Salesorder_Form_View,name="SalesorderFormPage"),
    path('SalesorderList/',Salesorder_List_View,name="SalesorderListPage"),
    path('CustomerSupportTicketForm/',CustomerSupportTicket_Form_View,name="CustomerSupportTicketFormPage"),
    path('CustomerSupportTicketList/',CustomerSupportTicket_List_View,name="CustomerSupportTicketListPage"),
    path('Product/',Product_Form_View,name="ProductFormPage"),
    path('ProductList/',Product_List_View,name="ProductListPage"),
    path('FinancialtransactionForm/',Financialtransaction_Form_View,name="FinancialtransactionFormPage"),
    path('FinancialtransactionList/',Financialtransaction_List_View,name="FinancialtransactionListPage"),
    path('editdepartment/<int:department_id>/',edit_Department_View,name="EditDepartmentPage"),
    path('editemployee/<int:employee_id>/',edit_Employee_View,name="EditEmployeePage"),
    path('editcustomer/<int:customer_id>/',edit_Customer_View,name="EditCustomerPage"),
    path('editcustomersupportticket/<int:customersupportticket_id>/',edit_CustomerSupportTicket_View,name="EditCustomerSupportTicketPage"),
    path('editfinancialtransaction/<int:financialtransaction_id>/',edit_Financialtransaction_View,name="EditFinancialtransactionPage"),
    path('editproduct/<int:product_id>/',edit_Product_View,name="EditProductPage"),
    path('editsalesorder/<int:salesorder_id>/',edit_SalesOrder_View,name="EditSalesorderPage"),
    path('deletedepartment/<int:department_id>/',Department_Delete_View,name="DeleteDepartmentPage"),
    path('deleteemployee/<int:employee_id>/',Employee_Delete_View,name="DeleteEmployeePage"),
    path('deletecustomer/<int:customer_id>/',Customer_Delete_View,name="DeleteCustomerPage"),
    path('deletecustomersupportticket/<int:customersupportticket_id>/',Customersupportticket_Delete_View,name="DeleteSupportTicketPage"),
    path('deletefinancialtransaction/<int:financialtransaction_id>/',Financialtransaction_Delete_View,name="DeleteFinancialtransactionPage"),
    path('deletesalesorder/<int:salesorder_id>/',Salesorder_Delete_View,name="DeleteSalesorderPage"),
    path('deleteproduct/<int:product_id>/',Product_Delete_View,name="DeleteProductPage"),
    path('sign_up/',Sign_up_View,name="SignUpPage"),
    path('accounts/',include('django.contrib.auth.urls'))
]
