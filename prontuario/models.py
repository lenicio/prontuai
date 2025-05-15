from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Medico(models.Model):
    nome = models.CharField(
        max_length=200,
        help_text='Nome do médico',
        verbose_name='Nome Completo'
    )

    crm = models.CharField(
        max_length=12,
        unique=True,
        help_text='Nº do conselho',
        verbose_name='CRM'
    )

    especialidade = models.CharField(
        choices=[('Cardiologista', 'Cardiologista'),
                 ('Neurologista', 'Neurologista'),
                 ('Pediatra', 'Pediatra')]
    )

    data_nascimento = models.DateField(
        help_text='Ex: 01/01/2000',
        verbose_name='Data de Nascimento'
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
        auto_created=True,
        help_text='Criado Em',
        verbose_name='Criado Em'
    )
    atualizado_em = models.DateField(auto_now=True)

    def clean(self):
        super().clean()
        if (timezone.now().date().year - self.data_nascimento.year) < 18:
            raise ValidationError(f'Você é muito novo para ser médico')

        if len(self.nome) < 5:
            raise ValidationError(f'O nome precisa ter ao menos 5 caracteres.')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médicos'
