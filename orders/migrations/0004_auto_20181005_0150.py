# Generated by Django 2.0.3 on 2018-10-05 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20181005_0146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='name',
            new_name='order_name',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='name',
            new_name='pizza_name',
        ),
        migrations.RenameField(
            model_name='toppings',
            old_name='name',
            new_name='toppings_name',
        ),
    ]
