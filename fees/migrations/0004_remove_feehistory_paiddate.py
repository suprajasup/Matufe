# Generated by Django 2.1.5 on 2019-03-09 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0003_auto_20190309_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feehistory',
            name='paiddate',
        ),
    ]
