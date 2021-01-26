from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AdressForm
from .models import Adress


def index(request):
    adress_list = Adress.objects.all()
    adress_list_dict = {'adress_list' : adress_list}
    return render(request, 'Adress/Listagem.html', adress_list_dict)

def create(request):
    if request.method == 'GET':
        form = AdressForm()
        return render(request, 'Adress/Cadastro.html', {'form':form})
    else:
        form = AdressForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/cadastro')




