from django.shortcuts import render,HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from . import models

# recipes=[
# {
# 	'author':'Dom',
# 	'title':'meatball sub',
# 	'directions':'combine all ingredients',
# 	'date_posted':'May 19,2022'
# },
# {
# 	'author':'Dom',
# 	'title':'Turky sub',
# 	'directions':'combine all ingredients',
# 	'date_posted':'May 16,2022'
# },
# {
# 	'author':'Dom',
# 	'title':'ham and cheese sub',
# 	'directions':'combine all ingredients',
# 	'date_posted':'May 12,2022'
# }
# ]
def home(request):
	recipes=models.Recipe.objects.all()
	context = {
 	'recipes':recipes
	}
	return render(request,"recipess/home.html",context)

class RecipeListView(ListView):
	model=models.Recipe
	template_name='recipess/home.html'
	context_object_name='recipes'

class RecipeDetailView(DetailView):
	model=models.Recipe

class RecipeCreateView(LoginRequiredMixin,CreateView):
	model=models.Recipe
	fields=['title','description']

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
	model=models.Recipe
	fields=['title','description']

	def test_func(self):
		recipe=self.get_object()
		return self.request.user==recipe.author

	def form_valid(self,form):
		form.instance.author=self.request.user
		return super().form_valid(form)

class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
	model=models.Recipe
	success_url=reverse_lazy('recipess-home')

	def test_func(self):
		recipe=self.get_object()
		return self.request.user==recipe.author

	
def about(request):
	    return render(request,"recipess/about.html",{'title':'about us page'})
