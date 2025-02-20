from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()

CHOICES = [
        ('value1', 'What was your first pet\'s name?'),
        ('value2', 'What is the name of your elementary school?'),
        ('value3', 'What city did your parents meet each other?'),
]

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
        template_data['choices'] = CHOICES
        return render(request, 'accounts/signup.html',{'template_data': template_data})
    elif request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        security_question = request.POST['security_question']
        security_answer = request.POST['security_answer']

        if not CustomUser.objects.filter(username=username).exists():
            if password1 == password2:
                user = CustomUser.objects.create_user(username=username, password=password1, security_question=security_question, security_answer=security_answer)
                auth_login(request, user)
                return redirect('home.index')
            else:
                template_data['error'] = 'Passwords do not match.'
                template_data['choices'] = CHOICES
                return render(request, 'accounts/signup.html',{'template_data': template_data})
        else:
            template_data['error'] = 'Username already taken.'
            template_data['choices'] = CHOICES
            return render(request, 'accounts/signup.html',{'template_data': template_data})

        # if form.is_valid():
        #     print(request.POST)
        #     user = form.save()
        #     auth_login(request, user)
        #     return redirect('home.index')
        # else:
        #     return render(request, 'accounts/signup.html',{'template_data': template_data})

def reset(request):
    template_data = {}
    template_data['title'] = 'Reset Password'

    if request.method == 'GET':
        template_data['choices'] = CHOICES
        return render(request, 'accounts/reset.html', {'template_data': template_data})

    elif request.method == 'POST':
        username = request.POST['username']
        new_password = request.POST['new_password']
        security_question = request.POST['security_question']
        security_answer = request.POST['security_answer']

        try:
            user = CustomUser.objects.get(username=username)

            if user.security_question == security_question:
                if user.security_answer == security_answer:
                    if not user.check_password(new_password):
                        user.set_password(new_password)
                        user.save()

                        template_data['error'] = 'Success!'

                        return redirect('home.index')
                    else:
                        template_data['error'] = "New password must not match previous password."
                else:
                    template_data['error'] = 'Invalid security question or answer.'
            else:
                    template_data['error'] = 'Invalid security question or answer.'
        except User.DoesNotExist:
            template_data['error'] = 'User does not exist.'
    template_data['choices'] = CHOICES
    return render(request, 'accounts/reset.html', {'template_data': template_data})

@login_required
def orders(request):
    template_data = {}
    template_data['title'] = 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'accounts/orders.html',{'template_data': template_data})
