# Generated by Django 4.1.7 on 2023-04-19 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_mgmt_app', '0002_remove_project_invoices_remove_project_tasks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='invoices',
        ),
        migrations.RemoveField(
            model_name='project',
            name='tasks',
        ),
        migrations.AddField(
            model_name='invoice',
            name='project',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_mgmt_app.project'),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_mgmt_app.project'),
        ),
    ]
