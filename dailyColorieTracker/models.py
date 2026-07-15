from django.db import models

#Regiter your models here

class Food(models.Model):
    """
    Represents a food item and its calorie value.
    """

    name = models.CharField(
        max_length=100,
        help_text="Enter the name of the food item."
    )

    calories = models.PositiveIntegerField(
        help_text="Enter the calorie count."
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        """
        Returns the food name in the admin panel.
        """
        return self.name