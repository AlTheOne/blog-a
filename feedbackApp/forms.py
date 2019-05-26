from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from feedbackApp.models import FeedBackMessages


phone_validator = RegexValidator(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")

class FeedBackMessagesForm(forms.ModelForm):
    """Form for get and check data send for feedback."""
    class Meta:
        model = FeedBackMessages
        exclude = ('created',)

    name = forms.CharField(
        label='Ваше имя',
        max_length=32,
        required=False,
        help_text='Имя должны быть от 3 до 32 символов \
                    может состоять только из букв и пробела',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ваше имя',
                'class':'modal-input fb_name',
                'pattern':'^[a-zA-Zа-яА-ЯЁё\s]{3,120}$'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email*',
                'id':'reg_id_email',
                'class':'modal-input fb_email',
                'pattern':'^([A-Za-z0-9_\-\.]{4,32})+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$'
            }
        )
    )
    phone = forms.CharField(
        label='Номер телефона',
        required=False,
        max_length=32,
        validators=[phone_validator],
        widget=forms.TextInput(
            attrs={
                'placeholder': '+79273338791',
                'type': 'phone',
                'class':'modal-input fb_phone',
                'pattern':'^[\+]\d{1,2}\d{3}\d{3}\d{2}\d{2}$'
            }
        )
    )
    message = forms.CharField(
        label='Сообщение*',
        required=True,
        max_length=512,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Текст сообщения*',
                'class':'modal-textarea',
            }
        )
    )