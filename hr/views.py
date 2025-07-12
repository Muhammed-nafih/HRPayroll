from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.urls import reverse
# Create your views here.
def login_view(request):
    # If already logged in, send them on
    if request.user.is_authenticated:
        return redirect(reverse('dashboard'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('dashboard'))
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')