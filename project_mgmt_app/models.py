from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    first_name = models.CharField("First name", max_length=1000)
    last_name = models.CharField("Last name", max_length=1000)
    company = models.CharField("Company", max_length=1000)
    phone = models.IntegerField("Phone number")
    email = models.EmailField("Email address")

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.company} ({self.phone}; {self.email})"


class Employee(models.Model):
    first_name = models.CharField("First name", max_length=1000)
    last_name = models.CharField("Last name", max_length=1000)
    position = models.CharField("Position", max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.position}"
    

class Project(models.Model):
    name = models.CharField("Name", max_length=1000)
    start_date = models.DateField("Start date")
    due_date = models.DateField("Due date")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    clients = models.ManyToManyField(Client)
    employees = models.ManyToManyField(Employee)

    def display_clients(self):
        return ", ".join(client.company for client in self.clients.all())
    
    def display_employees(self):
        return ", ".join(employee.last_name for employee in self.employees.all())
    
    def __str__(self):
        return f"{self.name} {self.user}"
    

class Invoice(models.Model):
    issue_date = models.DateField("Issue date")
    total_amount = models.IntegerField("Total amount")
    project = models.ForeignKey("Project", on_delete=models.SET_NULL, null=True, default=None, related_name='invoice')

    def __str__(self):
        return f"{self.total_amount} ({self.issue_date})"
    

class Task(models.Model):
    task_name = models.CharField("Name", max_length=1000)
    notes = models.CharField("Notes", max_length=1000)
    project = models.ForeignKey("Project", on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return f"{self.task_name}: {self.notes}"


