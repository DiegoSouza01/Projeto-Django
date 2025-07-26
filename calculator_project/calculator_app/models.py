from django.db import models
from django.contrib.auth.models import User

class Operation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expression = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.expression} = {self.result}"