from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Food Model
    
    """
    list_display = (
        "id",
        "name",
        "calories",
        "created_at",
    )
    
    search_fields = (
        "name",
    )
    
    ordering = (
        "created_at",
    )
    
    