from django.contrib import admin
from .models import Member, Mindmap, Document
# Register your models here.

admin.site.register(Member)
admin.site.register(Mindmap)
admin.site.register(Document)