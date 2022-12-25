from django.db import models

class KyrgyzLang(models.Model):
    header = models.CharField(max_length=250)
    content_kg = models.TextField(null=False)

    def __str__(self):
        return self.header



class ModalWindow(models.Model):
    header_modal = models.CharField(max_length=250)
    content_modal = models.TextField(null=False)

    def __str__(self):
        return self.header_modal