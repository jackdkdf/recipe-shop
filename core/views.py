# TODO
# Account system using Google login
# Filters
# Search bar functionality
# Larger logo
# Search filters
# Cart
# Saved recipes
# Ingredients
# Scraper
# Hosting

from typing import Any
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Recipe

# Default list view for all recipes unfiltered
class RecipeListView(ListView):
    model = Recipe
    paginate_by = 15
    template_name = "/core/recipe_list.html"

# Listview with queryset filtered by user's search
class RecipeSearchView(ListView):
    model = Recipe
    paginate_by = 15
    template_name = "/core/recipe_list.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Recipe.objects.filter(name__icontains=query)
        return object_list

class RecipeDetailView(DetailView):
    model = Recipe

class RecipeCreateView(CreateView):
    model = Recipe
    fields = "__all__"
    success_url = reverse_lazy('recipe-list')

class RecipeUpdateView(UpdateView):
    model = Recipe
    fields = "__all__"

class RecipeDeleteView(DeleteView):
    model = Recipe
    success_url = reverse_lazy('recipe-list')

class RecipeSavedView(ListView):
    model = Recipe
    template_name = "/core/recipe_list.html"

class RecipeCartView(ListView):
    model = Recipe
    template_name = "/core/recipe_list.html"


