from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

class usuario(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    nome = models.CharField(max_length=200)
    ra = models.IntegerField()

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('usuarios_fbv_user:usuario_edit', kwargs={'pk': self.pk})