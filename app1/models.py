from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    due_date = models.DateField(null=True , blank=True)
    PRIORITY_CHOICES = [
        ('H','High'),
        ('M','Medium'),
        ('L','Low'),
    ]

    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default='M'
    )
