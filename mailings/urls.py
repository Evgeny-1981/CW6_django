from django.urls import path
from django.views.decorators.cache import cache_page

from mailings.apps import MailingsConfig
from mailings.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, \
    ContactsView, ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, MailingAttemptView, \
    mailing_status, HomePage

app_name = MailingsConfig.name

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('mailings/', MailingListView.as_view(), name='mailings_list'),
    path('mailings/<int:pk>/', MailingDetailView.as_view(), name='mailing_info'),
    path('mailings/create', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/<int:pk>/update/', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/<int:pk>/delete/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('attempts/', MailingAttemptView.as_view(), name='attempts_info'),
    path('clients/', ClientListView.as_view(), name='clients_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_info'),
    path('clients/create', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
    path('messages/', MessageListView.as_view(), name='messages_list'),
    path('messages/<int:pk>/', MessageDetailView.as_view(), name='message_info'),
    path('messages/create', MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/update/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete/', MessageDeleteView.as_view(), name='message_delete'),
    path('contacts/', cache_page(60)(ContactsView.as_view()), name='contacts'),
    path("activation/<int:pk>/", mailing_status, name="mailing_status"),

]
