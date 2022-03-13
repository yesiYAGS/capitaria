from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    def __str__(self):
        return f"<Profesor object: {self.nombre} {self.apellido} >"

class Curso(models.Model):
    nombre = models.CharField(max_length=80)
    promedio = models.DecimalField(max_digits=8, decimal_places=2)
    profesor = models.ForeignKey(Profesor,related_name="cursos", on_delete=models.CASCADE)
    def __str__(self):
        return f"<Curso object: {self.nombre} {self.promedio} {self.profesor}>"

class Prueba(models.Model):
    nota = models.DecimalField(max_digits=8, decimal_places=2)
    curso = models.ForeignKey(Curso,related_name="pruebas",on_delete= models.CASCADE)
    def __str__(self):
        return f"<Prueba object: {self.nota} {self.curso}>"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    curso = models.ManyToManyField(Curso,related_name="estudiantes")
    def __str__(self):
        return f"<Estudiante object: {self.nombre} {self.apellido} {self.curso}>"

