from comic.models import Comic
from django.contrib import admin


class ComicAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    fieldsets = [
            (None, { 'fields': ['title', 'image']}),
            ('Metadata', { 'fields': ['slug', 'votes', 'approved', 'created_at']}),
        ]
    list_display = ('title', 'votes', 'approved', 'admin_thumbnail')

admin.site.register(Comic,ComicAdmin)
