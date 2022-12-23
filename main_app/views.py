from django.shortcuts import render
from .models import Goodboiz
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class GoodboiCreate(CreateView):
    model = Goodboiz

    fields = '__all__'
    

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gb_index(request):
    gb = Goodboiz.objects.all()
    return render(request, 'goodboiz/index.html', { 'gb': gb })

def gb_detail(request, gb_id):
    gb = Goodboiz.objects.get(id=gb_id)
    return render(request, 'goodboiz/detail.html', {'gbz': gb})