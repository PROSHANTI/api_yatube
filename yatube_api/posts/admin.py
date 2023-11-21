from django.contrib import admin

from .models import Comment, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'group',
        'pub_date',
    )
    search_fields = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'post',
        'text',
    )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'description',
    )


admin.site.empty_value_display = 'Не задано'
