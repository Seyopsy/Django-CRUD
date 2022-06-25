from django.contrib import admin
from .models import STATUS_CHOICES, title, slug, author, body, publish, created, updated, status


# Register your models here.
admin.site.register(STATUS_CHOICES)
admin.site.register(title)
admin.site.register(slug)
admin.site.register(author)
admin.site.register(body)
admin.site.register(publish)
admin.site.register(created)
admin.site.register(updated)
admin.site.register(status)