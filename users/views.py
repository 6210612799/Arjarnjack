from django.http.response import HttpResponse, HttpResponseRedirect
import users
from django.shortcuts import get_object_or_404, render 
from .models import Couses, Nisit
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "users/index.html",
    {
        "couses" : Couses.objects.all()
    })
def do_couses(request , couses_id):
    nisitall = []
    couses = Couses.objects.get(id= couses_id)
    for nisit in Nisit.objects.all():
        for couse in nisit.couses.all(): 
            if (couse == couses):
                nisitall.append(nisit)

    return render(request, "users/couses.html",{
        "couses" : couses,
        "nisitall" : nisitall,
        "non_student" : Nisit.objects.exclude(couses=couses).all()
        
    })
def book(request, couses_id):
    if request.method == "POST":
        couses = get_object_or_404(Couses, pk = couses_id)
        student = request.POST["student"]
        couses.student.add(student)
        return HttpResponseRedirect(reverse("users:couses",args=(couses_id,)))



