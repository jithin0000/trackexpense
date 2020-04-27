from django.urls import path

from . import views

urlpatterns = [

    path('', views.CategoryListView.as_view(), name='category_list'),
    path('create', views.CategoryCreateView.as_view(), name='category_create'),
    path('detail/<int:pk>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('update/<int:pk>', views.CategoryUpdateView.as_view(), name='category_update'),
    path('all', views.get_all_categories, name='category_json'),
    path('delete/<int:pk>', views.delete_category, name='delete_category'),

]
