from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Application, Event
from .forms import EventForm
from django.contrib.auth.decorators import login_required


def index(request):

    return render(request, 'polls/SchoolMain.html', {"welcome": "Добро пожаловать!"})


def show_equipment(request):
    return render(request, 'polls/Equipment.html')


def show_best_graduates(request):
    return render(request, 'polls/BestGraduates.html')


def show_graduation(request):
    return render(request, 'polls/Graduation2020.html')


def show_traditions(request):
    return render(request, 'polls/Traditions.html')


def show_test(request):
    return render(request, 'polls/Test.html')


def changemode(request, dark):
    colour = dark
    return render(request, 'polls/SchoolMain.html', {"welcome": "Добро пожаловать!", "colour": colour})


@csrf_exempt
def getform(request):

    if request.method == 'GET':
        return render(request, 'polls/Form.html')
    if request.method == 'POST':
        sname = request.POST["studentName"]
        ssurname = request.POST["studentSurname"]
        sfather_name = request.POST["studentFathersName"]
        saddress = request.POST["studentAddress"]
        sdate = request.POST["studentDate"]
        sphone = request.POST["studentPhone"]
        semail = request.POST["studentEmail"]
        sgrade = request.POST["grades"]
        new_student = Student(first_name=sname, father_name=sfather_name, last_name=ssurname, address=saddress, birth_date=sdate, tel=sphone, email=semail, grade=sgrade)
        new_student.save()
        new_application = Application(student=new_student)
        new_application.save()
        return render(request, 'polls/Form.html')


@csrf_exempt
def apps_info(request):

    applications = Application.objects.all()
    return render(request, 'polls/tables.html', {'applications': applications})


def add_and_save(request):
    if request.method == 'POST':
        ef = EventForm(request.POST)
        if ef.is_valid():
            ef.save()
            return HttpResponseRedirect(reverse('form'))
        else:
            context = {'form': ef}
            return render(request, 'polls/Form.html', context)
    else:
        ef = EventForm()
        context = {'form': ef}
        return render(request, 'polls/Form.html', context)


def staffIndex(request, responsibleStaff_id=0):
    events = Event.objects.filter(responsibleStaff__pk=responsibleStaff_id).order_by('-date')
    staff = events[0].responsibleStaff
    return render(request, 'polls/staffIndex.html', {'events': events, 'responsibleStaff': staff})