from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from blogs.models import Blog
from mailings.forms import FormMixin


class BlogForm(FormMixin, ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class BlogModeratorForm(FormMixin, ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
