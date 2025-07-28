from django.shortcuts import render
from contactus_app.models import Contact,Message
from project_app import models

# Create your views here.

def home(request):

    if request.method == 'POST':
        context = {"errors":[]}
        name = request.POST.get('name')
        email = request.POST.get('email')
        title = request.POST.get('title')
        message = request.POST.get('message')
        if name and email and title and message:
            Message.objects.create(name=name, email=email, title=title, message=message)
        else:
            context["errors"].append("لطفا تمامی موارد را پر کنید و سپس بعد از آن دکمه ی ارسال را بزنید.")
        fooder = Contact.objects.all().last()
        project = models.Project.objects.all()
        return render(request,"index.html",context={"fooder":fooder,"project":project,"context":context})

    fooder = Contact.objects.all().last()
    project = models.Project.objects.all()
    return render(request, "index.html", context={"fooder": fooder, "project": project})