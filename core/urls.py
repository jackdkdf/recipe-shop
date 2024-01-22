from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import RecipeListView, RecipeCreateView, RecipeDeleteView, RecipeDetailView, RecipeUpdateView, RecipeSavedView, RecipeCartView, RecipeSearchView, RecipeOfTheDayView

urlpatterns = [
    path("recipe/list", RecipeListView.as_view(), name="recipe-list"),
    path("recipe/search", RecipeSearchView.as_view(), name="recipe-search"),
    path("recipe/<int:pk>/detail/", RecipeDetailView.as_view(), name="recipe-detail"),
    path("recipe/add/", RecipeCreateView.as_view(), name="recipe-add"),
    path("recipe/<int:pk>/", RecipeUpdateView.as_view(), name="recipe-update"),
    path("recipe/<int:pk>/delete/", RecipeDeleteView.as_view(), name="recipe-delete"),
    path("recipe/rotd", RecipeOfTheDayView.as_view(), name="recipe-day"),
    path("recipe/saved", RecipeSavedView.as_view(), name="recipe-saved"),
    path("recipe/cart", RecipeCartView.as_view(), name="recipe-cart"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)