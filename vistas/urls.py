from django.urls import path
from . import views

urlpatterns = [
    path('', views.home1),
    #urls Empresas
    path('empresas/', views.home),
    path('RegistrarEmpresa/', views.RegistrarEmpresa),
    path('eliminarEmpresa/<id>', views.eliminarEmpresa),
    path('editarEmpresa/<id>', views.editarEmpresa),
    path('edicionEmpresa/', views.edicionEmpresa),
    
    #urls Desarrolladores
    path('desarrolladores/', views.verDesarrollador),
    path('registrarDesarrollador/', views.registrarDesarrollador),
    path('editarDesarrollador/<id>', views.editarDesarrollador),
    path('edicionDesarrollador/', views.edicionDesarrollador),
    path('eliminarDesarrollador/<id>', views.eliminarDesarrollador),
    
    #urls Contrato
    path('contrato/', views.verContrato),
    path('registrarContrato/', views.registrarContrato),
    path('editarContrato/<id>', views.editarContrato),
    path('edicionContrato/', views.edicionContrato),
    path('eliminarContrato/<id>', views.eliminarContrato),
    
    #urls Videojuegos
    path('videojuegos/', views.verVideojuegos),
    path('registrarVideojuego/', views.registrarVideojuegos),
    path('editarVideojuego/<id>', views.editarVideojuegos),
    path('edicionVideojuego/', views.edicionVideojuegos),
    path('eliminarVideojuego/<id>', views.eliminarVideojuegos),
    
    #urls Usuarios
    path('usuarios/', views.verUsuarios),
    path('registrarUsuario/', views.registrarUsuarios),
    path('editarUsuario/<id>', views.editarUsuarios),
    path('edicionUsuario/', views.edicionUsuarios),
    path('eliminarUsuario/<id>', views.eliminarUsuarios),
    
    #urls Plataformas
    path('plataformas/', views.verPlataformas),
    path('registrarPlataforma/', views.registrarPlataformas),
    path('editarPlataforma/<id>', views.editarPlataformas),
    path('edicionPlataforma/', views.edicionPlataforma),
    path('eliminarPlataforma/<id>', views.eliminarPlataforma),
    
    #urls Clasificacion
    path('clasificacion/', views.verClasificacion),
    path('registrarClasificacion/', views.registrarClasificacion),
    path('editarClasificacion/<id>', views.editarClasificacion),
    path('edicionClasificacion/', views.edicionClasificacion),
    path('eliminarClasificacion/<id>', views.eliminarClasificacion),
    
    #urls Genero
    path('genero/', views.verGenero),
    path('registrarGenero/', views.registrarGenero),
    path('editarGenero/<id>', views.editarGenero),
    path('edicionGenero/', views.edicionGenero),
    path('eliminarGenero/<id>', views.eliminarGenero),
    
    #urls Venta
    path('venta/', views.verVenta),
    path('registrarVenta/', views.registrarVenta),
    path('editarVenta/<id>', views.editarVenta),
    path('edicionVenta/', views.edicionVenta),
    path('eliminarVenta/<id>', views.eliminarVenta),
    
    #urls Tienda
    path('tienda/', views.verTienda),
    path('registrarTienda/', views.registrarTienda),
    path('editarTienda/<id>', views.editarTienda),
    path('edicionTienda/', views.edicionTienda),
    path('eliminarTienda/<id>', views.eliminarTienda),
]
