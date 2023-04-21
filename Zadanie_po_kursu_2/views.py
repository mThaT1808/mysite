import random
from django.shortcuts import render, HttpResponseRedirect
from Zadanie_po_kursu_2 import forms, models
from Zadanie_po_kursu_2.models import User
# Create your views here.


def start_page(request):

    return render(request, 'HelloPage.html')


def registration_page(request):

    for i in User.objects.all():
        i.current_user = False
        i.save()

    def gen_luna_index(card_number):
        luna_index = 0
        t = card_number % 10
        luna_index += t
        t = ((card_number // 10) % 10) * 2
        if t > 9:
            t -= 9
        luna_index += t
        t = (card_number // 100) % 10
        luna_index += t
        t = ((card_number // 1000) % 10) * 2
        if t > 9:
            t -= 9
        luna_index += t
        return luna_index

    def generate_card_number():
        card_number = ''
        users = User.objects.all()
        while True:
            luna_index = 0
            card_number1 = int(random.uniform(1000, 9999))
            card_number2 = int(random.uniform(1000, 9999))
            card_number3 = int(random.uniform(1000, 9999))
            card_number4 = int(random.uniform(1000, 9999))
            luna_index += gen_luna_index(card_number1)
            luna_index += gen_luna_index(card_number2)
            luna_index += gen_luna_index(card_number3)
            luna_index += gen_luna_index(card_number4)
            if luna_index % 10 == 0:
                break
        card_number += str(card_number1)
        card_number += str(card_number2)
        card_number += str(card_number3)
        card_number += str(card_number4)
        for i in users:
            if card_number == i.card_number:
                generate_card_number()
        return card_number

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            obj = models.User()
            obj.name = form.cleaned_data['username']
            obj.pin = form.cleaned_data['pin']
            obj.card_number = generate_card_number()
            obj.current_user = True
            obj.save()
            bal = models.Balance()
            bal.user = User.objects.get(id=obj.id)
            bal.save()
            return HttpResponseRedirect('/Zadanie_po_kursu_2/home_page/')
    else:
        form = forms.UserForm()

    return render(request, 'registration_page.html', {'form': form})


def login_page(request):
    for i in User.objects.all():
        i.current_user = False
        i.save()

    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            obj = models.User()
            obj.name = form.cleaned_data['username']
            obj.pin = form.cleaned_data['pin']
            for i in User.objects.all():
                if i.name == obj.name and i.pin == obj.pin:
                    i.current_user = True
                    i.save()
                    return HttpResponseRedirect(f'/Zadanie_po_kursu_2/home_page/')
    else:
        form = forms.LoginForm()
    return render(request, 'login_page.html', {'form': form})


def home_page(request):
    for i in User.objects.all():
        if i.current_user == True:
            username = i.name
            card_number = i.card_number
            balance = models.Balance.objects.get(user=i.id)
            context = {
                'username': username,
                'card_number': card_number,
                'balance': balance,
            }
            return render(request, 'home_page.html', context)

    return HttpResponseRedirect('/Zadanie_po_kursu_2/log/')


def add_money(request):
    if request.method == 'POST':
        form = forms.AddMoneyForm(request.POST)
        if form.is_valid():
            obj = User.objects.get(current_user=True)
            obj_balance = models.Balance.objects.get(user=obj.id)
            obj_balance.rub += form.cleaned_data['rub']
            obj_balance.usd += form.cleaned_data['usd']
            obj_balance.eur += form.cleaned_data['eur']
            obj_balance.save()
            return HttpResponseRedirect('/Zadanie_po_kursu_2/home_page')
    else:
        form = forms.AddMoneyForm()
    return render(request, 'add_money_page.html', {'form': form})


def take_money(request):
    if request.method == 'POST':
        form = forms.TakeMoneyForm(request.POST)
        if form.is_valid():
            obj = User.objects.get(current_user=True)
            obj_balance = models.Balance.objects.get(user=obj.id)
            obj_balance.rub -= form.cleaned_data['rub']
            obj_balance.usd -= form.cleaned_data['usd']
            obj_balance.eur -= form.cleaned_data['eur']
            obj_balance.save()
            return HttpResponseRedirect('/Zadanie_po_kursu_2/home_page')
    else:
        form = forms.TakeMoneyForm()
    return render(request, 'take_money_page.html', {'form': form})
