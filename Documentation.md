


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