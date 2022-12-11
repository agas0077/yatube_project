from django.contrib import admin
from .models import Post, Group
from typing import Tuple
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display: Tuple[str] = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
    )
    list_editable: Tuple[str] = ('group',)
    search_fields: Tuple[str] = ('text',)
    list_filter: Tuple[str] = (
        'pub_date',
    )
    empty_value_display: str = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
