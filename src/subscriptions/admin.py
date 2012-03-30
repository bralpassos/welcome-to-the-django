# -*- coding: utf-8 -*-

import datetime

from django.conf.urls.defaults  import patterns, url
from django.http                import HttpResponse
from django.contrib             import admin
from django.utils.translation   import ugettext as _
from django.utils.translation   import ungettext

from subscriptions.models       import Subscriptions

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'subscribed_today', 'paid')
    list_filter = ['created_at', 'paid']

    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'phone', 'email', 'created_at')

    actions = ['mark_as_paid']


    # Opção para marcar a inscrição como paga via admin
    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        msg = ungettext(
            u'%(count)d inscrição foi marcada com paga.',
            u'%(count)d inscrições foram marcadas como pagas.',
            count
        ) % {'count': count}

        self.message_user(request, msg)

    mark_as_paid.short_description = _(u'Marcar como paga')

    # Nova coluna que informa se o usúario foi criado hoje ou não
    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.date.today()

    subscribed_today.short_description = u'Inscrito hoje?'
    subscribed_today.boolean = True     # Exibe um ícone ao invés de 'True' ou 'False'


    # Opção para exportar todas as inscrções no formato csv
    def export_subscriptions(self, request):
        subscriptions = self.model.objects.all()
        rows = [','.join([s.name, s.email]) for s in subscriptions]

        response = HttpResponse('\r\n'.join(rows))
        response.mimetype = 'text/csv'
        response['Content-Disposition'] = 'attachment; filename=inscricoes.csv'

        return response


    def get_urls(self):
        original_urls = super(SubscriptionAdmin, self).get_urls()
        extra_url = patterns('',
            url(r'exportar-inscricoes/$',
                self.admin_site.admin_view(self.export_subscriptions),
                name='export_subscriptions'
            )
        )

        return extra_url + original_urls


admin.site.register(Subscriptions, SubscriptionAdmin)
