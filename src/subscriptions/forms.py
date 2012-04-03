# -*- coding: utf-8 -*-

from django                     import forms
from django.utils.translation   import ugettext_lazy as _

from subscriptions.models       import Subscription
from subscriptions.validators   import cpfValidator

class SubscriptionForm(forms.Form):

    class Meta:
        model = Subscription
        exclude = ('created_at', 'paid')

    name  = forms.CharField(label=_('Nome'), max_length=100)
    cpf   = forms.CharField(label=_('CPF'), max_length=11, min_length=11, validators=[cpfValidator])
    email = forms.EmailField(label=_('E-mail'))
    phone = forms.CharField(label=_('Telefone'), required=False, max_length=20)


    def clean_cpf(self):
        try :
            s = Subscription.objects.get(cpf=self.cleaned_data['cpf'])
        except Subscription.DoesNotExist :
            return self.cleaned_data['cpf']
        raise forms.ValidationError(_(u'Este CPF já está inscrito'))

