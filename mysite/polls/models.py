from django.db import models

# Create your models here.
from django.db import models


class Sklep(models.Model):
    nazwa_sklep = models.CharField(max_length=200)
    def __str__(self):
        return self.nazwa_sklep


class NazwaTowaru(models.Model):
    nazwa_towar = models.CharField(max_length=200)
    def __str__(self):
        return self.nazwa_towar



class PozycjaZakupowa(models.Model):
    nazwa_towar = models.ForeignKey(NazwaTowaru, on_delete=models.CASCADE, blank=True, null=True)
    ilosc = models.IntegerField(default=0)
    cena = models.FloatField(default=0.00)
    nazwa_sklep = models.ForeignKey(Sklep, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        s = str(self.nazwa_towar) + ', ilość: ' + str(self.ilosc) + ', cena: ' + str(self.cena) + ' zł, sklep: ' + str(self.nazwa_sklep)
        return s
    @property
    def total_price(self):
        return 4


