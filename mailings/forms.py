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


class MailingForm(FormMixin, ModelForm):
    class Meta:
        model = Mailing
        exclude = ('owner_mailing',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(MailingForm, self).__init__(*args, **kwargs)
        self.fields['message'].queryset = Message.objects.filter(owner_message=user)

        self.fields['clients'].queryset = Client.objects.filter(owner_client=user)


class MailingModeratorForm(FormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = ('is_active',)


class MailingAttemptForm(FormMixin, ModelForm):
    class Meta:
        model = MailingAttempt
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user')
    #     super(MailingAttemptForm, self).__init__(*args, **kwargs)
    #     self.fields['mailing'].queryset = Mailing.objects.filter(owner_mailing=user)
    #
    #     self.fields['clients'].queryset = Client.objects.filter(owner_client=user)
