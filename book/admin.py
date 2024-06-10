from django.contrib import admin
from .models import Book, Category
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        error_messages = {
            'name': {
                'unique': "Категория с таким названием уже существует.",
            },
        }


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryForm
    list_display = ('name',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category_name', 'image')

    def category_name(self, obj):
        return obj.category.name

    category_name.short_description = 'Категория'


admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
