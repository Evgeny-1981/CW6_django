from blogs.apps import BlogConfig
from django.urls import path
from django.views.decorators.cache import cache_page

from blogs.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


app_name = BlogConfig.name

urlpatterns = [
    # path('', HomePage.as_view(), name='home'),
    # path('blogs/', cache_page(60)(BlogListView.as_view()), name='blog_list'),
    path('<slug:slug>/', cache_page(60)(BlogDetailView.as_view()), name='blog_info'),
    path('create', BlogCreateView.as_view(), name='blog_create'),
    path('<slug:slug>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
