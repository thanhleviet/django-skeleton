from django.contrib import admin

from models import *


# Widget


class WidgetAdmin(core_models.ModelAdmin):
    list_display = ['title', 'related_page_names']

    def related_page_names(self, obj):
        return ",\n".join([page.title for page in obj.page_set.all()])


# Page


class PageAdmin(core_models.ModelAdmin):
    list_filter = ['status', ]
    list_display = ['slug', 'title', 'related_widget_names', 'status']

    def related_widget_names(self, obj):
        return ",\n".join([widget.title for widget in obj.widgets.all()])


# Category


class CategoryAdmin(core_models.ModelAdmin):
    list_display = ['slug', 'title', 'related_post_names']

    def related_post_names(self, obj):
        return ",\n".join([post.title for post in obj.post_set.all()])


# Post


class PostAdmin(core_models.ModelAdmin):
    list_filter = ['status', ]
    list_display = ['slug', 'title', 'short_content', 'related_category_names', 'status']

    def related_category_names(self, obj):
        return ",\n".join([category.title for category in obj.categories.all()])


# Slider


class SlideInline(admin.StackedInline):
    model = Slide
    extra = 1


class SliderAdmin(core_models.ModelAdmin):
    list_display = ['title', 'status']
    inlines = [SlideInline, ]


# Subscriber


class SubscriberAdmin(core_models.ModelAdmin):
    list_display = ['name', 'email']


admin.site.register(Widget, WidgetAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Slider, SliderAdmin)
admin.site.register(Subscriber, SubscriberAdmin)

