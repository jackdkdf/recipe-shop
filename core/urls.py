from django.urls import path

from .views import index, RecipeListView, RecipeCreateView, RecipeDeleteView, RecipeDetailView, RecipeUpdateView, RecipeSavedView, RecipeCartView

urlpatterns = [
    path("", index, name="index"),
    path("recipe/list", RecipeListView.as_view(), name="recipe-list"),
    path("recipe/<int:pk>/detail/", RecipeDetailView.as_view(), name="recipe-detail"),
    path("recipe/add/", RecipeCreateView.as_view(), name="recipe-add"),
    path("recipe/<int:pk>/", RecipeUpdateView.as_view(), name="recipe-update"),
    path("recipe/<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe-delete"),
    path("recipe/saved", RecipeSavedView.as_view(), name="recipe-saved"),
    path("recipe/cart", RecipeCartView.as_view(), name="recipe-cart"),
]