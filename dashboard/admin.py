from django.contrib import admin
from .models import Project, NGO

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'created_by', 'updated', 'updated_by')
    

class NGOAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'created_by', 'updated', 'updated_by')
    search_fields = ('name',)
    # list_filter = ('created',)
    # prepopulated_fields = {'paste':('copy',)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(NGO, NGOAdmin)