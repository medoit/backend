from django.db import models

class Snls(models.Model):
    pan = models.CharField(max_length=14)
    serias = models.CharField(max_length=2)

class Sub(models.Model):
    serias = models.IntegerField()
    since = models.DateTimeField("Дата начала действия")
    till = models.DateTimeField("Дата окончания действия")
    sale_date = models.DateTimeField("Дата добавления")
    pan = models.CharField(max_length=14)

class Terminal(models.Model):
    serial_number = models.IntegerField()
    description = models.CharField(max_length=254)
    last_date_update = models.DateTimeField("Дата последнего обновления")
    version_sw = models.CharField(max_length=6)

class Transaction(models.Model):
    terminal_sn = models.IntegerField()
    datetime = models.DateTimeField("Дата и время транзацкии")
    serias = models.CharField(max_length=2)
    ticket_number = models.CharField(max_length=4)
    price = models.IntegerField()
    pan = models.CharField(max_length=14)
