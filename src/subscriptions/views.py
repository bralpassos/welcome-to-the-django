from django.http        import HttpResponseRedirect, HttpResponse
from django.shortcuts   import render_to_response
from django.template    import RequestContext
from forms              import SubscriptionForm

def subscribe(request):
    form = SubscriptionForm()

    if request.method == 'POST':
        # Se tiver algo para gravar, sobrescreve form
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            subscriptions = form.save()

            return HttpResponseRedirect('%i/sucesso/' % subscriptions.pk)


    context = RequestContext(request, {'form' : form})

    return render_to_response('subscriptions/new.html', context)


def success(request):
    return HttpResponse('Sucesso!')
