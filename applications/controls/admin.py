from django.contrib import admin

from .models import Exercise, ExerciseRegister, Control

# Register your models here.

admin.site.register(Exercise)
admin.site.register(ExerciseRegister)
admin.site.register(Control)