from django.contrib import admin

from .models import Expert, Skill


class ExpertAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'full_name', 'slug',
                    'created_date', 'is_staff', 'is_active', 'show_skills', 'about', )
    exclude = ('last_login', 'last_update',)
    list_display_links = ('username', 'full_name',)
    prepopulated_fields = {'slug': ('first_name', 'last_name',)}
    ordering = ('id',)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description',)
    list_display_links = ('title',)
    ordering = ('id',)


# Register your models here.
admin.site.register(Expert, ExpertAdmin)
admin.site.register(Skill, SkillAdmin)
