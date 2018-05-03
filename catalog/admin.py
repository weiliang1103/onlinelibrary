from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language, Location

# Register your models here.
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Location)

class BookInline(admin.TabularInline):
    model = Book.author.through
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0;
        
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_author', 'display_genre', 'isbn_13')
    inlines = [BookInstanceInline,]
    
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status', 'due_back', 'location')
    list_filter = ('status', 'due_back', 'location')
    fieldsets = (
        (None, {
            'fields': ('id', 'book', 'imprint')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
        ('Location', {
            'fields': ('location',)
        }),
    )
