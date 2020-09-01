from django.db import models


# Esta sera para la BBDD de Servicios
class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)

    """ Campo para usar una imagen, requiere instalar 'pillow'
    lo siguiente 'upload_to' especifica la direccion para guardar las imagenes y crea la sub carpeta 'servicio' donde 
    se almacenara el contenido        """
    imagen = models.ImageField(upload_to='Servicios')
    created = models.DateTimeField(auto_now_add=True)  # Para guardar la fecha de creacion de un servicio
    updated = models.DateTimeField(auto_now_add=True)  # Para poner la fecha en que se actualizo el servicio

    class Meta:
        # Esto es para especificar los nombres de la tabla y de los campos, en este caso solo de la tabla
        verbose_name = 'servicio'  # nombre del servicio en la BBDD en singular
        verbose_name_plural = 'Servicios'  # Nombre de la BBDD en plural

    def __str__(self):
        return self.titulo
