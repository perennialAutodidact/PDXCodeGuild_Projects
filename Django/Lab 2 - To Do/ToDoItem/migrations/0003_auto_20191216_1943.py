# Generated by Django 3.0 on 2019-12-17 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoItem', '0002_auto_20191216_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='completed_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]