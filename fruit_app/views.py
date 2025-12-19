from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def send_fruits(request):
    fruits = [
        {"name": "Apple", "weight": 100, "color": "red"},
        {"name": "Banana", "weight": 120, "color": "yellow"},
        {"name": "Orange", "weight": 150, "color": "orange"},
        {"name": "Pear", "weight": 130, "color": "green"},
        {"name": "Cherry", "weight": 10, "color": "red"}
    ]
    return render(request, "fruit_app/fruitlist.html", { "fruits": fruits })