from django.shortcuts import render
from django.http import Http404
from .models import Recipe


def index(request):
	recipelist = Recipe.objects.all()
	context = {'recipelist': recipelist}
	
	return render(request, 'recipes/index.html', context)

def detail(request, recipe_id):
	try:
		recipe = Recipe.objects.get(pk=recipe_id)
	except Recipe.DoesNotExist:
		raise Http404("Recipe is not defined")
	return render(request, 'recipes/detail.html', {'recipe': recipe})

