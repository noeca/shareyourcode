from django.db import models

# Create your models here.


class ptb(models.Model):

    lenguajes = (('Python', 'Python', ), ('Perl', 'Perl',), ('Ruby', 'Ruby',), ('PythonConsole', 'Python Console'), \
        ('RubyConsole', 'Ruby Console'), ('PythonTraceback', 'Python Traceback'), ('HtmlDjango','Django Template'),\
        ('Html', 'Html'), ('Others', 'Others'))

    nombre = models.CharField(max_length=40, null=True, blank=True)
    lenguaje = models.CharField(max_length=20,
                                      choices=lenguajes,
                                      default='Python')
    autor = models.CharField(max_length=40, null=True, blank=True)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    codigo = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.nombre or str(self.id)

    @models.permalink
    def get_absolute_url(self):
        return ('ptb_detalle', [self.id])
        #return ('ptb_listado', [self.id])


