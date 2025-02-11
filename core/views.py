from django.shortcuts import render, redirect
from core.models import Car


# Create your views here.
def index(request):
    return render(request,"core/index.html")

def home_page(request):
    data = Car.objects.all()
    formatted_data = []
    
    for car in data:
        lakh_price = car.price / 100000  # Convert the price to lakh
        formatted_price = "{:.2f} lakh".format(lakh_price)  # Format the price
        print(formatted_price)
        formatted_data.append({
            'car': car,
            'formatted_price': formatted_price
        })
    
    # Pass only the formatted data to the template
    return render(request, "core/home_page.html", {'formatted_data': formatted_data})


def car_view(request):
    data = Car.objects.all()
    return render(request, "car_view\car_view.html")
