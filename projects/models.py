from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=50)
    project_code = models.CharField(max_length=6)
    date_start = models.DateField(null=True,blank=True)
    date_expected = models.DateField(null=True,blank=True)
    date_completion = models.DateField(null=True,blank=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    is_live = models.BooleanField(default=False)

    created_time = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, related_name='create',blank=True,null=True)
    modified_time = models.DateTimeField(auto_now = True)
    modified_by = models.ForeignKey(User,related_name='modified',blank=True,null=True)

    def __unicode__(self):
        return self.project_code