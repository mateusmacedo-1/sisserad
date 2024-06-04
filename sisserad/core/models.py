from django.db import models


# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, related_name='%(class)s_created_by', null=True, blank=True)
    updated_by = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING, related_name='%(class)s_updated_by', null=True, blank=True)
    class Meta:
        abstract = True