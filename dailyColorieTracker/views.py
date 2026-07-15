from django.shortcuts import render, redirect
from django.db.models import Sum
from .forms import FoodForm

from .models import Food


def home(request):
    """
    Display all food items and the total calories consumed.
    """

    if request.method == "POST":
        form = FoodForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("home")
    
    else:
        form = FoodForm()

    
    food_items = Food.objects.all().order_by("created_at")
    
    total_calories = (
        Food.objects.aggregate(total=Sum("calories"))["total"] or 0
    )
    
    
    context = {
        "form": form,
        "food_items": food_items,
        "total_calories": total_calories
    }
    
    return render(
        request,
        "home.html",
        context
    )