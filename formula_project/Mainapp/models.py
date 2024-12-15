from django.db import models

# Create your models here.

class formula(models.Model):
    id_formula = models.AutoField(primary_key=True)
    clean_formula= models.TextField(max_length=300)

    short_description=models.TextField(max_length=200,blank=True)
    meta_inf=models.TextField(max_length=200,blank=True)

    class Meta:
        db_table = 'formula'
        managed = False