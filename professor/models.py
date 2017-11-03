from django.db import models
from django.core.urlresolvers import reverse


class professor(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200, verbose_name='Endereço:')
    CIDADE_CHOICES = (
        ('São Paulo', 'São Paulo'),
        ('Americana', 'Americana'),
        ('Araraquara', 'Araraquara'),
        ('Barueri', 'Barueri'),
        ('Bauru', 'Bauru'),
        ('Campinas', 'Campinas'),
        ('Carapicuíba', 'Carapicuíba'),
        ('Cotia', 'Cotia'),
        ('Diadema', 'Diadema'),
        ('Embu das Artes', 'Embu das Artes'),
        ('Franca', 'Franca'),
        ('Guarujá', 'Guarujá'),
        ('Guarulhos', 'Guarulhos'),
        ('Hortolândia', 'Hortolândia'),
        ('Indaiatuba', 'Indaiatuba'),
        ('Itapevi', 'Itapevi'),
        ('Itaquaquecetuba', 'Itaquaquecetuba'),
        ('Jacareí', 'Jacareí'),
        ('Jundiaí', 'Jundiaí'),
        ('Limeira', 'Limeira'),
        ('Marília', 'Marília'),
        ('Mauá', 'Mauá'),
        ('Mogi das Cruzes', 'Mogi das Cruzes'),
        ('Osasco', 'Osasco'),
        ('Piracicaba', 'Piracicaba'),
        ('Praia Grande', 'Praia Grande'),
        ('Presidente Prudente', 'Presidente Prudente'),
        ('Ribeirão Preto', 'Ribeirão Preto'),
        ('Santo André', 'Santo André'),
        ('Santos', 'Santos'),
        ('Sorocaba', 'Sorocaba'),
        ('Sumaré', 'Sumaré'),
        ('Suzano', 'Suzano'),
        ('São Bernardo do Campo', 'São Bernardo do Campo'),
        ('São Carlos', 'São Carlos'),
        ('São José do Rio Preto', 'São José do Rio Preto'),
        ('São José dos Campos', 'São José dos Campos'),
        ('São Vicente', 'São Vicente'),
        ('Taboão da Serra', 'Taboão da Serra'),
        ('Taubaté', 'Taubaté')
    )
    cidade = models.CharField(max_length=100, verbose_name='Cidade:', choices = CIDADE_CHOICES)
    ESTADO_CHOICES = (
        ('SP', 'SP'),
        ('RJ', 'RJ')
    )
    estado = models.CharField(max_length=10, verbose_name='Estado:', choices = ESTADO_CHOICES)
    telefone = models.CharField(max_length=15, verbose_name='Telefone:')
    materia = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('professor:professor_edit', kwargs={'pk': self.pk})
