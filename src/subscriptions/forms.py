from django                     import forms
from django.utils.translation   import ugettext_lazy as _

from subscriptions.validators   import cpfValidator

class SubscriptionForm(forms.Form):
    name  = forms.CharField(label=_('Nome'), max_length=100)
    cpf   = forms.CharField(label=_('CPF'), max_length=11, min_length=11, validators=[cpfValidator])
    email = forms.EmailField(label=_('E-mail'))
    phone = forms.CharField(label=_('Telefone'), required=False, max_length=20)


