from django.db import models

from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    user_id = models.IntegerField(unique=True)
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.username

class Program(models.Model):
    program_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    url = models.URLField()
    handle = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name

class Report(models.Model):
    report_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=300)
    vulnerability_information = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    first_program_activity_at = models.DateTimeField()
    last_program_activity_at = models.DateTimeField()
    state = models.CharField(max_length=50)
    substate = models.CharField(max_length=50)
    severity_rating = models.CharField(max_length=50, null=True, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    reporter = models.ForeignKey(User, related_name='reports_submitted', on_delete=models.CASCADE)
    assignee = models.ForeignKey(User, related_name='reports_assigned', on_delete=models.CASCADE, null=True, blank=True)
    team = models.ForeignKey(User, related_name='reports_team', on_delete=models.CASCADE, null=True, blank=True)
    attachments = ArrayField(models.URLField(), null=True, blank=True)

    def __str__(self):
        return self.title

class Activity(models.Model):
    activity_id = models.IntegerField(unique=True)
    type = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.type} - {self.message}"
