from django.shortcuts import render
from django.db.models import Sum
from .models import *


# Create your views here.

def home(request):
    
    """
    Display all food items and the total calories consumed
    """
    
    food_items = Food.objects.all().order_by("created_at")
    
    total_calories = (
        Food.objects.aggregate(total=sum("calories"))["total"] or 0
    )
    
    
    context = {
        "food_items": food_items,
        "total_calories": total_calories
    }
    
    return render(
        request,
        "home.html"
        context,
    )
