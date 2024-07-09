from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from mailings.forms import MailingForm, ClientForm, MessageForm, MailingModeratorForm
from mailings.models import Client, Message, Mailing, MailingAttempt
from users.models import User


# from mailings.services import get_categoryes_list


class MailingListView(LoginRequiredMixin, ListView):
    """Контроллер отображения страницы с расылками"""
    model = Mailing

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset()
    #     user = self.request.user
    #     if user.has_perm('mailings.View_any_mailing_lists'):
    #         queryset = queryset.all()
    #         return queryset
    # else:
    #     queryset = queryset.filter(published=True)
    #     return queryset

    # def get_context_data(self, *args, **kwargs):
    #     """Метод для получения версии продукта и вывода только активной версии"""
    #     context = super().get_context_data(*args, **kwargs)
    #     products = self.get_queryset()
    #     for product in products:
    #         product.version_name = product.version.filter(current_version=True).first()
    #     context["object_list"] = products
    #     return context


class MailingDetailView(LoginRequiredMixin, DetailView):
    """Контроллер для просмотра рассылки"""
    model = Mailing


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailings_list')

    def form_valid(self, form):
        """Метод для автоматического привязывания Пользователя к создаваемой Рассылке"""
        # Сохранение формы
        self.object = form.save()
        self.object.owner_mailing = self.request.user
        self.object.save()

        return super().form_valid(form)



class MailingUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy("mailings:mailings_list")


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy("mailings:mailings_list")


class ClientListView(LoginRequiredMixin, ListView):
    """Контроллер отображения страницы с клиентами"""
    model = Client

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset()
    #     user = self.request.user
    #     if user.has_perm('mailings.View_any_mailing_lists'):
    #         queryset = queryset.all()
    #         return queryset
    # else:
    #     queryset = queryset.filter(published=True)
    #     return queryset

    # def get_context_data(self, *args, **kwargs):
    #     """Метод для получения версии продукта и вывода только активной версии"""
    #     context = super().get_context_data(*args, **kwargs)
    #     products = self.get_queryset()
    #     for product in products:
    #         product.version_name = product.version.filter(current_version=True).first()
    #     context["object_list"] = products
    #     return context


class ClientDetailView(DetailView):
    """Контроллер для просмотра клиента"""
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:clients_list')


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования рассылки"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:clients_list')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления рассылки"""
    model = Client
    success_url = reverse_lazy('mailings:clients_list')


class MessageListView(LoginRequiredMixin, ListView):
    """Контроллер отображения страницы с сообщениями"""
    model = Message

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset()
    #     user = self.request.user
    #     if user.has_perm('mailings.View_any_mailing_lists'):
    #         queryset = queryset.all()
    #         return queryset
    # else:
    #     queryset = queryset.filter(published=True)
    #     return queryset

    # def get_context_data(self, *args, **kwargs):
    #     """Метод для получения версии продукта и вывода только активной версии"""
    #     context = super().get_context_data(*args, **kwargs)
    #     products = self.get_queryset()
    #     for product in products:
    #         product.version_name = product.version.filter(current_version=True).first()
    #     context["object_list"] = products
    #     return context


class MessageDetailView(DetailView):
    """Контроллер для просмотра сообщения"""
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания сообщения"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:messages_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования сообщений"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:messages_list')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    """Контроллер для удаления сообщений"""
    model = Message
    success_url = reverse_lazy('mailings:messages_list')


class UserListView(LoginRequiredMixin, ListView):
    """Контроллер отображения страницы с сообщениями"""
    model = User


class ContactsView(TemplateView):
    template_name = 'mailings/contacts.html'

    def post(self, request):
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        print(f'Имя:{name}, тел.:{phone}, сообщение: {message}')
        return HttpResponseRedirect(self.request.path)


def mailing_status(request, pk):
    """
    Функция для Модератора по смене активности рассылки.
    """
    status = get_object_or_404(Mailing, pk=pk)
    if status.is_active is True:
        status.is_active = False

    elif status.is_active is False:
        status.is_active = True

    status.save()
    return redirect(reverse("mailings:mailings_list"))
