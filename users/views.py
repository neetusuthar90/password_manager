from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm

def home(request):
    return render(request, 'users/home.html')

#create registration form
def register(request):
    submitted = False
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = RegistrationForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'users/add_user.html', {'form': form, 'submitted':submitted})
