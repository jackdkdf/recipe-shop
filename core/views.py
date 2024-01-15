from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Recipe

# Create your views here.
def index(request):
    return HttpResponse("Testing")

class RecipeListView(ListView):
    model = Recipe
    template_name = "/core/recipe_list.html"

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


