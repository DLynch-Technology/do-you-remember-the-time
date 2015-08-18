
from django.contrib import admin
from projects.models import Project


    
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('modified_by','created_by',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

admin.site.register(Project,ProjectAdmin)