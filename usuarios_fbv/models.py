from django.db import models
from django.core.urlresolvers import reverse


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    operadora = models.PositiveIntegerField()

class Aluno(Usuario):
    ra = models.IntegerField()
    curso_matriculado = models.CharField(max_length=100)
    status_aluno = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('usuarios_fbv:usuario_edit', kwargs={'pk': self.pk})
