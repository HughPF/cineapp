"""Script para cargar datos de ejemplo en CineApp."""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cineapp.settings')
django.setup()

from django.contrib.auth.models import User
from peliculas.models import Genero, Pelicula


def crear_superuser():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin', email='admin@cineapp.com', password='admin1234'
        )
        print('[OK] Superusuario creado: admin / admin1234')
    else:
        print('[--] Superusuario admin ya existe')


def crear_usuarios():
    usuarios = [
        ('alvaro', 'alvaro@cineapp.com', 'cineapp123'),
        ('maria', 'maria@cineapp.com', 'cineapp123'),
    ]
    for username, email, pwd in usuarios:
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, email=email, password=pwd)
            print(f'[OK] Usuario creado: {username} / cineapp123')


def crear_generos():
    generos = [
        ('Drama', 'Películas con fuerte carga emocional'),
        ('Acción', 'Películas con persecuciones, peleas y aventuras'),
        ('Ciencia Ficción', 'Películas de futuro, espacio y tecnología'),
        ('Comedia', 'Películas para reír y divertirse'),
        ('Terror', 'Películas para pasar miedo'),
        ('Animación', 'Películas animadas para todas las edades'),
    ]
    for nombre, desc in generos:
        Genero.objects.get_or_create(nombre=nombre, defaults={'descripcion': desc})
    print(f'[OK] Géneros creados: {Genero.objects.count()}')


def crear_peliculas():
    if Pelicula.objects.exists():
        print('[--] Ya hay películas en la base de datos')
        return

    admin = User.objects.get(username='admin')
    alvaro = User.objects.get(username='alvaro')
    maria = User.objects.get(username='maria')

    drama = Genero.objects.get(nombre='Drama')
    accion = Genero.objects.get(nombre='Acción')
    scifi = Genero.objects.get(nombre='Ciencia Ficción')
    comedia = Genero.objects.get(nombre='Comedia')
    animacion = Genero.objects.get(nombre='Animación')

    peliculas = [
        {
            'titulo': 'El Padrino',
            'director': 'Francis Ford Coppola',
            'sinopsis': 'La historia de la familia Corleone, una de las cinco grandes familias mafiosas de Nueva York. Don Vito Corleone es el patriarca de una familia dedicada al crimen organizado. Su hijo menor, Michael, ha vuelto de la guerra con la idea de mantenerse alejado de los negocios familiares, pero el destino le tiene reservado un papel muy diferente.',
            'anio': 1972, 'duracion': 175, 'genero': drama, 'autor': admin
        },
        {
            'titulo': 'Inception',
            'director': 'Christopher Nolan',
            'sinopsis': 'Dom Cobb es un experto ladrón especializado en el arte de la "extracción": robar valiosos secretos del subconsciente durante el estado onírico. Ahora le ofrecen la posibilidad de recuperar su antigua vida a cambio de realizar una última misión: la "incepción", o sea, implantar una idea en la mente de un objetivo en lugar de robarla.',
            'anio': 2010, 'duracion': 148, 'genero': scifi, 'autor': alvaro
        },
        {
            'titulo': 'Matrix',
            'director': 'Las Wachowski',
            'sinopsis': 'Un programador descubre que la realidad es una simulación generada por máquinas que utilizan a los humanos como fuente de energía. Tras conocer a Morfeo y Trinity, Neo deberá decidir si quiere seguir viviendo en la ilusión o conocer la verdad y luchar por liberar a la humanidad.',
            'anio': 1999, 'duracion': 136, 'genero': scifi, 'autor': alvaro
        },
        {
            'titulo': 'Forrest Gump',
            'director': 'Robert Zemeckis',
            'sinopsis': 'La vida de Forrest Gump, un hombre con un coeficiente intelectual bajo pero con un gran corazón, que vive momentos clave de la historia de Estados Unidos en los años 60 y 70. Su amor incondicional por Jenny le acompañará durante toda su vida.',
            'anio': 1994, 'duracion': 142, 'genero': drama, 'autor': maria
        },
        {
            'titulo': 'Toy Story',
            'director': 'John Lasseter',
            'sinopsis': 'Las aventuras de un grupo de juguetes que cobran vida cuando su dueño no está. Woody, el vaquero favorito de Andy, ve amenazada su posición con la llegada del nuevo juguete: Buzz Lightyear. La primera película totalmente realizada por ordenador.',
            'anio': 1995, 'duracion': 81, 'genero': animacion, 'autor': maria
        },
        {
            'titulo': 'Mad Max: Fury Road',
            'director': 'George Miller',
            'sinopsis': 'En un mundo postapocalíptico, donde el agua y la gasolina son los bienes más preciados, Max se une a Furiosa para huir del tirano Immortan Joe a través del desierto en una espectacular persecución llena de acción y violencia.',
            'anio': 2015, 'duracion': 120, 'genero': accion, 'autor': admin
        },
        {
            'titulo': 'Amélie',
            'director': 'Jean-Pierre Jeunet',
            'sinopsis': 'Amélie es una joven camarera parisina que decide cambiar a mejor la vida de quienes la rodean. A través de pequeños actos de bondad, encuentra el amor y descubre el sentido de su propia existencia. Una comedia romántica con una atmósfera única.',
            'anio': 2001, 'duracion': 122, 'genero': comedia, 'autor': maria
        },
        {
            'titulo': 'Interstellar',
            'director': 'Christopher Nolan',
            'sinopsis': 'En un futuro donde la Tierra se está volviendo inhabitable, un grupo de exploradores debe viajar a través de un agujero de gusano en busca de un nuevo hogar para la humanidad. Una mezcla épica de ciencia, emoción y aventura espacial.',
            'anio': 2014, 'duracion': 169, 'genero': scifi, 'autor': alvaro
        },
    ]

    for p in peliculas:
        Pelicula.objects.create(**p)

    print(f'[OK] {len(peliculas)} películas creadas')


if __name__ == '__main__':
    print('=== Cargando datos de ejemplo en CineApp ===')
    crear_superuser()
    crear_usuarios()
    crear_generos()
    crear_peliculas()
    print('\n=== Listo! ===')
    print('Acceso:')
    print('  - Admin:   admin  / admin1234')
    print('  - Usuario: alvaro / cineapp123')
    print('  - Usuario: maria  / cineapp123')
