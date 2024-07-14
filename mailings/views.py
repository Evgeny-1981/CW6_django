from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from mailings.forms import MailingForm, ClientForm, MessageForm, MailingModeratorForm
from mailings.models import Client, Message, Mailing
from users.models import User


class MailingListView(LoginRequiredMixin, ListView):
    """Контроллер отображения страницы с расылками"""
    model = Mailing

    def get_queryset(self):
        user = self.request.user
        if user.has_perm('mailings.View_any_mailing_lists'):
            return super().get_queryset()
        return super().get_queryset().filter(owner_mailing=user)



class MailingDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """Контроллер для просмотра рассылки"""
    model = Mailing

    def test_func(self):
        user = self.request.user
        mailing = self.get_object()
        if user == mailing.owner_mailing:
            return True
        elif user.has_perm('mailings.View_any_mailing_lists'):
            return True
        return False


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailings_list')

    def get_form_kwargs(self):
        kwargs = super(MailingCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

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

    def get_form_kwargs(self):
        kwargs = super(MailingUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner_mailing:
            return MailingForm
        elif user.has_perm('mailings.Disable_mailing_lists'):
            return MailingModeratorForm
        else:
            raise PermissionDenied


class MailingDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Контроллер для удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy("mailings:mailings_list")

    def test_func(self):
        mailing = self.get_object()
        if self.request.user == mailing.owner_mailing:
            return True
        return False


class ClientListView(LoginRequiredMixin, ListView):
    """Контроллер отображения страницы с клиентами"""
    model = Client


class ClientDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """Контроллер для просмотра клиента"""
    model = Client

    def test_func(self):
        client = self.get_object()
        if self.request.user == client.owner_client:
            return True
        return False


class ClientCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:clients_list')

    def form_valid(self, form):
        """Метод для автоматического привязывания Пользователя к создаваемому Клиенту"""
        # Сохранение формы
        self.object = form.save()
        self.object.owner_client = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailings:clients_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner_client:
            return ClientForm
        else:
            raise PermissionDenied


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Контроллер для удаления клиента"""
    model = Client
    success_url = reverse_lazy('mailings:clients_list')

    def test_func(self):
        client = self.get_object()
        if self.request.user == client.owner_client:
            return True
        return False


class MessageListView(LoginRequiredMixin, ListView):
    """Контроллер отображения страницы с сообщениями"""
    model = Message


class MessageDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """Контроллер для просмотра сообщения"""
    model = Message

    def test_func(self):
        user = self.request.user
        message = self.get_object()
        if user == message.owner_message:
            return True
        elif user.has_perm('users.View_the_list_of_service_users'):
            return True
        return False


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания сообщения"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:messages_list')

    def form_valid(self, form):
        """Метод для автоматического привязывания Пользователя к создаваемому Клиенту"""
        # Сохранение формы
        self.object = form.save()
        self.object.owner_message = self.request.user
        self.object.save()

        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер для редактирования сообщений"""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:messages_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner_message:
            return MessageForm
        else:
            raise PermissionDenied


class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Контроллер для удаления сообщений"""
    model = Message
    success_url = reverse_lazy('mailings:messages_list')

    def test_func(self):
        message = self.get_object()
        if self.request.user == message.owner_message:
            return True
        return False


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


def user_status(request, pk):
    """
    Функция для Модератора по смене активности пользователя.
    """
    status = get_object_or_404(User, pk=pk)
    if status.is_active is True:
        status.is_active = False
    elif status.is_active is False:
        status.is_active = True
    status.save()
    return redirect(reverse("users:users_list"))
