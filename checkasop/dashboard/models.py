from django.db import models

class Snls(models.Model):
    pan = models.CharField("Hash-PAN", max_length=14)
    serias = models.CharField("Транспортная серия", max_length=2)

class Sub(models.Model):
    id_sub = models.IntegerField("ID записи")
    serias = models.IntegerField("Транспортная серия")
    since = models.DateTimeField("Дата начала действия")
    till = models.DateTimeField("Дата окончания действия")
    sale_date = models.DateTimeField("Дата добавления")
    pan = models.CharField("Hash-PAN", max_length=14)

    def __str__(self):
        return f'{self.id_sub}, {self.serias}, {self.since.strftime('"%Y-%m-%d %H:%M"')}, {self.till.strftime('"%Y-%m-%d %H:%M"')}, {self.sale_date.strftime('"%Y-%m-%d %H:%M"')}, {self.pan}'

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