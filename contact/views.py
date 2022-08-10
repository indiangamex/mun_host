from django.shortcuts import render, HttpResponse
from django.contrib import messages
from contact.models import Contact
from contact.models import Idelegate
from contact.models import Sdelegate
from datetime import datetime
def index(request):
    return render(request, "index.html")
def unga(request):
    return render(request, "unga.html")
def unhrc(request):
    return render(request, "unhrc.html")
def aippm(request):
    return render(request, "aippm.html")
def ip(request):
    return render(request, "ip.html")
def crisis(request):
    return render(request, "crisis.html")
def letter(request):
    return render(request, "letter.html")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Contact has been sent !!')
    return render(request, "contact.html")
def idelegate(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        ids = Idelegate(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        ids.save()
        messages.success(request, 'Your request as a Individual delegate has been sent !!')
    return render(request, "idelegate.html")
def sdelegate(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        sds = Sdelegate(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        sds.save()
        messages.success(request, 'Your request as a School delegate has been sent !!')
    return render(request, "sdelegate.html")
