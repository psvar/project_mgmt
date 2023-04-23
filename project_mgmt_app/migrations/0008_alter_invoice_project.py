# Generated by Django 4.2 on 2023-04-20 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_mgmt_app', '0007_remove_project_invoice_invoice_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='project',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_invoice', to='project_mgmt_app.project'),
        ),
    ]
