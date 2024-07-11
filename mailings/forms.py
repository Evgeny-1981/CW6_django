from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from mailings.models import Client, Message, Mailing, MailingAttempt


class FormMixin:
    """Класс для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ClientForm(FormMixin, ModelForm):
    """Класс для создание форм для модели Клиенты"""

    class Meta:
        model = Client
        exclude = ('owner_client',)


class ClientModeratorForm(FormMixin, ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MessageForm(FormMixin, ModelForm):
    """Класс для создание форм для модели Сообщения"""

    class Meta:
        model = Message
        exclude = ('owner_message',)


class MessageModeratorForm(FormMixin, ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

    # def clean_name(self):
    #     """Метод для проверки валидации названия продукта при создании"""
    #     list_words = []
    #     cleaned_data = self.cleaned_data['name']
    #     for word in self.locked_words:
    #         if word in cleaned_data:
    #             list_words.append(word)
    #     result_locked_words = ", ".join(list_words)
    #     if len(result_locked_words) != 0:
    #         raise ValidationError(f'Запрещено использовать в названии слова: {result_locked_words}')
    #     return cleaned_data

    # def clean_description(self):
    #     """Метод для проверки валидации описания продукта при создании"""
    #     list_words = []
    #     cleaned_data = self.cleaned_data['description']
    #     for word in self.locked_words:
    #         if word in cleaned_data:
    #             list_words.append(word)
    #     result_locked_words = ", ".join(list_words)
    #     if len(result_locked_words) != 0:
    #         raise ValidationError(f'Запрещено использовать в описании слова: {result_locked_words}')
    #     return cleaned_data


class MailingForm(FormMixin, ModelForm):
    class Meta:
        model = Mailing
        exclude = ('owner_mailing',)


class MailingModeratorForm(FormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = ('is_active',)


class MailingAttemptForm(FormMixin, ModelForm):
    class Meta:
        model = MailingAttempt
        fields = '__all__'
