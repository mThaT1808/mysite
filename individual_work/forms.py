from django import forms
from individual_work import models
from individual_work.models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = models.Job
        fields = '__all__'


class CustomerForm(forms.Form):
    customer_name = forms.CharField(label='Customer name', max_length=100)
    customer_phone_number = forms.CharField(label='Customer phone number', max_length=10)


CHOICES = (
    ('1', 'Я умный'),
    ('2', 'Я красивый'),
    ('3', 'Я умный и красивый'),
)


class ContractorCustomerForm(forms.Form):

    contractor_name = forms.CharField(label='Имя подрядчика', max_length=100)
    contractor_description = forms.CharField(label='Примечание', max_length=500)
    contractor_job = forms.ModelChoiceField(label='Работа подрядчика', queryset=Job.objects.all())
    customer_name = forms.CharField(label='Имя заказччика', max_length=100)
    customer_phone_number = forms.CharField(label='Номер телефона заказчика', max_length=100)
    useless_choice = forms.ChoiceField(label='Важнейший выбор', choices=CHOICES)
