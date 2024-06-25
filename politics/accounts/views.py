from django.shortcuts import render,redirect
from .forms import UserRegisterForm, LoginForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login as auth_login, get_user_model


# Home page
def home(request):
    return render(request,'accounts/index.html' )

# Registration a user
def register(request):

    usr_cred = UserRegisterForm()

    if request.method == 'POST':

        usr_cred = UserRegisterForm(request.POST)

        if usr_cred.is_valid():

            usr_cred.save()            

            return redirect('login')

    context = {'usercred': usr_cred}

    return render(request, 'accounts/registration.html', context)



#Updating a user's detail
@login_required
def edit_form(request):

    user_edit_form = UserUpdateForm(instance=request.user)
    profile_edit_form = ProfileUpdateForm(instance=request.user.profile)

    if request.method == 'POST':
        user_edit_form = UserUpdateForm(instance=request.user, data=request.POST)
        profile_edit_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_edit_form.is_valid() and profile_edit_form.is_valid():
            user_edit_form.save()
            profile_edit_form.save()
        else:
            user_edit_form = UserUpdateForm(instance=request.user)
            profile_edit_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_edit_form': user_edit_form,
        'profile_edit_form': profile_edit_form
    }
    return render(request, 'accounts/edit_profile.html', context)

#Login a user
def login(request):

    form = LoginForm()

    if request.method == 'POST':

        # form = LoginForm(request, data=request.POST)
        form = LoginForm(request.POST or None)

        if form.is_valid():

            # username = request.POST.get('username')
            # password = request.POST.get('password')

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            usr = authenticate(request, username=username, password=password)

            if usr is not None:

                auth_login(request, usr)

                return redirect('dashboard')

    context = {
        'login': form
    }

    return render(request, 'accounts/login.html', context)



#dashboard view
@login_required(login_url='login')
def dashboard(request):

    return render(request,'accounts/dashboard.html')


def logout(request):

    auth.logout(request)

    return render(request, 'accounts/logout.html')




    




