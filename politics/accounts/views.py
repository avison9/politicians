from django.shortcuts import render,redirect
from .forms import RegisterForm, LoginForm

# Home page
def home(request):
    return render(request,'accounts/index.html' )

# Registration a user
def register(request):

    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()            

            # return redirect('home')

    context = {'form': form}

    return render(request, 'accounts/registration.html', context)
