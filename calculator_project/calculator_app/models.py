from django.db import models
from django.contrib.auth.models import User

class Operation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parametros = models.CharField(max_length=200, default="")
    resultado = models.CharField(max_length=200, default="0")
    dt_inclusao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parametros} = {self.resultado}"