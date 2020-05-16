from django import forms

from .models import Sklep, PozycjaZakupowa, NazwaTowaru


class NameForm(forms.ModelForm):
    nazwa_towar = forms.ModelChoiceField(queryset=NazwaTowaru.objects.all())

    cena = forms.FloatField(widget=forms.NumberInput(
        attrs={
            'placeholder': 'Podaj cenę...'
        }
    ))
    ilosc = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'placeholder': 'Podaj ilość...'
        }
    ))
    nazwa_sklep = forms.ModelChoiceField(queryset=Sklep.objects.all())

    class Meta:
        model = PozycjaZakupowa
        #fields = '__all__'
        fields = ('nazwa_towar', 'cena', 'ilosc', 'nazwa_sklep',)