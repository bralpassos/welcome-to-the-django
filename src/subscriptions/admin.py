import datetime

from django.contrib         import admin
from subscriptions.models   import Subscriptions

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at', 'subscribed_today')
    date_hierarchy = 'created_at'
    list_filter = ['created_at']
    search_fields = ('name', 'cpf', 'phone', 'email', 'created_at')

    # Nova coluna que informa se o usúario foi criado hoje ou não
    def subscribed_today(self, obj):
        return obj.created_at.date() == datetime.date.today()

    subscribed_today.short_description = u'Inscrito hoje?'
    subscribed_today.boolean = True     # Exibe um ícone ao invés de 'True' ou 'False'

admin.site.register(Subscriptions, SubscriptionAdmin)
