from django.contrib import admin
from .models import Key, Users, KeyAssignment

admin.site.register(Key)
admin.site.register(Users)
admin.site.register(KeyAssignment)