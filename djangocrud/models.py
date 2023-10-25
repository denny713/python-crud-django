from django.db import models
import hashlib

# Create your models here.

class Akun(models.Model):
    id = models.IntegerField(primary_key=True, autoincrement=True,default=1)
    username = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    status = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        super(Akun, self).save(*args, **kwargs)