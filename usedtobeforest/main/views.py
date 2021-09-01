from usedtobeforest.main.models import Establishment
from django.shortcuts import render

# Create your views here.
def home(request):
    hotels = Establishment.objects.all()
    return render(request, "main/home.html", {"hotels": hotels})