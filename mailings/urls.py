from django.urls import path
from django.views.decorators.cache import cache_page

from mailings.apps import MailingsConfig
from mailings.views import MailingListView, MailingDetailView, MailingCreateView

app_name = MailingsConfig.name

urlpatterns = [
    # path('categoryes/', CategoryListView.as_view(), name='categoryes_list'),
    # path('category/create', CategoryCreateView.as_view(), name='category_create'),
    path('', MailingListView.as_view(), name='mailing_list'),
    path('mailings/<int:pk>/', MailingDetailView.as_view(), name='mailing_info'),
    path('mailings/create', MailingCreateView.as_view(), name='mailing_create'),
    # path('mailings/<str:slug>/update/', ProductUpdateView.as_view(), name='product_update'),
    # path('mailings/<str:slug>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    # path('contacts/', cache_page(60)(ContactsView.as_view()), name='contacts'),
    # path('blogs/', BlogListView.as_view(), name='blog_list'),
    # path('blogs/<slug:slug>/', BlogDetailView.as_view(), name='blog_info'),
    # path('blogs/create', BlogCreateView.as_view(), name='blog_create'),
    # path('blogs/<slug:slug>/update/', BlogUpdateView.as_view(), name='blog_update'),
    # path('blogs/<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]
