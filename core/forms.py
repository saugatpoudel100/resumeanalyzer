from django import forms
from .models import Resume

class ResumeForm(forms.ModelForm):
    job_description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'placeholder': 'Paste job description here...'}),
        required=False,
        label='Job Description'
    )

    class Meta:
        model = Resume
        fields = ['resume_file', 'job_description']
