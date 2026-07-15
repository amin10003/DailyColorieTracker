from django.shortcuts import render
from django.db.models import Sum

from .models import Food


def home(request):
    """
    Display all food items and the total calories consumed.
    """

    food_items = Food.objects.all().order_by("-created_at")

    total_calories = (
        Food.objects.aggregate(total=Sum("calories"))["total"] or 0
    )

    context = {
        "food_items": food_items,
        "total_calories": total_calories,
    }

    return render(
        request,
        "home.html",
        context,
    )