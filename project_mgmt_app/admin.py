from django.contrib import admin
from .models import Client, Employee, Task, Invoice, Project


class TasksInline(admin.TabularInline):
    model = Task
    extra = 0


class InvoicesInline(admin.TabularInline):
    model = Invoice
    extra = 0  


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'display_clients', 'display_employees']
    inlines = [TasksInline, InvoicesInline]


admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Invoice)
admin.site.register(Project, ProjectAdmin)