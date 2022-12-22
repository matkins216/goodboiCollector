from django.shortcuts import render

# Create your views here.


class goodbz:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age


goodboiz = [
    goodbz('Bear', 'poodle', "can't hold his licker", 13),
    goodbz('Rajah', 'besenji', 'the distinguished gentleman', 5),
    goodbz('Pippin', 'undetermined', 'cutest damn dog', 3),
]



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gb_index(request):
    return render(request, 'goodboiz/index.html', { 'gb': goodboiz })