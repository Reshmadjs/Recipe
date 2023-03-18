from django.urls import path
from . import views

urlpatterns=[
path('',views.RecipeListView.as_view(),name='recipess-home'),
path('recipe/<int:pk>',views.RecipeDetailView.as_view(),name='recipess-detail'),
path('recipe/create',views.RecipeCreateView.as_view(),name='recipess-create'),
path('recipe/<int:pk>/update',views.RecipeUpdateView.as_view(),name='recipess-update'),
path('recipe/<int:pk>/delete',views.RecipeDeleteView.as_view(),name='recipess-delete'),
path('about/',views.about,name='recipess-about'),

]