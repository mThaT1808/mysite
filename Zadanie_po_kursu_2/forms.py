from django import forms
from Zadanie_po_kursu_2 import models

class UserForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=50)
    pin = forms.CharField(label='Придумайте PIN код', max_length=4)

class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=50)
    pin = forms.CharField(label='PIN код', max_length=4)


class AddMoneyForm(forms.Form):
    rub = forms.IntegerField(label='RUB Введите сумму, которую хотите внести:')
    usd = forms.IntegerField(label='USD Введите сумму, которую хотите внести:')
    eur = forms.IntegerField(label='EUR Введите сумму, которую хотите внести:')

class TakeMoneyForm(forms.Form):
    rub = forms.IntegerField(label='RUB Введите сумму, которую хотите снять:')
    usd = forms.IntegerField(label='USD Введите сумму, которую хотите снять:')
    eur = forms.IntegerField(label='EUR Введите сумму, которую хотите снять:')