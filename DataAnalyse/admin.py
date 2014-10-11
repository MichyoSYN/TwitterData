from django.contrib import admin
from DataAnalyse.models import Twitter

# Register your models here.
class TwitterAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['text_content']}),
        ('Publish Date', {'fields': ['pub_date']})
    ]
    list_display = ('text_content', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['text_content']

admin.site.register(Twitter, TwitterAdmin)