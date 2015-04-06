from django.contrib import admin

from .models import Email, Rule
# Register your models here.

class EmailAdmin(admin.ModelAdmin):
    list_display = ['sender', 'timeStamp']
    search_fields = ('sender','subject','messageId')
    list_filter = ('category', 'sender')

admin.site.register(Email,EmailAdmin)
admin.site.register(Rule)
