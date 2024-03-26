from django.db import models

from applications.users.models import User

# Create your models here.

# create y update at
class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# exercise model   
class Exercise(TimestampedModel):

    exercise = models.CharField('Ejercicio', max_length=100)
    description = models.TextField('Descripcion')

    class Meta:
        verbose_name = 'Ejercicio'
        verbose_name_plural = 'Ejercicios'

    def __str__(self):
        return self.exercise


# Exercise Register
    
class ExerciseRegister(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.DecimalField('Peso', decimal_places=2, max_digits=3)
    repetition = models.IntegerField('Repeticiones')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Registro de ejercicio'
        verbose_name_plural = 'Registro de ejercicios'

    def __str__(self) -> str:
        return f'Ejercicio: {self.exercise} en fecha: {self.created_at}'
    
class Control(TimestampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField('Peso', decimal_places=2, max_digits=3)
    chest = models.DecimalField('Pecho', max_digits=3, decimal_places=2)
    arms = models.DecimalField('Brazos', max_digits=3, decimal_places=2)
    weist = models.DecimalField('Cintura', max_digits=3, decimal_places=2)
    legs = models.DecimalField('Piernas', max_digits=3, decimal_places=2)

    class Meta:
        verbose_name = 'Control'
        verbose_name_plural ='Controles'

    def __str__(self):
        return f'Usuario: {self.user.username} fecha: {self.created_at}'
    

    
