from django.contrib.auth.models import User
from django.db import models


class Business(models.Model):   
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business', null=True)
    business_name = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    cnpj = models.CharField(max_length=20)
    website = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.business_name

class Agenda(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    service = models.TextField(max_length=200)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='agendas')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Schedule(models.Model):
    date = models.DateField()
    time = models.TimeField()
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE, related_name='schedules')
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='business')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.agenda.title} - {self.date} {self.time}"

