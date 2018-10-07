from django.shortcuts import render
from .forms import CustomerForm
from django.http import HttpResponse
from .models import Customer


def regview(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            username = form.cleaned_data['username']
            pwd = form.cleaned_data['pwd']
            mn = form.cleaned_data['mn']
            c = Customer.objects.create(fname=fname, lname=lname, username=username, pwd=pwd, mn=mn)
            return render(request, 'result.html', {'fname': fname,
                                                   'lname': lname,
                                                   'username': username,
                                                   'pwd': pwd,
                                                   'mn': mn})
        else:
            return HttpResponse(form.errors)

    else:
        form = CustomerForm()
        return render(request, 'indexcontact.html', {'form': form})
