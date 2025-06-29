from django.db import models

class Resume(models.Model):
    resume_file = models.FileField(upload_to='resumes/')
    job_description = models.TextField(blank=True, null=True)  # optional to save JD

    def __str__(self):
        return self.resume_file.name
