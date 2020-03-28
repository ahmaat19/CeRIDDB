from django.db import models
from multiselectfield import MultiSelectField
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    starting_date = models.DateField()
    ending_date = models.DateField()
    funding_agency = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    summary = RichTextUploadingField()
    direct_beneficiary = RichTextField()
    documents = models.FileField(upload_to='documents')
    project_report_choices = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Annually', 'Annually'),
        ('End Report', 'ER')
    ]
    project_report = MultiSelectField(choices=project_report_choices)
    assessment_evaluation = models.TextField() 
    audit = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title