from django.contrib import admin
from .models import cattler, buyer, seller, contact

# Register your models here.
admin.site.register(cattler)
admin.site.register(contact)
admin.site.register(seller)
admin.site.register(buyer)