from django import forms
from django.contrib import admin
from projects.models import Project,Time


    
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('modified_by','created_by',)

    def save_model(self, request, obj, form, change):
        obj.modified_by = request.user
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

admin.site.register(Project,ProjectAdmin)

class TimeForm(forms.ModelForm):
    def clean(self):
        endtime = self.cleaned_data.get('end_time', 0)
        starttime = self.cleaned_data.get('start_time', 0)

        if not endtime or not starttime:
            raise forms.ValidationError('both times are required')
        if endtime < starttime:
            raise forms.ValidationError('endtime must be later than starttime')
class TimeAdmin(admin.ModelAdmin):
    form = TimeForm

admin.site.register(Time,TimeAdmin)