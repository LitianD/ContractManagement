from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(unique=True, null=False, max_length=50)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    level = models.IntegerField()


class Contract(models.Model):
    contract_id = models.IntegerField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True)
    results = models.CharField(max_length=150)
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    price = models.IntegerField()
    abstract = models.CharField(max_length=150)
    # 外键
    username = models.CharField(max_length=50)
    # 审查情况 未审查 正在审查 审查通过
    content = models.CharField(max_length=500)


class CheckInfo(models.Model):
    # 外键
    contract_id = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    # 通过 不通过
    results = models.CharField(max_length=50)
    content = models.CharField(max_length=150)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    price = models.IntegerField()

