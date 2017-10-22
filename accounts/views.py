from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm


def register_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return render(request, 'accounts/profile.html', {'user_id': user.pk})

                return render(request, 'crunchy_home/index.html', {'user_id': user.pk})

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)

                return render(request, 'accounts/profile.html', {'user_id': user.pk})

                return render(request, 'crunchy_home/index.html', {'user_id': user.pk})

            else:
                return render(request, 'accounts/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Invalid login'})
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def profile_user(request, user_id):
    context = {
        'user_id': user_id,
    }
    return render(request, 'accounts/profile.html', context)


