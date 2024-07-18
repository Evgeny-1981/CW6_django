from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from blogs.forms import BlogForm, BlogModeratorForm
from blogs.models import Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_views += 1
        self.object.save()
        return self.object


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(published=True)
        return queryset


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('mailings:home')

    def get_form_class(self):
        user = self.request.user
        if user.is_staff:
            return BlogModeratorForm
        else:
            raise PermissionDenied

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogModeratorForm

    def get_form_class(self):
        user = self.request.user
        if user.is_staff:
            return BlogModeratorForm
        else:
            raise PermissionDenied

    def get_success_url(self):
        return reverse('blogs:blog_info', args=[self.kwargs.get('slug')])


class BlogDeleteView(DeleteView):
    model = Blog

    def get_form_class(self):
        user = self.request.user
        if user.is_staff:
            return BlogModeratorForm
        else:
            raise PermissionDenied
