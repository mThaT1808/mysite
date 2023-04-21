from django import forms
from individual_work_2 import models



class DepartmentForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = '__all__'

class DepartmentWorkerForm(forms.Form):
    worker_name = forms.CharField(label='Имя работника', max_length=50)
    worker_phone_number = forms.CharField(label='Номер телефона работника', max_length=100)
    worker_department = forms.ModelChoiceField(label='Отдел работника', queryset=models.Department.objects.all())
    department_name = forms.CharField(label='Название отдела', max_length=50)
    department_description = forms.CharField(label='Примечание', max_length=500)


