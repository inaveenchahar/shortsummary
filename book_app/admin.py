from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import TagModel, BookModel, SuggestionModel


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name', 'tag_added', 'tag_edited')
    prepopulated_fields = {'tag_slug': ('tag_name',)}
    search_fields = ('tag_name',)


admin.site.register(TagModel, TagAdmin)


class BookAdmin(ImportExportModelAdmin):
    list_display = ('book_title', 'book_author', 'book_publish_on', 'publish_status')
    prepopulated_fields = {'book_slug': ('book_title',)}
    search_fields = ('book_author', 'book_title')


admin.site.register(BookModel, BookAdmin)



class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('name',  'email', 'book_name')
    search_fields = ('book_name', 'name', 'email')

admin.site.register(SuggestionModel, SuggestionAdmin)
