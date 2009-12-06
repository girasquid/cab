from django.contrib import admin

from cab.models import Language, Tag, Snippet, Rating, Bookmark

class LanguageAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Language information', {
        'fields': ('name', 'language_code')}),
        ('File type information', {
        'fields': ('file_extension', 'mime_type')}),
        )
    
admin.site.register(Language, LanguageAdmin)
admin.site.register([Tag, Rating, Bookmark])

class SnippetAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Metadata', {
        'fields': ('title', 'language', 'author', 'tag_list', 'original')}),
        ('None', {
         'fields': ('description', 'code')}),
        )
admin.site.register(Snippet, SnippetAdmin)