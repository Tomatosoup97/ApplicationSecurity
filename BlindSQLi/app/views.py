from django.shortcuts import render
from django.http.request import HttpRequest
from .models import Patient


def get_users(request):
    if 'id' in request.GET:
        query = "SELECT * FROM app_patient WHERE "\
                "app_patient.id={0}".format(
                    request.GET.get('id'))
        users = Patient.objects.raw(query)
    else:
        users = Patient.objects.all()

    return render(request, 'users.html', {'users': users})
