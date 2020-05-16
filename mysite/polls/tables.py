import django_tables2 as tables
from .models import PozycjaZakupowa, Sklep


class PozycjaZakupowaTable(tables.Table):
    class Meta:
        model = PozycjaZakupowa
        #template_name = "django_tables2/table.html"

class SklepTable(tables.Table):
    class Meta:
        model = Sklep
        #template_name = "django_tables2/table.html"

