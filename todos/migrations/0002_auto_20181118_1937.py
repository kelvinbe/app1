# Generated by Django 2.1 on 2018-11-18 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20181118_1937'),
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todolist',
            new_name='Todo',
        ),
    ]
