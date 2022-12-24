from django.contrib import admin
from home.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','name','email','message')


admin.site.register(Contact,ContactAdmin)