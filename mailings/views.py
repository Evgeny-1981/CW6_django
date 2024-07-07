from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from mailings.forms import MailingForm, MailingModeratorForm
from mailings.models import Client, Message, Mailing, MailingAttempt


# from mailings.services import get_categoryes_list


class MailingListView(ListView):
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


class MailingDetailView(DetailView):
    """Контроллер для просмотра продукта"""
    model = Mailing


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Контроллер для создания рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_list')
