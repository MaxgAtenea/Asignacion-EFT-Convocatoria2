BOLSA_COMUN = 7_062_748_147

PORCENTAJES_RUTA = {
    "antiguos":  0.4,
    "nuevos": 0.3,
    "cerrados": 0.3
}

RECURSOS_POR_RUTA = {
    "antiguos":  BOLSA_COMUN*PORCENTAJES_RUTA['antiguos'],
    "nuevos": BOLSA_COMUN*PORCENTAJES_RUTA['nuevos'],
    "cerrados": BOLSA_COMUN*PORCENTAJES_RUTA['cerrados']
}

# Columna que especifica el valor del programa
COLUMNA_VALOR_PROGRAMA = "VALOR PROGRAMA PROYECTADO"
# Columna que especifica el numero de cupos maximos aprobados 
COLUMNA_CUPOS_MAXIMOS = "numero_maximo_cupos"
COLUMNA_CUPOS_MINIMOS = "numero_minimo_cupos"

MINIMO_CUPOS_CERRADOS_SEDE = 50

NOMBRE_COLUMNAS_MAPPING_EXTERNO = {
    "CODIGO DEL PROGRAMA": 'codigo_programa', #done
    "NOMBRE DEL PROGRAMA" : 'nombre_programa', #done
    "Nombre Institucion" : "nombre_institucion", #done
    "NÚMERO DE CUPOS A OFERTAR": "numero_cupos_ofertar", #done
    "DURACION PROGRAMA HORAS" : "duracion_horas_programa", #done
    "ISOEFT" : "isoeft", #done
    "Ocupacion": "ocupacion", #done
    "IPO": "ipo", #done
    "RUTA HABILITADA": "ruta_habilitada", #done
    COLUMNA_VALOR_PROGRAMA: "valor_programa",
    "NÚMERO MÍNIMO DE CUPOS": "numero_minimo_cupos", #done
    "CODIGO DE LA OCUPACION": "cod_CNO", #done
    "PUNTAJE NUEVOS Y CERRADOS": "puntaje", #done
    "META DE VINCULACION": "meta_vinculacion", #done
    "NÚMERO MÍNIMO DE CUPOS": "numero_minimo_cupos"
}

NOMBRE_COLUMNAS_MAPPING_COMPLEMENTO = {
    "Ocupacion": "_ocupacion",
    "ISOEFT_4d": "isoeft_4d",
    "CODIGO_PROGRAMA": "codigo_programa"
}


TIPO_COLUMNAS_MAPPING_EXTERNO = {
    "codigo_programa" : 'Int64', #done
    "nombre_programa" : "str", #done
    "nombre_institucion" : "str", #done
    "numero_cupos_ofertar" : "Int64" , #done
    "cod_CNO": "Int64", #done
    "duracion_horas_programa": "Int64", #done
    "isoeft" : "float", #done
    "ocupacion": "str", #done 
    "ipo": "float", #done 
    "puntaje": "float", #done
    "meta_vinculacion": "float", #done
    "ruta_habilitada" : "str", #done 
    "valor_programa": "float", #done
    "valor_programa" : "float",
    "numero_minimo_cupos": "Int64" #done
}

TIPO_COLUMNAS_MAPPING_COMPLEMENTO = {
    'codigo_programa' : "Int64",
    "cod_CNO" : "Int64",
    "cod_CNO3d": "Int64",
    "cod_CNO2d": "Int64",
    "cod_CNO1d": "Int64",
    "isoeft_4d" : "float",
    "_ocupacion": "str",
}


# Columnas para quedarse con la data complementaria
COLUMNAS_COMPLEMENTO = [
    'cod_CNO',
    'cod_CNO3d',
    'cod_CNO2d',
    'cod_CNO1d',
    '_ocupacion',
    'isoeft_4d',
    'codigo_programa'
]

#son las columnas que queremos manipular en todo el proceso
COLUMNAS_EXTERNO = [
    'ruta_habilitada',
    'nombre_institucion',
    'nombre_programa',
    'codigo_programa',
    'cod_CNO',
    'ocupacion',
    'ipo',
    'isoeft',
    'puntaje',
    'meta_vinculacion',
    "numero_cupos_ofertar",
    'duracion_horas_programa',
    "numero_minimo_cupos",
    "valor_programa"
]

#diccionario con los cno e IPO de los programas nuevos
PROGRAMA_INFO = {
    "TÉCNICO LABORAL COMO ASESOR COMERCIAL Y DE SERVICIOS": (6311, 0.524),
    "TÉCNICO LABORAL POR COMPETENCIAS ACOMPAÑANTES DOMICILIARIOS": (6371, 0.492),
    "Técnico Laboral por competencias en Codificación de Software": (2281, 0.665),
    "TECNICO LABORAL EN AUXILIAR DE ENFERMERÍA": (3311, 0.477),
    "TECNICO LABORAL EN ASISTENCIA Y SOPORTE DE TECNOLOGIAS DE LA INFORMACION": (2281, 0.665),
    "TECNICO LABORAL EN MANEJO DE HERRAMIENTAS PARA LA CODIFICACION DE SOFTWARE": (2281, 0.665),
    "TÉCNICO LABORAL EN AUXILIAR CLÍNICA VETERINARIA": (6374, 0.558),
    "TÉCNICO LABORAL AUXILIAR EN AUTOMATIZACIÓN E INSTRUMENTACIÓN INDUSTRIAL": (2321, 0.551),
    "TÉCNICO LABORAL AUXILIAR EN RECREACIÓN Y DEPORTE": (6642, 0.546),
    "TÉCNICO LABORAL AUXILIAR AGENTE DE VENTAS Y PUBLICIDAD": (6233, 0.523),
    "TÉCNICO LABORAL EN SOPORTE Y MANTENIMIENTO DE TI": (2281, 0.665),
    "TÉCNICO LABORAL EN AUXILIAR DE SISTEMAS INFORMÁTICOS": (8325, 0.502)
}




    
