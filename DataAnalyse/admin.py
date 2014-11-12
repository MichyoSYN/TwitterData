from django.contrib import admin
from DataAnalyse.models import Twitter

# Register your models here.
class TwitterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['text_content']}),
        ('Publish Date', {'fields': ['pub_date']})
    ]
    list_display = ('pub_date', 'event', 'was_published_recently', 'text_content')
    list_filter = ['pub_date', 'event']
    search_fields = ['text_content', 'event']

admin.site.register(Twitter, TwitterAdmin)