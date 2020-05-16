from django.contrib import admin
from .models import Sklep
from .models import NazwaTowaru
from .models import PozycjaZakupowa

# Register your models here.
admin.site.register(Sklep)
admin.site.register(NazwaTowaru)
admin.site.register(PozycjaZakupowa)


