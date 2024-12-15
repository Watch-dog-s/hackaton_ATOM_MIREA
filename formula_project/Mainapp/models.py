from django.db import models

# Create your models here.
class Formula(models.Model):
    id_formula = models.AutoField(primary_key=True)
    clean_formula = models.CharField(max_length=300)
    short_description = models.CharField(max_length=200, blank=True)
    meta_inf = models.CharField(max_length=200, blank=True)

    class Meta:
        db_table = 'formula'
        managed = True  # Измените на True, если хотите, чтобы Django управлял таблицей