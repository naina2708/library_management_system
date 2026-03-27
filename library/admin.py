from django.contrib import admin
from .models import Item, Transaction, Profile

admin.site.register(Item)
admin.site.register(Transaction)
admin.site.register(Profile)