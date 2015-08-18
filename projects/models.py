from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=50)
    project_code = models.CharField(max_length=6)
    goals = models.TextField(null=True,blank=True)
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

class Time(models.Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey(Project)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    work_type_register = (
        ('PM', 'Project Manager'),
        ('DEV', 'Development'),
        ('IT', 'IT'),
        ('SERVER', 'Server Admin'),
        ('GFX', 'Graphic Design'),
        ('DEV_LEAD', 'LEAD Development'),
    )
    work_type = models.CharField(max_length=25, choices=work_type_register)
    notes = models.TextField()

    created_time = models.DateTimeField(auto_now_add = True)
    modified_time = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return "%s | %s | %s" % (self.project.project_code,self.work_type, self.notes)