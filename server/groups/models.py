from django.db import models
import uuid

class Groups(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    document = models.CharField(max_length=20)
    address = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)




