from django.urls import path
from . import views

urlpatterns = [
    path('first_blog/', views.first_blog, name='blog_one'),
    path('second_blog/', views.second_blog, name='blog_two'),
    path('third_blog/', views.third_blog),
    path('search/', views.search_view, name='search'),
    path('', views.blog, name='home_page'),
    path('blog_list/<int:id>/', views.blog_detail),
]