#encoding:utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class AlergiasUsuario(models.Model):
    cve_usuario = models.ForeignKey('Usuario', db_column='cve_usuario')
    #no hay llaves primarias compuestas, usaremos el id que nos da django para cada tupla
    alergia = models.CharField(max_length=30)
    class Meta:
        db_table = 'alergias_usuario' #creamos alias

class Alumno(models.Model):
    cve_usuario = models.ForeignKey('Usuario', primary_key=True, db_column='cve_usuario')
    escuela_procedencia = models.CharField(max_length=30)
    promedio_escuela_procedencia = models.FloatField()
    tipo_alumno = models.IntegerField()
    tutor_legal = models.CharField(max_length=25)
    tutor_escolar = models.ForeignKey('Profesor', null=True, db_column='tutor_escolar', blank=True)
    class Meta:
        db_table = 'alumno'

class AlumnoTomaEts(models.Model):
    boleta = models.ForeignKey(Alumno, db_column='boleta')
    cve_materia_ets = models.ForeignKey('ets', db_column='cve_materia_ets',to_field='cve_materia_ets')
    etsturno = models.ForeignKey('Ets', db_column='etsturno',to_field='turno')
    calificacion = models.IntegerField(null=True, blank=True)
    #no hay llaves primarias compuestas, usaremos el id que nos da django para cada tupla
    class Meta:
        db_table = 'alumno_toma_ets'

class Claveshorario(models.Model):
    cve_horario = models.CharField(max_length=2, primary_key=True)
    descripcion_horario = models.CharField(max_length=50)
    class Meta:
        db_table = 'claveshorario'

class Depto(models.Model):
    nombre_depto = models.CharField(max_length=30, primary_key=True)
    ubicacion = models.CharField(max_length=50, blank=True)
    jefe_depto = models.ForeignKey('Profesor', db_column='jefe_depto')
    class Meta:
        db_table = 'depto'

class EmpleadoEscolar(models.Model):
    cve_usuario= models.ForeignKey('Usuario', primary_key=True, db_column='cve_usuario')
    hora_entrada = models.CharField(max_length=5)
    hora_salida = models.CharField(max_length=5)
    grado_estudios = models.IntegerField()
    carrera = models.CharField(max_length=25)
    salario = models.FloatField(null=True, blank=True)
    status = models.IntegerField()
    lab_a_mi_cargo = models.ForeignKey('Laboratorio', null=True, db_column='lab_a_mi_cargo', blank=True)
    class Meta:
        db_table = 'empleado_escolar'

class EnfermedadesUsuario(models.Model):
    cve_usuario = models.ForeignKey('Usuario', db_column='cve_usuario')
    enfermedad = models.CharField(max_length=30)
    #no hay llaves primarias compuestas, usaremos el id que nos da django para cada tupla
    class Meta:
        db_table = 'enfermedades_usuario'

class Ets(models.Model):
    cve_materia_ets = models.ForeignKey('materia', db_column='cve_materia_ets')
    turno = models.CharField(max_length=25)
    dia = models.IntegerField()
    hora = models.CharField(max_length=5)
    evaluador = models.ForeignKey('Profesor', db_column='evaluador')
    class Meta:
        db_table = 'ets'

class EtsAplicarseEnSalon(models.Model):
    cve_materia_ets = models.ForeignKey(Ets, db_column='cve_materia_ets',to_field='cve_materia_ets')
    etsturno = models.ForeignKey(Ets, db_column='etsturno',to_field='turno')
    cve_salon = models.ForeignKey('Salon', db_column='cve_salon')
    class Meta:
        db_table = 'ets_aplicarse_en_salon'

class Grupo(models.Model):
    cve_grupo = models.CharField(max_length=4, primary_key=True)
    salon = models.ForeignKey('Salon', db_column='salon')
    class Meta:
        db_table = 'grupo'

class Laboratorio(models.Model):
    nombre_lab = models.CharField(max_length=30, primary_key=True)
    tipo = models.IntegerField()
    ubicacion = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = 'laboratorio'

class Materia(models.Model):
    cve_materia = models.CharField(max_length=4, primary_key=True)
    nom_materia = models.CharField(max_length=20)
    creditos = models.FloatField()
    plan_estudios = models.CharField(max_length=4)
    tipo = models.IntegerField()
    nivel = models.IntegerField(null=True, blank=True)
    coordinador = models.ForeignKey('Profesor', db_column='coordinador')
    depto = models.ForeignKey('depto', db_column='depto')
    materia_antecedente = models.ForeignKey('self', null=True, db_column='materia_antecedente', blank=True)
    materia_siguiente = models.ForeignKey('self', null=True, db_column='materia_siguiente', blank=True)
    class Meta:
        db_table = 'materia'

class MateriaImpartidaEnGrupo(models.Model):
    cve_materia = models.ForeignKey('materia', db_column='cve_materia')
    grupo = models.ForeignKey('grupo', db_column='grupo')
    cve_horario = models.ForeignKey('claveshorario', db_column='cve_horario')
    #no hay llaves primarias compuestas, usaremos el id que nos da django para cada tupla
    class Meta:
        db_table = 'materia_impartida_en_grupo'

class MateriaImpartidaEnLab(models.Model):
    cve_materia = models.ForeignKey('materia', db_column='cve_materia')
    nombre_lab = models.ForeignKey('laboratorio', db_column='nombre_lab')
    dia = models.IntegerField()
    clave_horario_lab = models.IntegerField()
    class Meta:
        db_table = 'materia_impartida_en_lab'

class Material(models.Model):
    cve_material = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=20)
    cantidad_disponible = models.IntegerField()
    cantidad_no_disponible = models.IntegerField()
    class Meta:
        db_table = 'material'

class Profesor(models.Model):
    cve_usuario = models.ForeignKey('empleado_escolar', primary_key=True, db_column='cve_usuario')
    tipo = models.IntegerField()
    grupo_tutorado = models.ForeignKey('grupo', null=True, db_column='grupo_tutorado', blank=True)
    class Meta:
        db_table = 'profesor'

class ProfesorDaClaseEnGrupo(models.Model):
    cve_prof = models.ForeignKey('profesor', db_column='cve_prof')
    grupo = models.ForeignKey('grupo', db_column='grupo')
    class Meta:
        db_table = 'profesor_da_clase_en_grupo'

class ProfesorImparteMateria(models.Model):
    cve_prof = models.ForeignKey('profesor', db_column='cve_prof')
    cve_materia = models.ForeignKey('materia', db_column='cve_materia')
    class Meta:
        db_table = 'profesor_imparte_materia'

class Salon(models.Model):
    cve_salon = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'salon'

class TelefonoUsuario(models.Model):
    cve_usuario = models.ForeignKey('Usuario', db_column='cve_usuario')
    tel = models.CharField(max_length=30)
    class Meta:
        db_table = 'telefono_usuario'

class Usuario(models.Model):
    cve_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    appat = models.CharField(max_length=50)
    apmat = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    curp = models.CharField(max_length=18)
    email_personal = models.CharField(max_length=50)
    email_institucional = models.CharField(max_length=50, blank=True)
    nss = models.CharField(max_length=20, blank=True)
    ss_institucion = models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=30)
    mun_o_del = models.CharField(max_length=30)
    calle = models.CharField(max_length=20, blank=True)
    colonia = models.CharField(max_length=20, blank=True)
    lt = models.IntegerField(null=True, blank=True)
    num = models.IntegerField(null=True, blank=True)
    mz = models.IntegerField(null=True, blank=True)
    cp = models.IntegerField()
    nacionalidad = models.CharField(max_length=15)
    generos=(('M', 'Masculino'),('F', 'Femenino'))
    sexo = models.CharField(max_length=1, choices=generos)
    tipo_sangre = models.CharField(max_length=15,null=True, blank=True)
    foto=models.ImageField(upload_to='fotos',verbose_name='Foto', blank=True)
    fecha_alta = models.DateField(null=True, blank=True)
    fecha_nac = models.DateField(null=True, blank=True)
    clasificacion = models.IntegerField()

    class Meta:
        db_table = 'usuario'

