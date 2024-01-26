# TODO
# Account system using Google login
# Filters (vegan/vegetarian/omnivore/carnivore)
# Larger logo
# Search filters
# Cart
# Proper pagination
# Detailview
# Recipe of the day
# Saved recipes
# Ingredients
# Scraper
# Hosting
from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.conf import settings

from .models import Recipe

# Default list view for all recipes unfiltered
class RecipeListView(LoginRequiredMixin, ListView):
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

# TODO
class RecipeOfTheDayView(DetailView):
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


