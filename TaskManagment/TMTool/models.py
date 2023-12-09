from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Тема которую изучает юзер"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    last_accessed = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.text}")
    
    def delete_topic(self):
        self.delete()

class Entry(models.Model):

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('status1', 'created'),
        ('status2', 'In progress'),
        ('status3', 'suspended'),
        ('status4', 'done'),
    )
    flag_status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='status1')
    

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return (f"{self.text[:50]}...",
                self.flag_status)
    
    def delete_entry(self):
        self.delete()