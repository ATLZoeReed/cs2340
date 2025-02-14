from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList, PasswordResetForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')

def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'accounts/login.html',
                       {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
    if user is None:
        template_data['error'] = 'Invalid username or password.'
        return render(request, 'accounts/login.html',
                      {'template_data': template_data})
    else:
        auth_login(request, user)
        return redirect('home.index')

def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'

    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',{'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home.index')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html',{'template_data': template_data})

@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html',{'template_data': template_data})

@login_required
def password_reset(request):
    template_data = {}
    template_data['title'] = 'Password Reset'

    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            old_password = form.cleaned_data['old_password']
            new_password = form.cleaned_data['new_password']
            user = request.user
            # I think this is where the error is at.

            if not request.user.is_authenticated:
                messages.error(request, 'You must be logged in to reset your password!')
                return redirect('login')

            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()

                messages.success(request, 'Your password has been successfully updated!')
                return redirect('home.index')
            else:
                messages.error(request, 'Old password is incorrect!')
        else:
            messages.error(request, 'Invalid form!')
    else:
        form = PasswordResetForm()
    return render(request, 'accounts/password_reset.html', {'form': form})