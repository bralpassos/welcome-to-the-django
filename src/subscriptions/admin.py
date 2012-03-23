from django.contrib         import admin
from subscriptions.models   import Subscriptions

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'cpf', 'phone', 'email', 'created_at')

admin.site.register(Subscriptions, SubscriptionAdmin)
