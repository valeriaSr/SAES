# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AlergiasUsuario(models.Model):
    cve_usuario = models.ForeignKey('Usuario', db_column='cve_usuario')
    alergia = models.CharField(max_length=30L)
    class Meta:
        db_table = 'alergias_usuario'

class Alumno(models.Model):
    cve_usuarioa = models.ForeignKey('Usuario', primary_key=True, db_column='cve_usuarioa')
    escuela_procedencia = models.CharField(max_length=30L)
    promedio_escuela_procedencia = models.FloatField()
    tipo_alumno = models.IntegerField()
    tutor_legal = models.CharField(max_length=25L)
    tutor_escolar = models.ForeignKey('Profesor', null=True, db_column='tutor_escolar', blank=True)
    class Meta:
        db_table = 'alumno'

class AlumnoTomaEts(models.Model):
    boleta = models.ForeignKey(Alumno, db_column='boleta')
    cve_materia_ets = models.ForeignKey('Ets', db_column='cve_materia_ets')
    etsturno = models.ForeignKey('Ets', db_column='etsturno')
    calificacion = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'alumno_toma_ets'

class Claveshorario(models.Model):
    cve_horario = models.CharField(max_length=2L, primary_key=True)
    descripcion_horario = models.CharField(max_length=50L)
    class Meta:
        db_table = 'claveshorario'

class Depto(models.Model):
    nombre_depto = models.CharField(max_length=30L, primary_key=True)
    ubicacion = models.CharField(max_length=50L, blank=True)
    jefe_depto = models.ForeignKey('Profesor', db_column='jefe_depto')
    class Meta:
        db_table = 'depto'

class EmpleadoEscolar(models.Model):
    cve_usuarioee = models.ForeignKey('Usuario', primary_key=True, db_column='cve_usuarioee')
    hora_entrada = models.CharField(max_length=8L)
    hora_salida = models.CharField(max_length=8L)
    grado_estudios = models.IntegerField()
    carrera = models.CharField(max_length=25L)
    salario = models.FloatField(null=True, blank=True)
    status = models.IntegerField()
    lab_a_mi_cargo = models.ForeignKey('Laboratorio', null=True, db_column='lab_a_mi_cargo', blank=True)
    class Meta:
        db_table = 'empleado_escolar'

class EnfermedadesUsuario(models.Model):
    cve_usuario = models.ForeignKey('Usuario', db_column='cve_usuario')
    enfermedad = models.CharField(max_length=30L)
    class Meta:
        db_table = 'enfermedades_usuario'

class Ets(models.Model):
    cve_materia_ets = models.ForeignKey('Materia', db_column='cve_materia_ets')
    turno = models.IntegerField()
    dia = models.IntegerField()
    hora = models.CharField(max_length=8L)
    evaluador = models.ForeignKey('Profesor', db_column='evaluador')
    class Meta:
        db_table = 'ets'

class EtsAplicarseEnSalon(models.Model):
    cve_materia_ets = models.ForeignKey(Ets, db_column='cve_materia_ets')
    etsturno = models.ForeignKey(Ets, db_column='etsturno')
    cve_salon = models.ForeignKey('Salon', db_column='cve_salon')
    class Meta:
        db_table = 'ets_aplicarse_en_salon'

class Grupo(models.Model):
    cve_grupo = models.CharField(max_length=4L, primary_key=True)
    salon = models.ForeignKey('Salon', db_column='salon')
    class Meta:
        db_table = 'grupo'

class Laboratorio(models.Model):
    nombre_lab = models.CharField(max_length=30L, primary_key=True)
    tipo = models.IntegerField()
    ubicacion = models.CharField(max_length=30L, blank=True)
    class Meta:
        db_table = 'laboratorio'

class Materia(models.Model):
    cve_materia = models.CharField(max_length=4L, primary_key=True)
    nom_materia = models.CharField(max_length=20L)
    creditos = models.FloatField()
    plan_estudios = models.CharField(max_length=4L)
    tipo = models.IntegerField()
    nivel = models.IntegerField(null=True, blank=True)
    coordinador = models.ForeignKey('Profesor', db_column='coordinador')
    depto = models.ForeignKey(Depto, db_column='depto')
    materia_antecedente = models.ForeignKey(''self'', null=True, db_column='materia_antecedente', blank=True)
    materia_siguiente = models.ForeignKey(''self'', null=True, db_column='materia_siguiente', blank=True)
    class Meta:
        db_table = 'materia'

class MateriaImpartidaEnGrupo(models.Model):
    cve_materia = models.ForeignKey(Materia, db_column='cve_materia')
    grupo = models.ForeignKey(Grupo, db_column='grupo')
    cve_horario = models.ForeignKey(Claveshorario, db_column='cve_horario')
    class Meta:
        db_table = 'materia_impartida_en_grupo'

class MateriaImpartidaEnLab(models.Model):
    cve_materia = models.ForeignKey(Materia, db_column='cve_materia')
    nombre_lab = models.ForeignKey(Laboratorio, db_column='nombre_lab')
    dia = models.IntegerField()
    clave_horario_lab = models.IntegerField()
    class Meta:
        db_table = 'materia_impartida_en_lab'

class Material(models.Model):
    cve_material = models.CharField(max_length=5L, primary_key=True)
    nombre = models.CharField(max_length=20L)
    cantidad_disponible = models.IntegerField()
    cantidad_no_disponible = models.IntegerField()
    class Meta:
        db_table = 'material'

class Profesor(models.Model):
    cve_usuariop = models.ForeignKey(EmpleadoEscolar, primary_key=True, db_column='cve_usuariop')
    tipo = models.IntegerField()
    grupo_tutorado = models.ForeignKey(Grupo, null=True, db_column='grupo_tutorado', blank=True)
    class Meta:
        db_table = 'profesor'

class ProfesorDaClaseEnGrupo(models.Model):
    cve_prof = models.ForeignKey(Profesor, db_column='cve_prof')
    grupo = models.ForeignKey(Grupo, db_column='grupo')
    class Meta:
        db_table = 'profesor_da_clase_en_grupo'

class ProfesorImparteMateria(models.Model):
    cve_prof = models.ForeignKey(Profesor, db_column='cve_prof')
    cve_materia = models.ForeignKey(Materia, db_column='cve_materia')
    class Meta:
        db_table = 'profesor_imparte_materia'

class Salon(models.Model):
    cve_salon = models.IntegerField(primary_key=True)
    class Meta:
        db_table = 'salon'

class TelefonoUsuario(models.Model):
    cve_usuario = models.ForeignKey('Usuario', db_column='cve_usuario')
    tel = models.CharField(max_length=30L)
    class Meta:
        db_table = 'telefono_usuario'

class Usuario(models.Model):
    cve_usuario = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30L)
    appat = models.CharField(max_length=50L)
    apmat = models.CharField(max_length=50L)
    password = models.CharField(max_length=20L)
    curp = models.CharField(max_length=18L)
    email_personal = models.CharField(max_length=50L)
    email_institucional = models.CharField(max_length=50L, blank=True)
    nss = models.CharField(max_length=20L, blank=True)
    ss_institucion = models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=30L)
    mun_o_del = models.CharField(max_length=30L)
    calle = models.CharField(max_length=20L, blank=True)
    colonia = models.CharField(max_length=20L, blank=True)
    lt = models.IntegerField(null=True, blank=True)
    num = models.IntegerField(null=True, blank=True)
    mz = models.IntegerField(null=True, blank=True)
    cp = models.IntegerField()
    nacionalidad = models.CharField(max_length=15L)
    sexo = models.CharField(max_length=1L)
    tipo_sangre = models.IntegerField(null=True, blank=True)
    foto = models.CharField(max_length=50L, blank=True)
    fecha_alta = models.DateField()
    fecha_nac = models.DateField(null=True, blank=True)
    clasificacion = models.IntegerField()
    class Meta:
        db_table = 'usuario'

