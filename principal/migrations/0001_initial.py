# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AlergiasUsuario'
        db.create_table(u'alergias_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Usuario'], db_column=u'cve_usuario')),
            ('alergia', self.gf('django.db.models.fields.CharField')(max_length=30L)),
        ))
        db.send_create_signal(u'principal', ['AlergiasUsuario'])

        # Adding model 'Alumno'
        db.create_table(u'alumno', (
            ('cve_usuarioa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Usuario'], primary_key=True, db_column=u'cve_usuarioa')),
            ('escuela_procedencia', self.gf('django.db.models.fields.CharField')(max_length=30L)),
            ('promedio_escuela_procedencia', self.gf('django.db.models.fields.FloatField')()),
            ('tipo_alumno', self.gf('django.db.models.fields.IntegerField')()),
            ('tutor_legal', self.gf('django.db.models.fields.CharField')(max_length=25L)),
            ('tutor_escolar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'], null=True, db_column=u'tutor_escolar', blank=True)),
        ))
        db.send_create_signal(u'principal', ['Alumno'])

        # Adding model 'AlumnoTomaEts'
        db.create_table(u'alumno_toma_ets', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('boleta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Alumno'], db_column=u'boleta')),
            ('cve_materia_ets', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'materia_ets_alumno', db_column=u'cve_materia_ets', to=orm['principal.Ets'])),
            ('etsturno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Ets'], db_column=u'etsturno')),
            ('calificacion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'principal', ['AlumnoTomaEts'])

        # Adding model 'Claveshorario'
        db.create_table(u'claveshorario', (
            ('cve_horario', self.gf('django.db.models.fields.CharField')(max_length=2L, primary_key=True)),
            ('descripcion_horario', self.gf('django.db.models.fields.CharField')(max_length=50L)),
        ))
        db.send_create_signal(u'principal', ['Claveshorario'])

        # Adding model 'Depto'
        db.create_table(u'depto', (
            ('nombre_depto', self.gf('django.db.models.fields.CharField')(max_length=30L, primary_key=True)),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('jefe_depto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'], db_column=u'jefe_depto')),
        ))
        db.send_create_signal(u'principal', ['Depto'])

        # Adding model 'EmpleadoEscolar'
        db.create_table(u'empleado_escolar', (
            ('cve_usuarioee', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Usuario'], primary_key=True, db_column=u'cve_usuarioee')),
            ('hora_entrada', self.gf('django.db.models.fields.CharField')(max_length=8L)),
            ('hora_salida', self.gf('django.db.models.fields.CharField')(max_length=8L)),
            ('grado_estudios', self.gf('django.db.models.fields.IntegerField')()),
            ('carrera', self.gf('django.db.models.fields.CharField')(max_length=25L)),
            ('salario', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.IntegerField')()),
            ('lab_a_mi_cargo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Laboratorio'], null=True, db_column=u'lab_a_mi_cargo', blank=True)),
        ))
        db.send_create_signal(u'principal', ['EmpleadoEscolar'])

        # Adding model 'EnfermedadesUsuario'
        db.create_table(u'enfermedades_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Usuario'], db_column=u'cve_usuario')),
            ('enfermedad', self.gf('django.db.models.fields.CharField')(max_length=30L)),
        ))
        db.send_create_signal(u'principal', ['EnfermedadesUsuario'])

        # Adding model 'Ets'
        db.create_table(u'ets', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_materia_ets', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Materia'], db_column=u'cve_materia_ets')),
            ('turno', self.gf('django.db.models.fields.IntegerField')()),
            ('dia', self.gf('django.db.models.fields.IntegerField')()),
            ('hora', self.gf('django.db.models.fields.CharField')(max_length=8L)),
            ('evaluador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'], db_column=u'evaluador')),
        ))
        db.send_create_signal(u'principal', ['Ets'])

        # Adding model 'EtsAplicarseEnSalon'
        db.create_table(u'ets_aplicarse_en_salon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_materia_ets', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'materia_ets_salon', db_column=u'cve_materia_ets', to=orm['principal.Ets'])),
            ('etsturno', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Ets'], db_column=u'etsturno')),
            ('cve_salon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Salon'], db_column=u'cve_salon')),
        ))
        db.send_create_signal(u'principal', ['EtsAplicarseEnSalon'])

        # Adding model 'Grupo'
        db.create_table(u'grupo', (
            ('cve_grupo', self.gf('django.db.models.fields.CharField')(max_length=4L, primary_key=True)),
            ('salon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Salon'], db_column=u'salon')),
        ))
        db.send_create_signal(u'principal', ['Grupo'])

        # Adding model 'Laboratorio'
        db.create_table(u'laboratorio', (
            ('nombre_lab', self.gf('django.db.models.fields.CharField')(max_length=30L, primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('ubicacion', self.gf('django.db.models.fields.CharField')(max_length=30L, blank=True)),
        ))
        db.send_create_signal(u'principal', ['Laboratorio'])

        # Adding model 'Materia'
        db.create_table(u'materia', (
            ('cve_materia', self.gf('django.db.models.fields.CharField')(max_length=4L, primary_key=True)),
            ('nom_materia', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('creditos', self.gf('django.db.models.fields.FloatField')()),
            ('plan_estudios', self.gf('django.db.models.fields.CharField')(max_length=4L)),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('nivel', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('coordinador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'], db_column=u'coordinador')),
            ('depto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Depto'], db_column=u'depto')),
            ('materia_antecedente', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'materia_materia_antecedente', null=True, db_column=u'materia_antecedente', to=orm['principal.Materia'])),
            ('materia_siguiente', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'materia_materia_siguiente', null=True, db_column=u'materia_siguiente', to=orm['principal.Materia'])),
        ))
        db.send_create_signal(u'principal', ['Materia'])

        # Adding model 'MateriaImpartidaEnGrupo'
        db.create_table(u'materia_impartida_en_grupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Materia'], db_column=u'cve_materia')),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Grupo'], db_column=u'grupo')),
            ('cve_horario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Claveshorario'], db_column=u'cve_horario')),
        ))
        db.send_create_signal(u'principal', ['MateriaImpartidaEnGrupo'])

        # Adding model 'MateriaImpartidaEnLab'
        db.create_table(u'materia_impartida_en_lab', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Materia'], db_column=u'cve_materia')),
            ('nombre_lab', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Laboratorio'], db_column=u'nombre_lab')),
            ('dia', self.gf('django.db.models.fields.IntegerField')()),
            ('clave_horario_lab', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'principal', ['MateriaImpartidaEnLab'])

        # Adding model 'Material'
        db.create_table(u'material', (
            ('cve_material', self.gf('django.db.models.fields.CharField')(max_length=5L, primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('cantidad_disponible', self.gf('django.db.models.fields.IntegerField')()),
            ('cantidad_no_disponible', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'principal', ['Material'])

        # Adding model 'Profesor'
        db.create_table(u'profesor', (
            ('cve_usuariop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.EmpleadoEscolar'], primary_key=True, db_column=u'cve_usuariop')),
            ('tipo', self.gf('django.db.models.fields.IntegerField')()),
            ('grupo_tutorado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Grupo'], null=True, db_column=u'grupo_tutorado', blank=True)),
        ))
        db.send_create_signal(u'principal', ['Profesor'])

        # Adding model 'ProfesorDaClaseEnGrupo'
        db.create_table(u'profesor_da_clase_en_grupo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_prof', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'], db_column=u'cve_prof')),
            ('grupo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Grupo'], db_column=u'grupo')),
        ))
        db.send_create_signal(u'principal', ['ProfesorDaClaseEnGrupo'])

        # Adding model 'ProfesorImparteMateria'
        db.create_table(u'profesor_imparte_materia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_prof', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Profesor'], db_column=u'cve_prof')),
            ('cve_materia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Materia'], db_column=u'cve_materia')),
        ))
        db.send_create_signal(u'principal', ['ProfesorImparteMateria'])

        # Adding model 'Salon'
        db.create_table(u'salon', (
            ('cve_salon', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
        ))
        db.send_create_signal(u'principal', ['Salon'])

        # Adding model 'TelefonoUsuario'
        db.create_table(u'telefono_usuario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cve_usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['principal.Usuario'], db_column=u'cve_usuario')),
            ('tel', self.gf('django.db.models.fields.CharField')(max_length=30L)),
        ))
        db.send_create_signal(u'principal', ['TelefonoUsuario'])

        # Adding model 'Usuario'
        db.create_table(u'usuario', (
            ('cve_usuario', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=30L)),
            ('appat', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('apmat', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=20L)),
            ('curp', self.gf('django.db.models.fields.CharField')(max_length=18L)),
            ('email_personal', self.gf('django.db.models.fields.CharField')(max_length=50L)),
            ('email_institucional', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('nss', self.gf('django.db.models.fields.CharField')(max_length=20L, blank=True)),
            ('ss_institucion', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('estado', self.gf('django.db.models.fields.CharField')(max_length=30L)),
            ('mun_o_del', self.gf('django.db.models.fields.CharField')(max_length=30L)),
            ('calle', self.gf('django.db.models.fields.CharField')(max_length=20L, blank=True)),
            ('colonia', self.gf('django.db.models.fields.CharField')(max_length=20L, blank=True)),
            ('lt', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('num', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('mz', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('cp', self.gf('django.db.models.fields.IntegerField')()),
            ('nacionalidad', self.gf('django.db.models.fields.CharField')(max_length=15L)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1L)),
            ('tipo_sangre', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('foto', self.gf('django.db.models.fields.CharField')(max_length=50L, blank=True)),
            ('fecha_alta', self.gf('django.db.models.fields.DateField')()),
            ('fecha_nac', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('clasificacion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'principal', ['Usuario'])


    def backwards(self, orm):
        # Deleting model 'AlergiasUsuario'
        db.delete_table(u'alergias_usuario')

        # Deleting model 'Alumno'
        db.delete_table(u'alumno')

        # Deleting model 'AlumnoTomaEts'
        db.delete_table(u'alumno_toma_ets')

        # Deleting model 'Claveshorario'
        db.delete_table(u'claveshorario')

        # Deleting model 'Depto'
        db.delete_table(u'depto')

        # Deleting model 'EmpleadoEscolar'
        db.delete_table(u'empleado_escolar')

        # Deleting model 'EnfermedadesUsuario'
        db.delete_table(u'enfermedades_usuario')

        # Deleting model 'Ets'
        db.delete_table(u'ets')

        # Deleting model 'EtsAplicarseEnSalon'
        db.delete_table(u'ets_aplicarse_en_salon')

        # Deleting model 'Grupo'
        db.delete_table(u'grupo')

        # Deleting model 'Laboratorio'
        db.delete_table(u'laboratorio')

        # Deleting model 'Materia'
        db.delete_table(u'materia')

        # Deleting model 'MateriaImpartidaEnGrupo'
        db.delete_table(u'materia_impartida_en_grupo')

        # Deleting model 'MateriaImpartidaEnLab'
        db.delete_table(u'materia_impartida_en_lab')

        # Deleting model 'Material'
        db.delete_table(u'material')

        # Deleting model 'Profesor'
        db.delete_table(u'profesor')

        # Deleting model 'ProfesorDaClaseEnGrupo'
        db.delete_table(u'profesor_da_clase_en_grupo')

        # Deleting model 'ProfesorImparteMateria'
        db.delete_table(u'profesor_imparte_materia')

        # Deleting model 'Salon'
        db.delete_table(u'salon')

        # Deleting model 'TelefonoUsuario'
        db.delete_table(u'telefono_usuario')

        # Deleting model 'Usuario'
        db.delete_table(u'usuario')


    models = {
        u'principal.alergiasusuario': {
            'Meta': {'object_name': 'AlergiasUsuario', 'db_table': "u'alergias_usuario'"},
            'alergia': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'cve_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Usuario']", 'db_column': "u'cve_usuario'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.alumno': {
            'Meta': {'object_name': 'Alumno', 'db_table': "u'alumno'"},
            'cve_usuarioa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Usuario']", 'primary_key': 'True', 'db_column': "u'cve_usuarioa'"}),
            'escuela_procedencia': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'promedio_escuela_procedencia': ('django.db.models.fields.FloatField', [], {}),
            'tipo_alumno': ('django.db.models.fields.IntegerField', [], {}),
            'tutor_escolar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Profesor']", 'null': 'True', 'db_column': "u'tutor_escolar'", 'blank': 'True'}),
            'tutor_legal': ('django.db.models.fields.CharField', [], {'max_length': '25L'})
        },
        u'principal.alumnotomaets': {
            'Meta': {'object_name': 'AlumnoTomaEts', 'db_table': "u'alumno_toma_ets'"},
            'boleta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Alumno']", 'db_column': "u'boleta'"}),
            'calificacion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cve_materia_ets': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'materia_ets_alumno'", 'db_column': "u'cve_materia_ets'", 'to': u"orm['principal.Ets']"}),
            'etsturno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Ets']", 'db_column': "u'etsturno'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.claveshorario': {
            'Meta': {'object_name': 'Claveshorario', 'db_table': "u'claveshorario'"},
            'cve_horario': ('django.db.models.fields.CharField', [], {'max_length': '2L', 'primary_key': 'True'}),
            'descripcion_horario': ('django.db.models.fields.CharField', [], {'max_length': '50L'})
        },
        u'principal.depto': {
            'Meta': {'object_name': 'Depto', 'db_table': "u'depto'"},
            'jefe_depto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Profesor']", 'db_column': "u'jefe_depto'"}),
            'nombre_depto': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'primary_key': 'True'}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'})
        },
        u'principal.empleadoescolar': {
            'Meta': {'object_name': 'EmpleadoEscolar', 'db_table': "u'empleado_escolar'"},
            'carrera': ('django.db.models.fields.CharField', [], {'max_length': '25L'}),
            'cve_usuarioee': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Usuario']", 'primary_key': 'True', 'db_column': "u'cve_usuarioee'"}),
            'grado_estudios': ('django.db.models.fields.IntegerField', [], {}),
            'hora_entrada': ('django.db.models.fields.CharField', [], {'max_length': '8L'}),
            'hora_salida': ('django.db.models.fields.CharField', [], {'max_length': '8L'}),
            'lab_a_mi_cargo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Laboratorio']", 'null': 'True', 'db_column': "u'lab_a_mi_cargo'", 'blank': 'True'}),
            'salario': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {})
        },
        u'principal.enfermedadesusuario': {
            'Meta': {'object_name': 'EnfermedadesUsuario', 'db_table': "u'enfermedades_usuario'"},
            'cve_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Usuario']", 'db_column': "u'cve_usuario'"}),
            'enfermedad': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.ets': {
            'Meta': {'object_name': 'Ets', 'db_table': "u'ets'"},
            'cve_materia_ets': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Materia']", 'db_column': "u'cve_materia_ets'"}),
            'dia': ('django.db.models.fields.IntegerField', [], {}),
            'evaluador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Profesor']", 'db_column': "u'evaluador'"}),
            'hora': ('django.db.models.fields.CharField', [], {'max_length': '8L'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'turno': ('django.db.models.fields.IntegerField', [], {})
        },
        u'principal.etsaplicarseensalon': {
            'Meta': {'object_name': 'EtsAplicarseEnSalon', 'db_table': "u'ets_aplicarse_en_salon'"},
            'cve_materia_ets': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'materia_ets_salon'", 'db_column': "u'cve_materia_ets'", 'to': u"orm['principal.Ets']"}),
            'cve_salon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Salon']", 'db_column': "u'cve_salon'"}),
            'etsturno': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Ets']", 'db_column': "u'etsturno'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.grupo': {
            'Meta': {'object_name': 'Grupo', 'db_table': "u'grupo'"},
            'cve_grupo': ('django.db.models.fields.CharField', [], {'max_length': '4L', 'primary_key': 'True'}),
            'salon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Salon']", 'db_column': "u'salon'"})
        },
        u'principal.laboratorio': {
            'Meta': {'object_name': 'Laboratorio', 'db_table': "u'laboratorio'"},
            'nombre_lab': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'primary_key': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {}),
            'ubicacion': ('django.db.models.fields.CharField', [], {'max_length': '30L', 'blank': 'True'})
        },
        u'principal.materia': {
            'Meta': {'object_name': 'Materia', 'db_table': "u'materia'"},
            'coordinador': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Profesor']", 'db_column': "u'coordinador'"}),
            'creditos': ('django.db.models.fields.FloatField', [], {}),
            'cve_materia': ('django.db.models.fields.CharField', [], {'max_length': '4L', 'primary_key': 'True'}),
            'depto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Depto']", 'db_column': "u'depto'"}),
            'materia_antecedente': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'materia_materia_antecedente'", 'null': 'True', 'db_column': "u'materia_antecedente'", 'to': u"orm['principal.Materia']"}),
            'materia_siguiente': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'materia_materia_siguiente'", 'null': 'True', 'db_column': "u'materia_siguiente'", 'to': u"orm['principal.Materia']"}),
            'nivel': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nom_materia': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'plan_estudios': ('django.db.models.fields.CharField', [], {'max_length': '4L'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'principal.materiaimpartidaengrupo': {
            'Meta': {'object_name': 'MateriaImpartidaEnGrupo', 'db_table': "u'materia_impartida_en_grupo'"},
            'cve_horario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Claveshorario']", 'db_column': "u'cve_horario'"}),
            'cve_materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Materia']", 'db_column': "u'cve_materia'"}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Grupo']", 'db_column': "u'grupo'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.materiaimpartidaenlab': {
            'Meta': {'object_name': 'MateriaImpartidaEnLab', 'db_table': "u'materia_impartida_en_lab'"},
            'clave_horario_lab': ('django.db.models.fields.IntegerField', [], {}),
            'cve_materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Materia']", 'db_column': "u'cve_materia'"}),
            'dia': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_lab': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Laboratorio']", 'db_column': "u'nombre_lab'"})
        },
        u'principal.material': {
            'Meta': {'object_name': 'Material', 'db_table': "u'material'"},
            'cantidad_disponible': ('django.db.models.fields.IntegerField', [], {}),
            'cantidad_no_disponible': ('django.db.models.fields.IntegerField', [], {}),
            'cve_material': ('django.db.models.fields.CharField', [], {'max_length': '5L', 'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '20L'})
        },
        u'principal.profesor': {
            'Meta': {'object_name': 'Profesor', 'db_table': "u'profesor'"},
            'cve_usuariop': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.EmpleadoEscolar']", 'primary_key': 'True', 'db_column': "u'cve_usuariop'"}),
            'grupo_tutorado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Grupo']", 'null': 'True', 'db_column': "u'grupo_tutorado'", 'blank': 'True'}),
            'tipo': ('django.db.models.fields.IntegerField', [], {})
        },
        u'principal.profesordaclaseengrupo': {
            'Meta': {'object_name': 'ProfesorDaClaseEnGrupo', 'db_table': "u'profesor_da_clase_en_grupo'"},
            'cve_prof': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Profesor']", 'db_column': "u'cve_prof'"}),
            'grupo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Grupo']", 'db_column': "u'grupo'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.profesorimpartemateria': {
            'Meta': {'object_name': 'ProfesorImparteMateria', 'db_table': "u'profesor_imparte_materia'"},
            'cve_materia': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Materia']", 'db_column': "u'cve_materia'"}),
            'cve_prof': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Profesor']", 'db_column': "u'cve_prof'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'principal.salon': {
            'Meta': {'object_name': 'Salon', 'db_table': "u'salon'"},
            'cve_salon': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'principal.telefonousuario': {
            'Meta': {'object_name': 'TelefonoUsuario', 'db_table': "u'telefono_usuario'"},
            'cve_usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['principal.Usuario']", 'db_column': "u'cve_usuario'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tel': ('django.db.models.fields.CharField', [], {'max_length': '30L'})
        },
        u'principal.usuario': {
            'Meta': {'object_name': 'Usuario', 'db_table': "u'usuario'"},
            'apmat': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'appat': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'calle': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
            'clasificacion': ('django.db.models.fields.IntegerField', [], {}),
            'colonia': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
            'cp': ('django.db.models.fields.IntegerField', [], {}),
            'curp': ('django.db.models.fields.CharField', [], {'max_length': '18L'}),
            'cve_usuario': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'email_institucional': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'email_personal': ('django.db.models.fields.CharField', [], {'max_length': '50L'}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'fecha_alta': ('django.db.models.fields.DateField', [], {}),
            'fecha_nac': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'foto': ('django.db.models.fields.CharField', [], {'max_length': '50L', 'blank': 'True'}),
            'lt': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'mun_o_del': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'mz': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nacionalidad': ('django.db.models.fields.CharField', [], {'max_length': '15L'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '30L'}),
            'nss': ('django.db.models.fields.CharField', [], {'max_length': '20L', 'blank': 'True'}),
            'num': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '20L'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1L'}),
            'ss_institucion': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'tipo_sangre': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['principal']