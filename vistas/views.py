from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
#Views Empresas
def home1(request):
    return render(request, "home1.html")

def home(request):
    empresas = Empresa.objects.all()
    return render(request, "empresas.html", {"empresas":empresas})

def RegistrarEmpresa(request):
    nombre = request.POST["nombre_empresa"]
    fundacion = request.POST["fundacion"]
    sitio_web = request.POST["sitio_web"]
    pais_origen = request.POST["pais_origen"]
    
    empresas = Empresa.objects.create(
        nombre_empresa=nombre, fundacion=fundacion, sitio_web=sitio_web, pais_origen=pais_origen
    )
    messages.success(request, "Empresa Registrada")
    return redirect("/empresas")

def editarEmpresa(request, id):
    empresa = Empresa.objects.get(id=id)
    return render(request, "editarEmpresa.html", {"empresa": empresa})

def edicionEmpresa(request):
    id = request.POST["id"]
    nombre = request.POST["nombre_empresa"]
    fundacion = request.POST["fundacion"]
    sitio_web = request.POST["sitio_web"]
    pais_origen = request.POST["pais_origen"]
    
    empresa = Empresa.objects.get(id=id)
    empresa.nombre_empresa = nombre
    empresa.fundacion = fundacion
    empresa.sitio_web = sitio_web
    empresa.pais_origen = pais_origen
    empresa.save()
    
    messages.success(request, "Empresa Actualizada")
    return redirect("/empresas")
    
    
def eliminarEmpresa(request, id):

    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    
    messages.success(request, "Empresa Eliminada")
    return redirect("/empresas")

#Views Desarrolladores
def verDesarrollador(request):
    desarrolladores = Desarrollador.objects.all()
    return render(request, "desarrolladores.html", {"desarrolladores":desarrolladores})

def registrarDesarrollador(request):
    nombre_desarrollador = request.POST["nombre_desarrollador"]
    fundacion = request.POST["fundacion"]
    sitio_web = request.POST["sitio_web"]
    pais_origen = request.POST["pais_origen"]
    
    desarrolladores = Desarrollador.objects.create(
        nombre_desarrollador=nombre_desarrollador, fundacion=fundacion, sitio_web=sitio_web, pais_origen=pais_origen
    )
    messages.success(request, "Desarrollador Registrado")
    return redirect("/desarrolladores")

def editarDesarrollador(request, id):
    desarrollador = Desarrollador.objects.get(id=id)
    return render(request, "editarDesarrollador.html", {"desarrollador":desarrollador})

def edicionDesarrollador(request):
    id = request.POST["id"]
    nombre_desarrollador = request.POST["nombre_desarrollador"]
    fundacion = request.POST["fundacion"]
    sitio_web = request.POST["sitio_web"]
    pais_origen = request.POST["pais_origen"]
    
    desarrollador = Desarrollador.objects.get(id=id)
    desarrollador.nombre_desarrollador = nombre_desarrollador
    desarrollador.fundacion = fundacion
    desarrollador.sitio_web = sitio_web
    desarrollador.pais_origen = pais_origen
    desarrollador.save()
    
    messages.success(request, "Desarrollador Actualizado")
    return redirect("/desarrolladores")

def eliminarDesarrollador(request, id):
    desarrollador = Desarrollador.objects.get(id=id)
    desarrollador.delete()
    
    messages.success(request, "Desarrollador Eliminado")
    return redirect("/desarrolladores")

#Views Contrato

def verContrato(request):
    contr = contrato.objects.all()
    return render(request, "contrato.html", {"contrato" :contr})

def registrarContrato(request):
    descripcion_contrato = request.POST["descripcion_contrato"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_limite = request.POST["fecha_limite"]
    desarrolladorid = request.POST["desarrolladorid"]
    empresaid = request.POST["empresaid"]
    
    
    contr = contrato.objects.create(
        descripcion_contrato=descripcion_contrato,
        fecha_inicio=fecha_inicio,
        fecha_limite=fecha_limite,
        desarrollador= Desarrollador.objects.get(id = desarrolladorid),
        empresa= Empresa.objects.get(id = empresaid)
    )
    messages.success(request, "Contrato Registrado")
    return redirect("/contrato")

def editarContrato(request, id):
    contr = contrato.objects.get(id=id)
    return render(request, "editarContrato.html", {"contrato":contr})

def edicionContrato(request):
    id = request.POST["id"]
    descripcion_contrato = request.POST["descripcion_contrato"]
    fecha_inicio = request.POST["fecha_inicio"]
    fecha_limite = request.POST["fecha_limite"]
    desarrolladorid = request.POST["desarrolladorid"]
    empresaid = request.POST["empresaid"]
    
    contr = contrato.objects.get(id=id)
    contr.descripcion_contrato = descripcion_contrato
    contr.fecha_inicio = fecha_inicio
    contr.fecha_limite = fecha_limite
    contr.desarrollador = Desarrollador.objects.get(id = desarrolladorid)
    contr.empresa = Empresa.objects.get(id = empresaid)
    contr.save()
    
    messages.success(request, "Contrato Actualizado")
    return redirect("/contrato")

def eliminarContrato(request, id):
    contr = contrato.objects.get(id=id)
    contr.delete()
    
    messages.success(request, "Contrato Eliminado")
    return redirect("/contrato")

#Views Videojuegos
def verVideojuegos(request):
    videojuego = Videojuegos.objects.all()
    return render(request, "videojuegos.html", {"videojuegos":videojuego})

def registrarVideojuegos(request):
    titulo_videojuego = request.POST["titulo_videojuego"]
    lanzamiento = request.POST["lanzamiento"]
    desarrolladorid = request.POST["desarrolladorid"]
    
    videojuego = Videojuegos.objects.create(
        titulo_videojuego=titulo_videojuego,
        lanzamiento=lanzamiento,
        desarrollador=Desarrollador.objects.get(id = desarrolladorid)
    )
    messages.success(request, "Videojuego Registrado")
    return redirect("/videojuegos")

def editarVideojuegos(request, id):
    videojuego = Videojuegos.objects.get(id=id)
    return render(request, "editarVideojuego.html", {"videojuego":videojuego})

def edicionVideojuegos(request):
    id = request.POST["id"]
    titulo_videojuego = request.POST["titulo_videojuego"]
    lanzamiento = request.POST["lanzamiento"]
    desarrolladorid = request.POST["desarrolladorid"]
    
    videojuego = Videojuegos.objects.get(id=id)
    videojuego.titulo_videojuego = titulo_videojuego
    videojuego.lanzamiento = lanzamiento
    videojuego.desarrollador = Desarrollador.objects.get(id = desarrolladorid)
    videojuego.save()
    
    messages.success(request, "Videojuego Actualizado")
    return redirect("/videojuegos")

def eliminarVideojuegos(request, id):
    videojuego = Videojuegos.objects.get(id=id)
    videojuego.delete()
    
    messages.success(request, "Videojuego Eliminado")
    return redirect("/videojuegos")

#Views Usuarios
def verUsuarios(request):
    usuario = Usuarios.objects.all()
    return render(request, "usuarios.html", {"usuarios":usuario})

def registrarUsuarios(request):
    username = request.POST["username"]
    correo = request.POST["correo"]
    
    usuario = Usuarios.objects.create(
        username=username,
        correo=correo
    )
    messages.success(request, "Usuario Registrado")
    return redirect("/usuarios")

def editarUsuarios(request, id):
    usuario = Usuarios.objects.get(id=id)
    return render(request, "editarUsuario.html", {"usuario":usuario})

def edicionUsuarios(request):
    id = request.POST["id"]
    username = request.POST["username"]
    correo = request.POST["correo"]
    
    usuario = Usuarios.objects.get(id=id)
    usuario.username = username
    usuario.correo = correo
    usuario.save()
    
    messages.success(request, "Usuario Actualizado")
    return redirect("/usuarios")

def eliminarUsuarios(request, id):
    usuario = Usuarios.objects.get(id=id)
    usuario.delete()
    
    messages.success(request, "Usuario Eliminado")
    return redirect("/usuarios")

#Views Plataformas
def verPlataformas(request):
    plataforma = Plataformas.objects.all()
    return render(request, "plataformas.html", {"plataformas":plataforma})

def registrarPlataformas(request):
    nombre_plataforma = request.POST["nombre_plataforma"]
    fabricante = request.POST["fabricante"]
    videojuegoid = request.POST["videojuegoid"]
    usuarioid = request.POST["usuarioid"]
    
    plataforma = Plataformas.objects.create(
        nombre_plataforma=nombre_plataforma,
        fabricante=fabricante,
        videojuego=Videojuegos.objects.get(id=videojuegoid),
        usuarios=Usuarios.objects.get(id = usuarioid)
    )
    messages.success(request, "Plataforma Registrada")
    return redirect('/plataformas')

def editarPlataformas(request, id):
    plataforma = Plataformas.objects.get(id=id)
    return render(request, "editarPlataforma.html", {"plataforma":plataforma})

def edicionPlataforma(request):
    id = request.POST["id"]
    nombre_plataforma = request.POST["nombre_plataforma"]
    fabricante = request.POST["fabricante"]
    videojuegoid = request.POST["videojuegoid"]
    usuarioid = request.POST["usuarioid"]
    
    plataforma = Plataformas.objects.get(id=id)
    plataforma.nombre_plataforma = nombre_plataforma
    plataforma.fabricante = fabricante
    plataforma.videojuego = Videojuegos.objects.get(id = videojuegoid)
    plataforma.usuarios = Usuarios.objects.get(id = usuarioid)
    plataforma.save()
    
    messages.success(request, "Plataforma Actualizada")
    return redirect("/plataformas")

def eliminarPlataforma(request, id):
    plataforma = Plataformas.objects.get(id=id)
    plataforma.delete()
    
    messages.success(request, "Plataforma Eliminada")
    return redirect("/plataformas")

#Views Clasificacion
def verClasificacion(request):
    clasificacion = Clasificacion.objects.all()
    return render(request, "clasificacion.html", {"clasificacion":clasificacion})

def registrarClasificacion(request):
    clasificacion = request.POST["clasificacion"]
    tipo_clasificacion = request.POST["tipo_clasificacion"]
    
    clasif = Clasificacion.objects.create(
        clasificacion=clasificacion,
        tipo_clasificacion=tipo_clasificacion
    )
    messages.success(request, "Clasificacion Registrada")
    return redirect("/clasificacion")

def editarClasificacion(request, id):
    clasificacion = Clasificacion.objects.get(id=id)
    return render(request, "editarClasificacion.html", {"clasificacion":clasificacion})

def edicionClasificacion(request):
    id = request.POST["id"]
    clasificacion = request.POST["clasificacion"]
    tipo_clasificacion = request.POST["tipo_clasificacion"]
    
    clasif = Clasificacion.objects.get(id=id)
    clasif.clasificacion = clasificacion
    clasif.tipo_clasificacion = tipo_clasificacion
    clasif.save()
    
    messages.success(request, "Clasificacion Actualizada")
    return redirect("/clasificacion")

def eliminarClasificacion(request, id):
    clasificacion = Clasificacion.objects.get(id=id)
    clasificacion.delete()
    
    messages.success(request, "Clasificacion Eliminada")
    return redirect("/clasificacion")

#Views Genero
def verGenero(request):
    genero = Genero.objects.all()
    return render(request, "genero.html", {"genero":genero})

def registrarGenero(request):
    nombre_genero = request.POST["nombre_genero"]
    videojuegoid = request.POST["videojuegoid"]
    clasificacionid = request.POST["clasificacionid"]
    
    genero = Genero.objects.create(
        nombre_genero=nombre_genero,
        videojuego=Videojuegos.objects.get(id = videojuegoid),
        clasificacion=Clasificacion.objects.get(id = clasificacionid)
    )
    messages.success(request, "Genero Registrado")
    return redirect("/genero")

def editarGenero(request, id):
    genero = Genero.objects.get(id = id)
    return render(request, "editarGenero.html", {"genero":genero})

def edicionGenero(request):
    id = request.POST["id"]
    nombre_genero = request.POST["nombre_genero"]
    videojuegoid = request.POST["videojuegoid"]
    clasificacionid = request.POST["clasificacionid"]
    
    genero = Genero.objects.get(id = id)
    genero.nombre_genero = nombre_genero
    genero.videojuego = Videojuegos.objects.get(id = videojuegoid)
    genero.clasificacion = Clasificacion.objects.get(id = clasificacionid)
    genero.save()
    
    messages.success(request, "Genero Actualizado")
    return redirect("/genero")

def eliminarGenero(request, id):
    genero = Genero.objects.get(id = id)
    genero.delete()
    
    messages.success(request, "Genero Eliminado")
    return redirect("/genero")

#Views Ventas
def verVenta(request):
    venta = Ventas.objects.all()
    return render(request, "venta.html", {"venta":venta})

def registrarVenta(request):
    precio = request.POST["precio"]
    fecha_venta = request.POST["fecha_venta"]
    
    venta = Ventas.objects.create(
        precio=precio,
        fecha_venta=fecha_venta
    )
    messages.success(request, "Venta Registrada")
    return redirect("/venta")

def editarVenta(request, id):
    venta = Ventas.objects.get(id = id)
    return render(request, "editarVenta.html", {"venta":venta})

def edicionVenta(request):
    id = request.POST["id"]
    precio = request.POST["precio"]
    fecha_venta = request.POST["fecha_venta"]
    
    venta = Ventas.objects.get(id = id)
    venta.precio = precio
    venta.fecha_venta = fecha_venta
    venta.save()
    
    messages.success(request, "Venta Actualizada")
    return redirect("/venta")

def eliminarVenta(request, id):
    venta = Ventas.objects.get(id = id)
    venta.delete()
    
    messages.success(request, "Venta Eliminada")
    return redirect("/venta")

#Views Tiendas
def verTienda(request):
    tienda = Tiendas.objects.all()
    return render(request, "tienda.html", {"tienda":tienda})

def registrarTienda(request):
    nombre_tienda = request.POST["nombre_tienda"]
    videojuegoid = request.POST["videojuegoid"]
    ventaid = request.POST["ventaid"]
    
    tienda = Tiendas.objects.create(
        nombre_tienda=nombre_tienda,
        videojuego=Videojuegos.objects.get(id = videojuegoid),
        venta=Ventas.objects.get(id = ventaid)
    )
    messages.success(request, "Tienda Registrada")
    return redirect("/tienda")

def editarTienda(request, id):
    tienda = Tiendas.objects.get(id = id)
    return render(request, "editarTienda.html", {"tienda":tienda})

def edicionTienda(request):
    id = request.POST["id"]
    nombre_tienda = request.POST["nombre_tienda"]
    videojuegoid = request.POST["videojuegoid"]
    ventaid = request.POST["ventaid"]
    
    tienda = Tiendas.objects.get(id = id)
    tienda.nombre_tienda = nombre_tienda
    tienda.videojuego = Videojuegos.objects.get(id = videojuegoid)
    tienda.venta = Ventas.objects.get(id = ventaid)
    tienda.save()
    
    messages.success(request, "Tienda Actualizada")
    return redirect("/tienda")

def eliminarTienda(request, id):
    tienda = Tiendas.objects.get(id = id)
    tienda.delete()
    
    messages.success(request, "Tienda eliminada")
    return redirect("/tienda")