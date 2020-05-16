import logging

from django.db.models import Sum, Count
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, DetailView
from django_filters import FilterSet
from django_tables2 import SingleTableView, MultiTableMixin
from django_filters.views import FilterView
from django.db.models import Avg

from .forms import NameForm
from .models import PozycjaZakupowa, Sklep



class SklepListView(SingleTableView):
    model = Sklep
    template_name = 'listazakupow.html'
    context_object_name = "all"


class PozycjaZakupowaListView(SingleTableView):
    model = PozycjaZakupowa
    template_name = 'listazakupow.html'
    total_paid = 5

    def sum(self):
        return self.aggregate(Avg('cena'))

class HomeView(TemplateView):

    template_name = 'index.html'

class ListaView(TemplateView):
    template_name = 'listazakupow.html'

    def get(self, request):
        sklepy = Sklep.objects.all()
        logger = logging.getLogger(__name__)

        #sklepy = PozycjaZakupowa.objects.values_list('nazwa_sklep').order_by('nazwa_sklep').all()
        skleps = []
        pozycje = PozycjaZakupowa.objects.all()
        for x in sklepy:
            for y in pozycje:

                if str(x.nazwa_sklep) == str(y.nazwa_sklep):
                    logger.error(str(x.nazwa_sklep))
                    if x in skleps:
                        continue
                    else:
                        skleps.append(x)

        #sklepy = Sklep.objects.all().order_by(*skleps)
        #suma = list(PozycjaZakupowa.objects.aggregate(Sum('cena')).values())[0]
        suma = 0
        for obj in PozycjaZakupowa.objects.all():
            suma += (obj.cena * obj.ilosc)
        suma = round(suma,2)
        args = {
            'pozycje': pozycje,
            'suma': suma,
            'sklepy': skleps
        }
        return render(request, self.template_name, args)

class FormView(TemplateView):
    template_name = 'form.html'

    def get(self, request):
        form = NameForm()
        sklepy = Sklep.objects.all()

        args = {
            'form': form,
            'sklepy': sklepy
        }
        return render(request, self.template_name, args)
    def post(self, request):
        form = NameForm(request.POST)
        if form.is_valid():
            nazwa_towar = form.save(commit=False)
            #nazwa_towar.user = request.user
            nazwa_towar.save()

            cena = form.save(commit=False)
            #cena.user = request.user
            cena.save()

            ilosc = form.save(commit=False)
            #ilosc.user = request.user
            ilosc.save()

            nazwa_sklep = form.save(commit=False)
            #nazwa_sklepu.user = request.user
            nazwa_sklep.save()

            nazwa_towar = form.cleaned_data['nazwa_towar']
            cena = form.cleaned_data['cena']
            ilosc = form.cleaned_data['ilosc']
            nazwa_sklep = form.cleaned_data['nazwa_sklep']


            form = NameForm()
            return redirect('/polls/lista')

        args = {'form': form}
        return render(request, self.template_name, args)


def index(request):
    template_name = 'index.html'

    return render(request, 'index.html')

