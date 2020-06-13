from django.shortcuts import render
from contactme.forms import formcontactdetails


def contact(request):
    form=formcontactdetails(request.POST)
    if form.is_valid():
        form.save()
    
    context={'form':form}

    return render(request,'contact.html',context)
