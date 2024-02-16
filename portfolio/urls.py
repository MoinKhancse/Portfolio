
from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('blog', views.blog, name='blog' ),
    path('single_blog',views.single_blog, name='single_blog')
]