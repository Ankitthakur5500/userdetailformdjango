from django.shortcuts import render
from home.models import Home

def home(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        details = Home(firstname=firstname,lastname=lastname,username=username,address=address,city=city,zip=zip)
        details.save()
    
    return render(request, 'form.html')