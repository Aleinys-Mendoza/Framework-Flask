from app import app
from flask import render_template, request, flash, redirect, url_for, session, jsonify
from mysql.connector.errors import Error


#Importando conexion a BD
from controllers.funciones_empleado import *

PATH_URL = "empleados"#carpeta template/empleados


@app.route('/registrar-empleado', methods=['GET'])
def viewFormEmpleado():
    if 'conectado' in session:
        return render_template(f'{PATH_URL}/form_empleado.html')
    else:
        flash('Primero debes iniciar sesión.','error')
        return redirect(url_for('inicio'))
    

@app.route('/form-registrar-empleado', methods=['POST'])
def formEmpleado():
    if'conectado' in session:
        if 'foto_perfil' in request.files:
            foto_perfil =request.files['foto_perfil']
            resultado = procesar_form_empleado(request.form, foto_perfil)
            if resultado:
                return redirect(url_for('lista_empleados'))
            else:
                flash('El empleado NO fue registrado.','error')
                return render_template(f'{PATH_URL}/form_empleados.html')
            
        else:
            flash('Primero debes iniciar sesion.','error')
            return redirect
        

@app.route('/lista-de-empleados', methods=['GET'])
def lista_empleados():
    if 'conectado' in session:
        return render_template(f'{PATH_URL}/lista_empleados.html', empleados=sql_lista_empleadosBD)
    else:
        flash('Primero debe iniciar sesio. ', 'error')
        return redirect(url_for('inicio'))


@app.route("/detalles-empleados/", methods=['GET'])
@app.route("/detalles-empleados/<int:idEmpleado>", methods=['GET'])
def detalleEmpleado(idEmpleado=None):
    if 'conectado' in session:
       #verificamos si el parametro idEmpleado es None o no esta presente en la URL
        if idEmpleado is None:
          return redirect(url_for('inicio'))
    
    else: 
        flash('Primero debes Iniciar sesion.','error')
        return redirect(url_for('inicio'))
    

#Buscadon de empleados
@app.route("/buscando-empleado", methods=['POST'])
def viewBuscarEmpleadoBD():
    resultadoBusqueda = buscarEmpleadoBD(request.json['busqueda'])
    if resultadoBusqueda:
        return render_template(f'{PATH_URL}/resultado_busqueda_empleado.html', dataBusqueda=resultadoBusqueda)
    else:
        return jsonify({'fin':0})
    

@app.route("/editar-empleado/<int:id>", methods=['GET'])
def viewEditarEmpleado(id):
    if 'conectado' in session:
        respuestaEmpleado = buscarEmpleadoUnico(id)
        if respuestaEmpleado:
            return render_template(f'{PATH_URL}/form_empleado_update.html', respuestaEmpleado=respuestaEmpleado)
        else:
            flash('El empleado no existe.', 'error')
            return redirect(url_for('inicio'))

    else: 
        flash('Primero debes Iniciar sesion.','error')
        return redirect(url_for('inicio'))


#Recibir formulario para actualizar informacion de empelado
@app.route('/actualizar-empleado', methods=['POST'])
def actualizarEmpleado():
    resultData = procesar_actualizacion_form(request)
    if resultData:
        return redirect(url_for('lista_empleados'))
    

@app.route("/lista-de-usuarios", methods=['GET'])
def usuario():
    if 'conectado' in session:
        resp_usuariosBD = lista_usuariosBD()
        return render_template('usuarios/lista_usuarios.html',resp_usuariosBD=resp_usuariosBD)
    else:
        return redirect(url_for('incioCpanel'))


@app.route('/borrar-usuario/<string:id>', methods=['GET'])
def borrarUsuario(id):
    resp = eliminarUsuario(id)
    if resp:
        flash('El usuario fue eliminado correctamente','success')
        return redirect(url_for('usuarios'))
    

@app.route ('/borrar-empelado/<string:id_empleado>/<string:foto_perfil>', methods=['GET'])
def borrarEmpleado(id_empleado, foto_perfil):
    reps= eliminarEmpleado(id_empleado,foto_perfil)
    if reps:
        flash('El empleado fue eliminado correctamente','success')
        return redirect(url_for('lista_empleados'))


@app.route("/descargar-informe-empleados/", methods=['GET'])
def reporteBD():
    if'conectado' in session:
        return generarReporteExcel()
    
    else:
        flash('primero debes iniciar sesion.', 'error')
        return redirect(url_for('inicio'))
