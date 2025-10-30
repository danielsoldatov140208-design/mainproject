from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import UnlRegisterForm
from django.contrib.auth import get_user_model
User = get_user_model()



def home(request):
    return render(request, 'main.html')

def sale(request):
    return render(request, 'sale.html')

@login_required
def user_profile(request, username):
    user_obj = get_object_or_404(User, username=username)
    return render(request, 'profile.html', {'user_obj': user_obj})


def register(request):
    if request.method == 'POST':
        form = UnlRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # <-- авторизация сразу после регистрации
            return redirect('home')
    else:
        form = UnlRegisterForm()
    return render(request, 'register.html', {'form': form})
