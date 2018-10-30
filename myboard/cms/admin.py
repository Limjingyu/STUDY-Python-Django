from django.contrib import admin
from cms.models import Book, Impression

# Register your models here.

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'publisher', 'price',)
    list_display_links = ('id', 'name',)

class ImpressionAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    raw_id_fields = ('book',)

admin.site.register(Book, BookAdmin)
admin.site.register(Impression, ImpressionAdmin)
