


## Food Model

The application stores food items in a `Food` model.

Fields:

- name
- calories
- created_at

The model uses `PositiveIntegerField` to ensure calorie values cannot be negative.



## Django Admin

The `Food` model was registered with Django Admin using a custom `ModelAdmin`.

The admin interface provides:

- Food listing
- Search by food name
- Ordering by newest records



### FoodForm

A Django ModelForm was created to allow users to submit food items.

The form contains:

- Food name
- Calories

The form is linked directly to the Food model.


## Home View

The `home` view retrieves all food items ordered by creation date.

It also calculates the total calories using Django's `aggregate()` function with `Sum`.