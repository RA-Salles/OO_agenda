from django.contrib import admin
from .models import Event, User, Username, Userpass
# Register your models here.

admin.site.register(Event)
admin.site.register(User)
admin.site.register(Username)
admin.site.register(Userpass)

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'passwd')

class EventAdmin(admin.ModelAdmin):
    list_display = ('Title', 'user')


#admin.site.register(User, UserAdmin)
#admin.site.register(Event, EventAdmin)


