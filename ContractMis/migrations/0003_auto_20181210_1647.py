# Generated by Django 2.1.2 on 2018-12-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContractMis', '0002_auto_20181210_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkinfo',
            name='email',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkinfo',
            name='name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='checkinfo',
            name='phone',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='price',
            field=models.IntegerField(default=3000),
            preserve_default=False,
        ),
    ]
