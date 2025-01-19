from django.shortcuts import render
from .forms import NewAnimalForm

# Create your views here.
def index(request):
    return render(request, 'shop_animals/shop.html')


def new_animal(request):
    form = NewAnimalForm()
    return render(request, 'shop_animals/forms_add_animal.html', {'form': form})