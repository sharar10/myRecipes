from django.contrib import admin

from .models import Recipe


class RecipeAdminView(admin.ModelAdmin):
	list_display = ('name', 'cuisine', 'pub_date', 'mod_date')


admin.site.register(Recipe, RecipeAdminView)
