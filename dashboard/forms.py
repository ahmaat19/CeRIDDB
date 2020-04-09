from django.conf import settings
from django import forms
from .models import Project
from django.forms.widgets import CheckboxSelectMultiple
from django_select2.forms import Select2MultipleWidget
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'starting_date', 'ending_date', 'funding_agency', 'location', 'summary', 'direct_beneficiary', 'file1', 'file1', 'file2', 'file3', 'file4', 'file5', 'project_report', 'assessment_evaluation', 'audit']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Project Title'}),
            'starting_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Project Started Date'}),
            'ending_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Project Ended Date'}),
            'funding_agency': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Funding Agency'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
            'summary': CKEditorWidget(),
            'direct_beneficiary': CKEditorWidget(),
            # 'documents': forms.FileField(widget=forms.FileInput(attrs={'multiple': True})),
            # 'documents': forms.FileInput(attrs={'class': 'form-control-file', 'multiple': True, 'placeholder': 'Direct Beneficiaries'}),
            # 'project_report': forms.Select(),
            'assessment_evaluation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assessment & Evaluation Report'}),
            'audit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Audit'}),
        }