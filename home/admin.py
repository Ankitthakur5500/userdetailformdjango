from django.contrib import admin
from .models import *

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "username","address","city","zip")

admin.site.register(Home,MemberAdmin)
