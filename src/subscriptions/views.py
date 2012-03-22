# coding: utf-8

from django.core.mail   import send_mail
from django.http        import HttpResponseRedirect, HttpResponse
from django.shortcuts   import render_to_response, get_object_or_404
from django.template    import RequestContext
from django.conf        import settings

from models             import Subscriptions
from forms              import SubscriptionForm

def subscribe(request):
    form = SubscriptionForm()

    if request.method == 'POST':
        # Se tiver algo para gravar, sobrescreve form
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            subscriptions = form.save()

            # Envia o e-mail de notificação
            send_mail(subject=u'Eventex - Cadastro realizado com sucesso!',
                message=u'Obrigado pela sua inscrição!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[subscriptions.email]
            )

            return HttpResponseRedirect('%i/sucesso/' % subscriptions.pk)


    context = RequestContext(request, {'form' : form})

    return render_to_response('subscriptions/new.html', context)


def success(request, pk):
    subscription = get_object_or_404(Subscriptions, pk=pk)
    context = RequestContext(request, {'subscription': subscription})

    return render_to_response('subscriptions/success.html', context)
