from django.urls import path
from pantryapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/metrics', views.metrics),
    path('api/pantry', views.pantry_collection),
    path('api/pantry/<int:item_id>', views.pantry_item),
    path('api/recipes/suggest', views.suggest_recipes),
    path('api/recipes', views.saved_recipes),
    path('api/recipes/<int:recipe_id>', views.saved_recipe),
    path('api/shopping', views.shopping_collection),
    path('api/shopping/<int:item_id>', views.shopping_item),
]
