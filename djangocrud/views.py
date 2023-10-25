from django.shortcuts import render, redirect
from .models import Akun
from .forms import UserForm

# Create your views here.

def create_user(request):
    if request.method == 'POST'
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_user')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

def user_list(request):
    users = Akun.objects.all()
    return render(request, 'list_user.html', {'users': users})