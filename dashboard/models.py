from django.db import models
from multiselectfield import MultiSelectField
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.dispatch import receiver
import os


# Create your models here.
class NGO(models.Model):
    name = models.CharField(max_length=100, unique=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_by = models.IntegerField()
    updated_by = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'NGOs'
    

class Project(models.Model):
    title = models.CharField(max_length=100)
    starting_date = models.DateField()
    ending_date = models.DateField()
    funding_agency = models.ForeignKey(NGO, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    summary = RichTextUploadingField()
    direct_beneficiary = RichTextField()
    file1 = models.FileField(upload_to='documents', blank=True, null=True)
    file2 = models.FileField(upload_to='documents', blank=True, null=True)
    file3 = models.FileField(upload_to='documents', blank=True, null=True)
    file4 = models.FileField(upload_to='documents', blank=True, null=True)
    file5 = models.FileField(upload_to='documents', blank=True, null=True)
    project_report_choices = [
        ('Monthly', 'Monthly'),
        ('Quarterly', 'Quarterly'),
        ('Annually', 'Annually'),
        ('End Report', 'End Report')
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



@receiver(models.signals.post_delete, sender=Project)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.file1:
        if os.path.isfile(instance.file1.path):
            os.remove(instance.file1.path)
    elif instance.file2:
        if os.path.isfile(instance.file2.path):
            os.remove(instance.file2.path)
    elif instance.file3:
        if os.path.isfile(instance.file3.path):
            os.remove(instance.file3.path)
    elif instance.file4:
        if os.path.isfile(instance.file4.path):
            os.remove(instance.file4.path)
    elif instance.file5:
        if os.path.isfile(instance.file5.path):
            os.remove(instance.file5.path)

@receiver(models.signals.pre_save, sender=Project)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    # File1
    try:
        old_file1 = sender.objects.get(pk=instance.pk).file1
    except sender.DoesNotExist:
        return False

    new_file1 = instance.file1
    if not old_file1 == new_file1:
        if os.path.isfile(old_file1.path):
            os.remove(old_file1.path)
    
    # File2
    try:
        old_file2 = sender.objects.get(pk=instance.pk).file2
    except sender.DoesNotExist:
        return False

    new_file2 = instance.file2
    if not old_file2 == new_file2:
        if os.path.isfile(old_file2.path):
            os.remove(old_file2.path)
    
    # File3
    try:
        old_file3 = sender.objects.get(pk=instance.pk).file3
    except sender.DoesNotExist:
        return False

    new_file3 = instance.file3
    if not old_file3 == new_file3:
        if os.path.isfile(old_file3.path):
            os.remove(old_file3.path)
    
    # File4
    try:
        old_file4 = sender.objects.get(pk=instance.pk).file4
    except sender.DoesNotExist:
        return False

    new_file4 = instance.file4
    if not old_file4 == new_file4:
        if os.path.isfile(old_file4.path):
            os.remove(old_file4.path)
    
    # File5
    try:
        old_file5 = sender.objects.get(pk=instance.pk).file5
    except sender.DoesNotExist:
        return False

    new_file5 = instance.file5
    if not old_file5 == new_file5:
        if os.path.isfile(old_file5.path):
            os.remove(old_file5.path)