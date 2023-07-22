from django.contrib import admin
from .models import Event, User
# Register your models here.

#admin.site.register(Event)
#admin.site.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'passwd')

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'user') 


admin.site.register(User, UserAdmin)
admin.site.register(Event, EventAdmin)


