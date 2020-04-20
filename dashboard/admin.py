from django.contrib import admin
from .models import Project, NGO

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'created_by', 'updated', 'updated_by')
    search_fields = ('title',)
    fields = ('title', ('starting_date', 'ending_date'), 'funding_agency', 'location', 'summary', 'direct_beneficiary', ('file1', 'file2', 'file3', 'file4', 'file5'), 'project_report', 'assessment_evaluation', 'audit', ('created_by', 'updated_by'),)
    

class NGOAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'created_by', 'updated', 'updated_by')
    search_fields = ('name',)
    fields = ('name', ('created_by', 'updated_by'),)
    # list_filter = ('created',)
    # prepopulated_fields = {'paste':('copy',)}


admin.site.register(Project, ProjectAdmin)
admin.site.register(NGO, NGOAdmin)