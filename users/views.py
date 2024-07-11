from django.views.generic import CreateView, UpdateView, ListView
from users.models import User
from users.forms import UserRegisterForm, UserProfileForm
from django.urls import reverse_lazy, reverse
import secrets
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.shortcuts import render
# from django.contrib.auth.models import User


class UserListView(ListView):
    """Контроллер отображения страницы с сообщениями"""
    model = User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты для завершения регистрации',
            message=f'Для подтверждения почты необходимо перейти по ссылке: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('mailings:mailings_list')

    def get_object(self, queryset=None):
        return self.request.user


def send_message(request):
    return render(request, "users/send_message.html")


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
