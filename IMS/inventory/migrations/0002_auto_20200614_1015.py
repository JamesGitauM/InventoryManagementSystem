# Generated by Django 3.0.3 on 2020-06-14 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='status',
            field=models.CharField(choices=[('AVAILABLe', 'Item read to be purchased'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in a Few Days')], default='SOLD', max_length=10),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(choices=[('AVAILABLe', 'Item read to be purchased'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in a Few Days')], default='SOLD', max_length=10),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='status',
            field=models.CharField(choices=[('AVAILABLe', 'Item read to be purchased'), ('SOLD', 'Item Sold'), ('RESTOCKING', 'Item restocking in a Few Days')], default='SOLD', max_length=10),
        ),
    ]
