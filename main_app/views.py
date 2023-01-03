from django.shortcuts import render, redirect
from .models import Goodboiz, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import FeedingForm
from django.http import HttpResponse

# Create your views here.


def add_feeding(request, goodboiz_id):
  # create a ModelForm instance using the data from the
  # post request (when our form submits from the client to server)
  # request.POST is the contents of the form, when submitted
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # save an instance in memory
    new_feeding = form.save(commit=False)
    # new_feeding.cat_id comes from the model key on Feeding called cat
    # remember the _id is automatically appended to it
    new_feeding.goodboiz_id = goodboiz_id
    new_feeding.save()
    # we always redirect when we change data in the database
    # in this case we added a feeding to a cat
    # cat_id on the left refers to the param in url
    # cats/<int:cat_id>/' for the details
    # cat_id on the right is referring to the actually id, we
    # reusing the cat_id from form submission that is argument to add_feeding
    # function above
  return redirect('detail', gb_id=goodboiz_id)

class GoodboiCreate(CreateView):
    model = Goodboiz

    fields = ['name', 'breed', 'description', 'age']
    

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gb_index(request):
    gb = Goodboiz.objects.all()
    return render(request, 'goodboiz/index.html', { 'gb': gb })

def gb_detail(request, gb_id):
    gb = Goodboiz.objects.get(id=gb_id)
    toys_gb_doesnt_have = Toy.objects.exclude(
        id__in=gb.toys.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'goodboiz/detail.html', {'gbz': gb, 'feeding_form': feeding_form, 'toys': toys_gb_doesnt_have})

class GoodboiUpdate(UpdateView):
    model = Goodboiz

    fields = ['breed', 'description', 'age']

class GoodboiDelete(DeleteView):
    model = Goodboiz
    success_url = '/goodboiz/'


class ToyList(ListView):
    model = Toy


class ToyDetail(DetailView):
    model = Toy


class ToyCreate(CreateView):
    model = Toy
    fields = '__all__'


class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']


class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'


def assoc_toy(request, gb_id, toy_id):
  # Note that you can pass a toy's id instead of the whole object
  Goodboiz.objects.get(id=gb_id).toys.add(toy_id)
  return redirect('detail', gb_id=gb_id)


