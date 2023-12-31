# Generated by Django 4.2.4 on 2023-09-07 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerId', models.IntegerField()),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('others', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentId', models.IntegerField()),
                ('departmentname', models.CharField(max_length=200)),
                ('salaryscale', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeId', models.IntegerField()),
                ('firstname', models.CharField(max_length=200)),
                ('others', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('DOB', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('maritalstatus', models.CharField(choices=[('S', 'Single'), ('M', 'Married')], max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('departmentname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hibah.department')),
            ],
        ),
        migrations.CreateModel(
            name='Financialtransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionId', models.IntegerField()),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.IntegerField()),
                ('productname', models.CharField(max_length=100)),
                ('stockquantity', models.IntegerField()),
                ('unitprice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Salesorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.IntegerField()),
                ('orderdate', models.DateField()),
                ('totalamount', models.IntegerField()),
                ('EmployeeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hibah.employee')),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hibah.customer')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerSupportTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticketId', models.IntegerField()),
                ('customerIssueDescription', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('O', 'Open'), ('C', 'Closed'), ('I', 'In-progress')], max_length=100)),
                ('EmployeeId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hibah.employee')),
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hibah.customer')),
            ],
        ),
    ]
