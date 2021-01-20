from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.contrib.admin import ModelAdmin


from main.models import Student


class StudentAdmin(ModelAdmin):
    list_display = ('custom_field', 'email', 'birthday')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('-name',)
    readonly_fields = ('name',)

    if not Student.social_url:
        def custom_field(self, instance):
            return "{} {}".format(instance.name, instance.surname)
    else:
        def custom_field(self, instance):
            return format_html('<a href= {0}>{1} {2}</a>',
                mark_safe(instance.social_url),
                instance.name,
                instance.surname,
                )


admin.site.register(Student, StudentAdmin)

