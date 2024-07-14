from django.contrib import admin
from mailings.models import Client, Message, Mailing, MailingAttempt


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


@admin.register(Mailing)
class UserAdmin(admin.ModelAdmin):
    list_display = ('start_mailing', 'owner_mailing', 'frequency', 'status', 'is_active',)
    list_filter = ('status',)
    search_fields = ('owner_mailing',)


@admin.register(MailingAttempt)
class UserAdmin(admin.ModelAdmin):
    list_display = ('data_mailing', 'status', 'answer',)
    list_filter = ('status', 'answer', )
    search_fields = ('data_mailing',)
