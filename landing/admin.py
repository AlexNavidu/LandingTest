from django.contrib import admin

from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display =[field.name for field in Subscriber._meta.fields]
    # exclude =["email"]
    fields = ["email"]
    list_filter = ["name"]
    search_fields = ["email","name",]

    class Meta:
        models = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)
