from django                 import forms
from subscriptions.models   import  Subscriptions

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriptions
        exclude = ('created_at')
