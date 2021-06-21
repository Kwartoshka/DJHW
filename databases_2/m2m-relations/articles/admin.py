from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag


class ArticleInlineFormset(BaseInlineFormSet):
    def clean(self):


        main_found = False
        for form in self.forms:
            print(form.cleaned_data)
            if not form.cleaned_data:
                pass
            elif form.cleaned_data['is_main'] and not main_found:
                main_found = True
            elif form.cleaned_data['is_main'] and main_found:
                raise ValidationError('Основным может быть только один тег')

        if not main_found:
            raise ValidationError('Нужно указать хотя бы один тег основным')
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # print(form.cleaned_data)
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке

        return super().clean()  # вызываем базовый код переопределяемого метода


# class RelationshipInline(admin.TabularInline):
#     model = Relationship
#     formset = RelationshipInlineFormset
#
#
# @admin.register(Object)
# class ObjectAdmin(admin.ModelAdmin):
#     inlines = [RelationshipInline]


class ArticleInline(admin.TabularInline):
    model = Article.tags.through
    formset = ArticleInlineFormset


class ArticleInlineNoCheck(admin.TabularInline):
    model = Article.tags.through

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]
    exclude = ("tags",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ArticleInlineNoCheck]

    exclude = ("Tags",)

# class RelationshipInline(admin.TabularInline):
#     model = Relationship
#
#
# @admin.register(Object)
# class ObjectAdmin(admin.ModelAdmin):
#     inlines = [RelationshipInline]
