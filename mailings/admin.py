from django.contrib import admin
from mailings.models import Client, Message

@admin.register(Client)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'fio', 'comment',)
    list_filter = ('email',)
    search_fields = ('email', 'fio',)

@admin.register(Message)
class UserAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message',)
    list_filter = ('subject',)
    search_fields = ('subject',)
