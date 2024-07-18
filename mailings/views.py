from random import sample
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from blogs.models import Blog
from mailings.forms import MailingForm, ClientForm, MessageForm, MailingModeratorForm, MailingAttemptForm
from mailings.models import Client, Message, Mailing, MailingAttempt


class MailingListView(LoginRequiredMixin, ListView):
    """Контроллер отображения страницы с расылками"""
    model = Mailing

    # success_url = reverse_lazy("mailing:home")

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

    # def get_form_kwargs(self):
    #     kwargs = super(MailingCreateView, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs

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

    # def get_form_kwargs(self):
    #     kwargs = super(MailingUpdateView, self).get_form_kwargs()
    #     kwargs['user'] = self.request.user
    #     return kwargs

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


class MailingAttemptView(LoginRequiredMixin, ListView):
    """Контроллер для просмотра попыток рассылки"""
    model = MailingAttempt

    form_class = MailingAttemptForm

    def get_queryset(self):
        user_id = self.request.user.id
        mailing_ids = Mailing.objects.all().filter(owner_mailing=user_id).values('id')
        queryset = MailingAttempt.objects.filter(mailing_id__in=mailing_ids)

        return queryset

    def get_context_data(self, *args, **kwargs):
        user_id = self.request.user.id
        mailing_ids = Mailing.objects.all().filter(owner_mailing=user_id).values('id')
        context_data = super().get_context_data(*args, **kwargs)
        context_data['total'] = MailingAttempt.objects.all()
        context_data['total_count'] = MailingAttempt.objects.filter(mailing_id__in=mailing_ids).count()
        context_data['success_count'] = MailingAttempt.objects.filter(mailing_id__in=mailing_ids,
                                                                      status='Отправлено').count()
        context_data['error_count'] = MailingAttempt.objects.filter(mailing_id__in=mailing_ids, status='Ошибка').count()
        return context_data


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


class HomePage(TemplateView):
    """
    Контроллер домашней страницы
    """

    template_name = 'mailings/home.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['mailing_count'] = Mailing.objects.all().count()
        context_data["active_mailing_count"] = Mailing.objects.filter(is_active=True).count()
        context_data["unique_clients_count"] = Client.objects.all().distinct('email').count()
        blogs_list = list(Blog.objects.all())
        context_data['random_blogs'] = sample(blogs_list, min(len(blogs_list), 3))
        return context_data
