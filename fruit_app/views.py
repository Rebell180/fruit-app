from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def send_fruits(request):
    fruits = (
            {
                "name" : "Apple",
                "weight" : "200 gr.",
                "color" : "red"
            },
            {
                "name" : "Orange",
                "weight" : "180 gr.",
                "color" : "orange"
            },
            {
                "name" : "Banana",
                "weight" : "140 gr.",
                "color" : "yellow"
            },
            {
                "name" : "Pineapple",
                "weight" : "600 gr.",
                "color" : "yellow"
            },
            {
                "name" : "Cherry",
                "weight" : "10 gr.",
                "color" : "red"
            }
        )
    return JsonResponse(fruits, safe=False)