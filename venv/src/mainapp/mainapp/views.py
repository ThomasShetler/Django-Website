from django.http import HttpResponse
from django.shortcuts import  render
def home(request):
    products = ["Swamp Barries", "Worms", "Eyeballs", "brains","Synthetic Cannibinoids"]
    user = request.user
    context = {
        'products': products,
    }

    return render(request, "home.html", context)