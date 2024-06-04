from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    class Meta:
        abstract = True