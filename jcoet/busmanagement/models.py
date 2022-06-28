from django.db import models

# Create your models here.

class modelname(models.Model):
    fieldname = models.FieldType()

    def __str__(self):
        return self.fieldname