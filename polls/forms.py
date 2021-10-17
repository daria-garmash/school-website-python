from django.forms import ModelForm
from django.forms.widgets import TextInput, Select
from .models import Event, Student


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'responsibleStaff', 'date', 'description')
        labels = {'name': 'Мероприятие',
                  'responsibleStaff': 'Ответственный за проведение',
                  'date': 'Дата проведения',
                  'description': 'Краткое описание'}
        widgets = {'name': TextInput(),
                   'responsibleStaff': Select(attrs={'size': 1})}


class Form(ModelForm):
    class Meta:
        model = Student
        fields = ("first_name", "last_name", "address", "birth_date", "grade")
