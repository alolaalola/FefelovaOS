from django.contrib import admin
from main.models import Project, News, Review
from .models import ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title',)
    list_filter = ('date',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'date', 'is_approved')
    list_filter = ('date', 'is_approved')
    search_fields = ('author', 'content')


admin.site.register(ContactMessage)