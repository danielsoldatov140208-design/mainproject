from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import UnlRegisterForm, AddPropertyForm
from django.contrib.auth import get_user_model
from .models import Property
User = get_user_model()



def home(request):
    return render(request, 'main.html')

def sale(request):
    return render(request, 'sale.html')

@login_required
def user_profile(request, username):
    user_obj = get_object_or_404(User, username=username)
    user_properties = Property.objects.filter(owner=user_obj)
    return render(request, 'profile.html', {
        'user_obj': user_obj
        ,'user_properties': user_properties,})


def register(request):
    if request.method == 'POST':
        form = UnlRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')
    else:
        form = UnlRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def add_property(request):
    if request.method == 'POST':
        form = AddPropertyForm(request.POST , request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.owner = request.user
            property.save()
            return redirect('profile', username=request.user.username)
    else:
        form = AddPropertyForm()
    return render(request, 'add_property.html', {'form': form})

def sale(request):
    properties = Property.objects.all()
    return render(request, 'sale.html', {'properties': properties})

@login_required
def delete_property(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)

    if property_obj.owner != request.user:
        return HttpResponseForbidden("Вы не можете удалить это объявление.")

    if request.method == "POST":
        property_obj.delete()
        return redirect('profile', username=request.user.username)

    return render(request, 'delete_property_confirm.html', {'property': property_obj})


def property_detail(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    return render(request, 'property_detail.html', {'property': property_obj})

