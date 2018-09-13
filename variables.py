# coding=utf-8

dates = {
    "1980": "",
    "1981": "",
    "1982": "",
    "1983": "",
    "1984": "",
    "1985": "",
    "1986": "",
    "1987": "",
    "1988": "",
    "1989": "",
    "1990": "",
    "1991": "",
    "1992": "",
    "1993": "",
    "1994": "",
    "1995": "",
    "1996": "",
    "1997": "",
    "1998": "",
    "1999": "",
    "2000": "",
    "2001": "",
    "2002": "",
    "2003": "",
    "2004": "",
    "2005": "",
    "2006": "",
    "2007": "",
    "2008": "",
    "2009": "",
    "2010": "",
    "2011": "",
    "2012": "",
    "2013": "",
    "2014": "",
    "2015": "",
    "2010": "",
    "2016": "",
    "2017": "2017",
    "2018": "2018Q1",
    "hoy": "2018Q1",
    "este mes": "2018Q1",
    "este año": "2018Q1",
    "Enero": "",
    "Febrero": "",
    "Marzo": "",
    "Abril": "",
    "Mayo": "",
    "Junio": "",
    "Julio": "",
    "Agosto": "",
    "Septiembre": "",
    "Octubre": "",
    "Noviembre": "",
    "Diciembre": ""
}

indicators = {
    'Afiliaciones a la Seguridad Social': 'AFILIACIONES',
    'Venta mayor de cemento': 'CEMENTO_VENTAS',
    'Empleo registrado. Agricultura': 'EMPLEO_REGISTRADO_AGRICULTURA',
    'Empleo registrado. Hostelería': 'EMPLEO_REGISTRADO_HOSTELERIA',
    'Empleo registrado. Industria': 'EMPLEO_REGISTRADO_INDUSTRIA',
    'Empleo registrado. Servicios': 'EMPLEO_REGISTRADO_SERVICIOS',
    'Población inactiva': 'POBLACION_INACTIVA',
    'Población inactiva. Hombres': 'POBLACION_INACTIVA_HOMBRES',
    'Población inactiva. Mujeres': 'POBLACION_INACTIVA_MUJERES',
    'Tasa de actividad': 'TASA_ACTIVIDAD',
    'Tasa de actividad. Hombres': 'TASA_ACTIVIDAD_HOMBRES',
    'Tasa de actividad. Mujeres': 'TASA_ACTIVIDAD_MUJERES',
    'Tasa de empleo': 'TASA_EMPLEO',
    'Tasa de empleo. Hombres': 'TASA_EMPLEO_HOMBRES',
    'Tasa de empleo. Mujeres': 'TASA_EMPLEO_MUJERES',
    'Tasa de paro': 'TASA_PARO',
    'Tasa de paro. Hombres': 'TASA_PARO_HOMBRES',
    'Tasa de paro. Mujeres': 'TASA_PARO_MUJERES',
    'Paro registrado': 'PARO_REGISTRADO',
    'Paro registrado. Hombres': 'PARO_REGISTRADO_HOMBRES',
    'Paro registrado. Mujeres': 'PARO_REGISTRADO_MUJERES',
    'Nacimientos': 'NACIMIENTOS',
    'Defunciones': 'DEFUNCIONES',
    'Población. Edad media': 'POBLACION_EDAD_MEDIA',
    'Población. De 0 a 14 años ': 'POBLACION_00A14_PC',
    'Población. De 65 o más años ': 'POBLACION_65MAS_PC',
    'Defunciones. Mujeres': 'DEFUNCIONES_MUJERES',
    'Nacimientos. Hombres': 'NACIMIENTOS_HOMBRES',
    'Nacimientos. Mujeres': 'NACIMIENTOS_MUJERES',
    'Pernoctaciones en alojamientos turísticos': 'ALOJATUR_PERNOCTACIONES',
    'Plazas ofertadas por alojamientos turísticos': 'ALOJATUR_PLAZAS_OFERTADAS',
    'Población': 'POBLACION',
    'Población. De 0 a 14 años': 'POBLACION_00A14',
    'Población. De 15 a 64 años': 'POBLACION_15A64',
    'Población. De 15 a 64 años. Hombres': 'POBLACION_HOMBRES_15A64',
    'Población. De 65 o más años': 'POBLACION_65MAS',
    'Población. Hombres': 'POBLACION_HOMBRES',
    'Población. Mujeres': 'POBLACION_MUJERES',
    'Población. De 0 a 14 años. Hombres': 'POBLACION_HOMBRES_00A14',
    'Población. De 0 a 14 años. Mujeres': 'POBLACION_MUJERES_00A14',
    'Población. De 65 o más años. Mujeres': 'POBLACION_MUJERES_65MAS',
    'Matriculación de vehículos': 'MATRICULA_VEHICULOS',
    'Matriculación de vehículos. Turismos': 'MATRICULA_VEHICULOS_TURISMOS',
    'Policía Local. Efectivos': 'POLICIA_LOCAL_EFECTIVOS',
    'Viajeros entrados en alojamientos turísticos': 'ALOJATUR_VIAJEROS_ENTRADOS',
    'Empleo registrado. Cabildos': 'EMPLEO_REGISTRADO_CABILDOS',
    'Empleo registrado por cada 1.000 habitantes. Cabildos': 'EMPLEO_REGISTRADO_CABILDOS_HAB',
    'IRPF. Base Imponible por declarante': 'TRIBUTO_IRPF_BASE_IMPONIBLE_DECLARANTE',
    'IBI. Cuota líquida. Urbanos': 'TRIBUTO_IBI_CUOTA_LIQUIDA_URBANO',
    'IBI. Cuota líquida. Rústicos': 'TRIBUTO_IBI_CUOTA_LIQUIDA_RUSTICO',
    'Presupuesto liquidado. Gastos por habitante. Ayuntamientos': 'PRESUPUESTO_AYUNTAMIENTOS_LIQUIDADO_GASTO_HABITANTE',
    'Presupuesto liquidado. Ingresos por habitante. Ayuntamientos': 'PRESUPUESTO_AYUNTAMIENTOS_LIQUIDADO_INGRESO_HABITANTE',
    'Presupuesto liquidado. Ingresos fiscales por habitante. Ayuntamientos': 'PRESUPUESTO_AYUNTAMIENTOS_LIQUIDADO_INGRESO_FISCAL_HABITANTE',
    'Presupuesto liquidado. Gastos por habitante. Cabildos': 'PRESUPUESTO_CABILDOS_LIQUIDADO_GASTO_HABITANTE',
    'Presupuesto liquidado. Ingresos por habitante. Cabildos': 'PRESUPUESTO_CABILDOS_LIQUIDADO_INGRESO_HABITANTE',
    'Presupuesto liquidado. Ingresos fiscales por habitante. Cabildos': 'PRESUPUESTO_CABILDOS_LIQUIDADO_INGRESO_FISCAL_HABITANTE',
    'Población. De 65 o más años. Hombres': 'POBLACION_HOMBRES_65MAS',
    'Población. De 15 a 64 años. Mujeres': 'POBLACION_MUJERES_15A64',
    'Matrimonios. Entre cónyuges de diferente sexo': 'MATRIMONIOS_SEXO_DIFERENTE',
    'Defunciones. Hombres': 'DEFUNCIONES_HOMBRES',
    'Migraciones. Saldo migratorio': 'MIGRACIONES_SALDO',
    'Migraciones. Saldo migratorio. Hombres': 'MIGRACIONES_SALDO_HOMBRES',
    'Migraciones. Saldo migratorio. Mujeres': 'MIGRACIONES_SALDO_MUJERES',
    'Policía Local. Efecticvos por cada 1.000 habitantes': 'POLICIA_LOCAL_EFECTIVOS_HABITANTE',
    'Parque de vehículos': 'PARQUE_VEHICULOS',
    'Parque de vehículos. Turismos': 'PARQUE_VEHICULOS_TURISMOS',
    'Tráfico aéreo comercial. Movimiento de mercancías': 'TRAFICO_AEREO_MERCANCIAS',
    'Superficie cultivada': 'SUPERFICIE_CULTIVO',
    'Superficie cultivada. Regadío': 'SUPERFICIE_CULTIVO_REGADIO',
    'Superficie cultivada. Cultivos herbáceos': 'SUPERFICIE_CULTIVO_HERBACEOS',
    'Superficie cultivada. Cultivos leñosos': 'SUPERFICIE_CULTIVO_LENOSOS',
    'Tasa bruta de mortalidad': 'TASA_MORTALIDAD',
    'Población parada': 'POBLACION_PARADA',
    'Población parada. Hombres': 'POBLACION_PARADA_HOMBRES',
    'Población parada. Mujeres': 'POBLACION_PARADA_MUJERES',
    'Población ocupada': 'POBLACION_OCUPADA',
    'Población ocupada. Hombres': 'POBLACION_OCUPADA_HOMBRES',
    'Población ocupada. Mujeres': 'POBLACION_OCUPADA_MUJERES',
    'Población turística equivalente en alojamientos turísticos': 'ALOJATUR_POBLACION_TUR_ETC',
    'Empleo registrado. Ayuntamientos': 'EMPLEO_REGISTRADO_AYUNTAMIENTOS',
    'Empleo registrado por cada 1.000 habitantes. Ayuntamientos': 'EMPLEO_REGISTRADO_AYUNTAMIENTOS_HAB',
    'Parque de vehículos por cada 1.000 habitantes': 'PARQUE_VEHICULOS_HABITANTE',
    'Parque de vehículos por cada 1.000 habitantes. Turismos': 'PARQUE_VEHICULOS_TURISMOS_HABITANTE',
    'Tráfico aéreo comercial. Movimiento de aeronaves': 'TRAFICO_AEREO_AVIONES',
    'Tráfico aéreo comercial. Movimiento de pasajeros': 'TRAFICO_AEREO_PASAJEROS',
    'Superficie cultivada. Secano': 'SUPERFICIE_CULTIVO_SECANO',
    'Superficie': 'SUPERFICIE',
    'Alojamientos turísticos abiertos': 'ALOJATUR_ABIERTOS',
    'Empleo registrado. Comercio': 'EMPLEO_REGISTRADO_COMERCIO',
    'Empleo registrado. Construcción': 'EMPLEO_REGISTRADO_CONSTRUCCION',
    'Población activa': 'POBLACION_ACTIVA',
    'Población activa. Hombres': 'POBLACION_ACTIVA_HOMBRES',
    'Población activa. Mujeres': 'POBLACION_ACTIVA_MUJERES',
    'Afiliaciones a la Seguridad Social. Hombres': 'AFILIACIONES_HOMBRES',
    'Afiliaciones a la Seguridad Social. Mujeres': 'AFILIACIONES_MUJERES',
    'Afiliaciones a la Seguridad Social. Empleos asalariados. Hombres': 'AFILIACIONES_ASALARIADOS_HOMBRES',
    'Afiliaciones a la Seguridad Social. Empleos asalariados': 'AFILIACIONES_ASALARIADOS',
    'Afiliaciones a la Seguridad Social. Empleos asalariados. Mujeres': 'AFILIACIONES_ASALARIADOS_MUJERES',
    'Afiliaciones a la Seguridad Social. Empleos autónomos': 'AFILIACIONES_AUTONOMOS',
    'Afiliaciones a la Seguridad Social. Empleos autónomos. Hombres': 'AFILIACIONES_AUTONOMOS_HOMBRES',
    'Afiliaciones a la Seguridad Social. Empleos autónomos. Mujeres': 'AFILIACIONES_AUTONOMOS_MUJERES',
    'Índice de precios de consumo (IPC). Subyacente': 'IPC_SUBYACENTE',
    'Tasa bruta de mortalidad. Hombres': 'TASA_MORTALIDAD_HOMBRES',
    'Tasa bruta de mortalidad. Mujeres': 'TASA_MORTALIDAD_MUJERES',
    'Comercio exterior. Importaciones en peso': 'COMERCIO_EXTERIOR_IMPORTACIONES_PESO',
    'Comercio exterior. Importaciones en valor': 'COMERCIO_EXTERIOR_IMPORTACIONES_VALOR',
    'Comercio exterior. Exportaciones en peso': 'COMERCIO_EXTERIOR_EXPORTACIONES_PESO',
    'Comercio exterior. Exportaciones en valor': 'COMERCIO_EXTERIOR_EXPORTACIONES_VALOR',
    'Comercio exterior. Déficit comercial': 'COMERCIO_EXTERIOR_DEFICIT_COMERCIAL',
    'Comercio exterior. Tasa de cobertura': 'COMERCIO_EXTERIOR_TASA_COBERTURA',
    'PIB a precios corrientes': 'PIB_PM_CORRIENTE',
    'Energía eléctrica. Disponible': 'ENERGIA_ELECTRICA_DISPONIBLE',
    'Coste laboral. Por trabajador y mes': 'COSTE_LABORAL_TRABAJADOR',
    'Coste laboral. Por hora efectiva de trabajo': 'COSTE_LABORAL_HORA',
    'Hipotecas constituidas': 'HIPOTECAS_CONSTITUIDAS',
    'Hipotecas constituidas. Importe': 'HIPOTECAS_CONSTITUIDAS_IMPORTE',
    'Hipotecas canceladas': 'HIPOTECAS_CANCELADAS',
    'Índice de volumen encadenado del PIB (variaciones reales)': 'PIB_PM_VOLUMEN',
    'Sociedades mercantiles. Creadas': 'SOCIEDADES_MERCANTILES_CREADAS',
    'Sociedades mercantiles. Creadas. Capital suscrito': 'SOCIEDADES_MERCANTILES_CREADAS_CAPITAL',
    'Sociedades mercantiles. Amplian capital': 'SOCIEDADES_MERCANTILES_AMPLIADAS',
    'Sociedades mercantiles. Amplian capital. Capital suscrito': 'SOCIEDADES_MERCANTILES_AMPLIADAS_CAPITAL',
    'Licitación oficial en construcción': 'LICITACION_OFICIAL',
    'Licitación oficial en construcción. Edificación': 'LICITACION_OFICIAL_EDIFICACION',
    'Licitación oficial en construcción. Ingeniería civil': 'LICITACION_OFICIAL_INGENIERIA_CIVIL',
    'Afiliaciones a la Seguridad Social. Industria': 'AFILIACIONES_INDUSTRIA',
    'Afiliaciones a la Seguridad Social. Construcción': 'AFILIACIONES_CONSTRUCCION',
    'Afiliaciones a la Seguridad Social. Servicios': 'AFILIACIONES_SERVICIOS',
    'Afiliaciones a la Seguridad Social. Agricultura': 'AFILIACIONES_AGRICULTURA',
    'Accidentes de trabajo con baja': 'ACCIDENTES_TRABAJO_BAJA',
    'Accidentes de trabajo con baja. Jornadas no trabajadas': 'ACCIDENTES_TRABAJO_BAJA_JORNADAS',
    'Empresas inscritas en la Seguridad Social. Agricultura': 'EMPRESAS_SEGURIDAD_SOCIAL_AGRICULTURA',
    'Empresas inscritas en la Seguridad Social. Industria': 'EMPRESAS_SEGURIDAD_SOCIAL_INDUSTRIA',
    'Empresas inscritas en la Seguridad Social. Construcción': 'EMPRESAS_SEGURIDAD_SOCIAL_CONSTRUCCION',
    'Empresas inscritas en la Seguridad Social. Servicios': 'EMPRESAS_SEGURIDAD_SOCIAL_SERVICIOS',
    'Visados de obra. Viviendas': 'VISADOS_OBRA_VIVIENDAS',
    'Visados de obra. Viviendas de obra nueva': 'VISADOS_OBRA_VIVIENDAS_NUEVAS',
    'Vivienda libre. Precio del metro cuadrado': 'VIVIENDA_LIBRE_PRECIO_M2',
    'Vivienda protegida. Precio del metro cuadrado': 'VIVIENDA_PROTEGIDA_PRECIO_M2',
    'Empresas inscritas en la Seguridad Social': 'EMPRESAS_SEGURIDAD_SOCIAL',
    'IBI. Tipo de gravamen. Rústicos': 'TRIBUTO_IBI_TIPO_GRAVAMEN_RUSTICO',
    'IBI. Tipo de gravamen. Urbanos': 'TRIBUTO_IBI_TIPO_GRAVAMEN_URBANO',
    'Cabezas de ganado. Bovino': 'GANADO_BOVINO',
    'Cabezas de ganado. Caprino': 'GANADO_CAPRINO',
    'Cabezas de ganado. Ovino': 'GANADO_OVINO',
    'Cabezas de ganado. Porcino': 'GANADO_PORCINO',
    'Tasa de ocupación por plazas': 'ALOJATUR_PLAZAS_OCUPACION',
    'Gasto turístico': 'GASTO_TURISTICO',
    'Gasto medio por turista': 'GASTO_TURISTICO_TURISTA',
    'Gasto medio por turista y día': 'GASTO_TURISTICO_TURISTA_DIA',
    'Población extranjera': 'POBLACION_EXTRANJERA',
    'Población extranjera. Hombres': 'POBLACION_EXTRANJERA_HOMBRES',
    'Población extranjera. Mujeres': 'POBLACION_EXTRANJERA_MUJERES',
    'Índice de precios industriales': 'IPRI',
    'Índice de producción industrial': 'IPI',
    'Índice de precios de consumo. General': 'IPC',
    'Alumnado no universitario. Enseñanzas de régimen general': 'ALUMNADO_NO_UNIVERSITARIO_REGIMEN_GENERAL',
    'Alumnado no universitario. Educación primaria': 'ALUMNADO_NO_UNIVERSITARIO_REGIMEN_GENERAL_PRIMARIA',
    'Alumnado no universitario. Educación secundaria obligatoria (E.S.O.)': 'ALUMNADO_NO_UNIVERSITARIO_REGIMEN_GENERAL_ESO',
    'Alumnado no universitario. Centros públicos. Enseñanzas de régimen general': 'ALUMNADO_NO_UNIVERSITARIO_PUBLICOS_REGIMEN_GENERAL',
    'Alumnado no universitario. Centros privados concertados. Enseñanzas de régimen general': 'ALUMNADO_NO_UNIVERSITARIO_CONCERTADOS_REGIMEN_GENERAL',
    'Alumnado no universitario. Centros privados no concertados. Enseñanzas de régimen general': 'ALUMNADO_NO_UNIVERSITARIO_NO_CONCERTADOS_REGIMEN_GENERAL',
    'Alumnado no universitario. Educación infantil': 'ALUMNADO_NO_UNIVERSITARIO_REGIMEN_GENERAL_INFANTIL',
    'Índice de cifra de negocios. Servicios': 'IASS_CIFRA_NEGOCIO',
    'Índice de ocupación. Servicios': 'IASS_OCUPACION',
    'Comercio exterior. Importaciones en peso. Productos agrícolas': 'COMERCIO_EXTERIOR_IMPORTACIONES_PESO_AGRICOLAS',
    'Comercio exterior. Importaciones en valor. Productos agrícolas': 'COMERCIO_EXTERIOR_IMPORTACIONES_VALOR_AGRICOLAS',
    'Comercio exterior. Exportaciones en peso. Productos agrícolas': 'COMERCIO_EXTERIOR_EXPORTACIONES_PESO_AGRICOLAS',
    'Comercio exterior. Exportaciones en valor. Productos agrícolas': 'COMERCIO_EXTERIOR_EXPORTACIONES_VALOR_AGRICOLAS',
    'Empleo registrado': 'EMPLEO_REGISTRADO',
    'Empleo registrado. Autónomos': 'EMPLEO_REGISTRADO_AUTONOMOS',
    'Empleo registrado. Asalariados': 'EMPLEO_REGISTRADO_ASALARIADOS'
}

indicators_check = {
    "Superficie": "Superficie",
    "superficie": "Superficie",
    "la superficie": "Superficie",
    "terreno": "Superficie",
    "el terreno": "Superficie",
    "extension territorial": "Superficie",
    "la extension territorial": "Superficie",
    "area": "Superficie",
    "el area": "Superficie",
    "Poblacion": "Población",
    "poblacion": "Población",
    "la poblacion": "Población",
    "habitantes": "Población",
    "los habitantes": "Población",
    "numero de habitantes": "Población",
    "el numero de habitantes": "Población",
    "padron": "Población",
    "el padron": "Población",
    "Seguridad Social": "Seguridad Social",
    "seguridad social": "Seguridad Social",
    "ss": "Seguridad Social",
    "SS": "Seguridad Social",
    "Nacimientos": "Nacimientos",
    "nacimientos": "Nacimientos",
    "los nacimientos": "Nacimientos",
    "natalidad": "Nacimientos",
    "la natalidad": "Nacimientos",
    "nacidos": "Nacimientos",
    "Defunciones": "Defunciones",
    "las defunciones": "Defunciones",
    "muertes": "Defunciones",
    "las muertes": "Defunciones",
    "muertos": "Defunciones",
    "los muertos": "Defunciones",
    "Matrimonios entre conyuges de diferente sexo": "Matrimonios. Entre cónyuges de diferente sexo",
    "matrimonios": "Matrimonios. Entre cónyuges de diferente sexoo",
    "los matrimonios": "Matrimonios. Entre cónyuges de diferente sexo",
    "Migraciones saldo migratorio": "Migraciones. Saldo migratorio",
    "migraciones": "Migraciones. Saldo migratorio",
    "las migraciones": "Migraciones. Saldo migratorio",
    "Alumnado no universitario Educacion primaria": "Alumnado no universitario. Educación primaria",
    "educacion primaria": "Alumnado no universitario. Educación primaria",
    "la educacion primaria": "Alumnado no universitario. Educacion primaria",
    "alumnos primaria": "Alumnado no universitario. Educacion primaria",
    "los alumnos primaria": "Alumnado no universitario. Educacion primaria",
    "Alumnado no universitario Educacion secundaria obligatoria ESO": "Alumnado no universitario. Educación secundaria obligatoria (E.S.O.)",
    "educacion secundaria obligatoria": "Alumnado no universitario. Educación secundaria obligatoria (E.S.O.)",
    "alumnos ESO": "Alumnado no universitario. Educación secundaria obligatoria (E.S.O.)",
    "ESO": "Alumnado no universitario. Educación secundaria obligatoria (E.S.O.)",
    "la eso": "Alumnado no universitario. Educación secundaria obligatoria (E.S.O.)",
    "Alumnado no universitario Educacion infantil": "Alumnado no universitario. Educación infantil",
    "educacion infantil": "Alumnado no universitario. Educación infantil",
    "la educacion infantil": "Alumnado no universitario. Educación infantil",
    "alumnos educacion infantil": "Alumnado no universitario. Educación infantil",
    "los alumnos educacion infantil": "Alumnado no universitario. Educación infantil",
    "Policia local Efectivos": "Policía Local. Efectivos",
    "policia local": "Policía Local. Efectivos",
    "la policia local": "Policía Local. Efectivos",
    "policia": "Policía Local. Efectivos",
    "la policia": "Policía Local. Efectivos",
    "PIB a precios corrientes": "PIB a precios corrientes",
    "PIB": "PIB a precios corrientes",
    "el PIB": "PIB a precios corrientes",
    "producto interno bruto": "PIB a precios corrientes",
    "el producto interno bruto": "PIB a precios corrientes",
    "indice de precios de consumo IPC General": "Índice de precios de consumo. General",
    "IPC": "Índice de precios de consumo. General",
    "el IPC": "Índice de precios de consumo. General",
    "indice de precios de consumo": "Índice de precios de consumo. General",
    "el indice de precios de consumo": "Índice de precios de consumo. General",
    "Sociedades mercantiles Creadas": "Sociedades mercantiles. Creadas",
    "sociedades mercantiles": "Sociedades mercantiles. Creadas",
    "las sociedades mercantiles": "Sociedades mercantiles. Creadas",
    "sociedades": "Sociedades mercantiles. Creadas",
    "las sociedades": "Sociedades mercantiles. Creadas",
    "Empresas inscritas en la seguridad social": "Empresas inscritas en la Seguridad Social",
    "empresas inscritas en la seguridad social": "Empresas inscritas en la Seguridad Social",
    "las empresas inscritas en la seguridad social": "Empresas inscritas en la Seguridad Social",
    "empresas seguridad social": "Empresas inscritas en la Seguridad Social",
    "las empresas seguridad social": "Empresas inscritas en la Seguridad Social",
    "empresas inscritas en la ss": "Empresas inscritas en la Seguridad Social",
    "las empresas inscritas en la ss": "Empresas inscritas en la Seguridad Social",
    "empresas ss": "Empresas inscritas en la Seguridad Social",
    "las empresas ss": "Empresas inscritas en la Seguridad Social",
    "Afiliaciones a la seguridad social": "Afiliaciones a la Seguridad Social",
    "afiliaciones a la seguridad social": "Afiliaciones a la Seguridad Social",
    "las afiliaciones a la seguridad social": "Afiliaciones a la Seguridad Social",
    "altas en la seguridad social": "Afiliaciones a la Seguridad Social",
    "las altas en la seguridad social": "Afiliaciones a la Seguridad Social",
    "altas seguridad social": "Afiliaciones a la Seguridad Social",
    "las altas seguridad social": "Afiliaciones a la Seguridad Social",
    "inscritos en la seguridad social": "Afiliaciones a la Seguridad Social",
    "los inscritos en la seguridad social": "Afiliaciones a la Seguridad Social",
    "inscritos seguridad social": "Afiliaciones a la Seguridad Social",
    "los inscritos seguridad social": "Afiliaciones a la Seguridad Social",
    "afiliaciones a la ss": "Afiliaciones a la Seguridad Social",
    "las afiliaciones a la ss": "Afiliaciones a la Seguridad Social",
    "altas en la ss": "Afiliaciones a la Seguridad Social",
    "las altas en la ss": "Afiliaciones a la Seguridad Social",
    "altas ss": "Afiliaciones a la Seguridad Social",
    "las altas ss": "Afiliaciones a la Seguridad Social",
    "inscritos en la ss": "Afiliaciones a la Seguridad Social",
    "los inscritos en la ss": "Afiliaciones a la Seguridad Social",
    "inscritos ss": "Afiliaciones a la Seguridad Social",
    "los inscritos ss": "Afiliaciones a la Seguridad Social",
    "Tasa de empleo": "Tasa de empleo",
    "tasa de empleo": "Tasa de empleo",
    "la tasa de empleo": "Tasa de empleo",
    "el empleo": "Tasa de empleo",
    "empleo": "Tasa de empleo",
    "Tasa de paro": "Tasa de paro",
    "paro": "Tasa de paro",
    "el paro": "Tasa de paro",
    "desempleo": "Tasa de paro",
    "el desempleo": "Tasa de paro",
    "tasa de paro": "Tasa de paro",
    "la tasa de paro": "Tasa de paro",
    "Paro registrado": "Paro registrado",
    "paro registrado": "Paro registrado",
    "el paro registrado": "Paro registrado",
    "personas en paro": "Paro registrado",
    "las personas en paro": "Paro registrado",
    "personas desempleadas": "Paro registrado",
    "las personas desempleadas": "Paro registrado",
    "los desempleados": "Paro registrado",
    "desempleados": "Paro registrado",
    "Empleo registrado": "Empleo registrado",
    "empleo registrado": "Empleo registrado",
    "el empleo registrado": "Empleo registrado",
    "personas con trabajo": "Empleo registrado",
    "las personas con trabajo": "Empleo registrado",
    "empleados": "Empleo registrado",
    "los empleados": "Empleo registrado",
    "personas con empleo": "Empleo registrado",
    "las personas con empleo": "Empleo registrado",
    "Superficie cultivada": "Superficie cultivada",
    "superficie cultivada": "Superficie cultivada",
    "la superficie cultivada": "Superficie cultivada",
    "terreno cultivado": "Superficie cultivada",
    "el terreno cultivado": "Superficie cultivada",
    "area cultivada": "Superficie cultivada",
    "el area cultivada": "Superficie cultivada",
    "Energia electrica Disponible": "Energía eléctrica. Disponible",
    "energia electrica": "Energía eléctrica. Disponible",
    "la energia electrica": "Energía eléctrica. Disponible",
    "indice de precios industriales IPRI": "Índice de precios industriales",
    "indice de precios industriales": "Índice de precios industriales",
    "el indice de precios industriales": "Índice de precios industriales",
    "IPRI": "Índice de precios industriales",
    "el IPRI": "Índice de precios industriales",
    "precios industriales": "Índice de precios industriales",
    "los precios industriales": "Índice de precios industriales",
    "indice de produccion industrial IPI": "Índice de producción industrial",
    "indice de produccion industrial": "Índice de producción industrial",
    "el indice de produccion industrial": "Índice de producción industrial",
    "IPI": "Índice de producción industrial",
    "el IPI": "Índice de producción industrial",
    "produccion industrial": "Índice de producción industrial",
    "la produccion industrial": "Índice de producción industrial",
    "Venta mayor de cemento": "Venta mayor de cemento",
    "cemento": "Venta mayor de cemento",
    "el cemento": "Venta mayor de cemento",
    "venta de cemento": "Venta mayor de cemento",
    "la venta de cemento": "Venta mayor de cemento",
    "Comercio exterior Tasa de cobertura": "Comercio exterior. Tasa de cobertura",
    "comercio exterior": "Comercio exterior. Tasa de cobertura",
    "el comercio exterior": "Comercio exterior. Tasa de cobertura",
    "Pernoctaciones en alojamientos turisticos": "Pernoctaciones en alojamientos turísticos",
    "noches en hoteles": "Pernoctaciones en alojamientos turísticos",
    "las noches en hoteles": "Pernoctaciones en alojamientos turísticos",
    "Plazas ofertadas por alojamientos turisticos": "Plazas ofertadas por alojamientos turísticos",
    "plazas ofertadas en alojamientos turisticos": "Plazas ofertadas por alojamientos turísticos",
    "las plazas ofertadas en alojamientos turisticos": "Plazas ofertadas por alojamientos turísticos",
    "habitaciones disponibles en alojamientos turisticos": "Plazas ofertadas por alojamientos turísticos",
    "las habitaciones disponibles en alojamientos turisticos": "Plazas ofertadas por alojamientos turísticos",
    "Viajeros entrados en alojamientos turisticos": "Viajeros entrados en alojamientos turísticos",
    "visitantes en alojamientos turisticos": "Viajeros entrados en alojamientos turísticos",
    "los visitantes en alojamientos turisticos": "Viajeros entrados en alojamientos turísticos",
    "personas hospedadas en alojamientos turisticos": "Viajeros entrados en alojamientos turísticos",
    "las personas hospedadas en alojamientos turisticos": "Viajeros entrados en alojamientos turísticos",
    "visitantes en hoteles": "Viajeros entrados en alojamientos turísticos",
    "los visitantes en hoteles": "Viajeros entrados en alojamientos turísticos",
    "Alojamientos turisiticos abiertos": "Alojamientos turísticos abiertos",
    "alojamientos abiertos": "Alojamientos turísticos abiertos",
    "los alojamientos abiertos": "Alojamientos turísticos abiertos",
    "hoteles abiertos": "Alojamientos turísticos abiertos",
    "los hoteles abiertos": "Alojamientos turísticos abiertos",
    "hoteles": "Alojamientos turísticos abiertos",
    "los hoteles": "Alojamientos turísticos abiertos",
    "Tasa de ocupacion por plazas": "Tasa de ocupación por plazas",
    "ocupacion alojamientos turisticos": "Tasa de ocupación por plazas",
    "la ocupacion alojamientos turisticos": "Tasa de ocupación por plazas",
    "ocupacion hotelera": "Tasa de ocupación por plazas",
    "la ocupacion hotelera": "Tasa de ocupación por plazas",
    "ocupacion hoteles": "Tasa de ocupación por plazas",
    "la ocupacion hoteles": "Tasa de ocupación por plazas",
    "tasa de ocupacion hotelera": "Tasa de ocupación por plazas",
    "la tasa de ocupacion hotelera": "Tasa de ocupación por plazas",
    "Matriculacion de vehiculos": "Matriculación de vehículos",
    "vehiculos": "Matriculación de vehículos",
    "coches": "Matriculación de vehículos",
    "los vehiculos": "Matriculación de vehículos",
    "los coches": "Matriculación de vehículos",
    "vehiculos matriculados": "Matriculación de vehículos",
    "coches matriculados": "Matriculación de vehículos",
    "los vehiculos matriculados": "Matriculación de vehículos",
    "los coches matriculados": "Matriculación de vehículos",
    "Parque de vehiculos": "Parque de vehículos",
    "vehiculos en circulacion": "Parque de vehículos",
    "losvehiculos en circulacion": "Parque de vehículos",
    "coches en circulacion": "Parque de vehículos",
    "los coches en circulacion": "Parque de vehículos",
    "Trafico aereo comercial Movimiento de mercancias": "Tráfico aéreo comercial. Movimiento de mercancías",
    "trafico aereo": "Tráfico aéreo comercial. Movimiento de mercancías",
    "el trafico aereo": "Tráfico aéreo comercial. Movimiento de mercancías",
    "trafico aereo comercial": "Tráfico aéreo comercial. Movimiento de mercancías",
    "el trafico aereo comercial": "Tráfico aéreo comercial. Movimiento de mercancías",
    "transporte de mercancias": "Tráfico aéreo comercial. Movimiento de mercancías",
    "el transporte de mercancias": "Tráfico aéreo comercial. Movimiento de mercancías",
    "movimiento de mercancias": "Tráfico aéreo comercial. Movimiento de mercancías",
    "el movimiento de mercancias": "Tráfico aéreo comercial. Movimiento de mercancías",
    "Hipotecas constituidas": "Hipotecas constituidas",
    "hipotecas": "Hipotecas constituidas",
    "las hipotecas": "Hipotecas constituidas",
    "hipotecados": "Hipotecas constituidas",
    "los hipotecados": "Hipotecas constituidas",
    "Hipotecas canceladas": "Hipotecas canceladas",
    "hipotecas canceladas": "Hipotecas canceladas",
    "las hipotecas canceladas": "Hipotecas canceladas",
    "Empleo registrado Cabildos": "Empleo registrado. Cabildos",
    "empleo": "Empleo registrado. Cabildos",
    "el empleo": "Empleo registrado. Cabildos",
    "empleo por cabildos": "Empleo registrado. Cabildos",
    "el empleo por cabildos": "Empleo registrado. Cabildos",
    "Empleo registrado Ayuntamientos": "Empleo registrado. Ayuntamientos",
    "empleo por ayuntamientos": "Empleo registrado. Ayuntamientos",
    "el empleo por ayuntamientos": "Empleo registrado. Ayuntamientos",
    "IRPF Base imponible por declarante": "IRPF. Base Imponible por declarante",
    "IRPF": "IRPF. Base Imponible por declarante",
    "el IRPF": "IRPF. Base Imponible por declarante",
    "IRPF por declarante": "IRPF. Base Imponible por declarante",
    "el IRPF por declarante": "IRPF. Base Imponible por declarante",
    "IBI Cuota liquida Urbanos": "IBI. Cuota líquida. Urbanos",
    "IBI": "IBI. Cuota líquida. Urbanos",
    "el IBI": "IBI. Cuota líquida. Urbanos",
    "IBI urbanos": "IBI. Cuota líquida. Urbanos",
    "el IBI urbanos": "IBI. Cuota líquida. Urbanos",
    "impuesto sobre los bienes inmuebles": "IBI. Cuota líquida. Urbanos",
    "el impuesto sobre los bienes inmuebles": "IBI. Cuota líquida. Urbanos",
    "IBI Cuota liquida Rusticos": "IBI. Cuota líquida. Rústicos",
    "IBI rusticos": "IBI. Cuota líquida. Rústicos",
    "el IBI rusticos": "IBI. Cuota líquida. Rústicos",
    "Presupuesto liquidado Gastos por habitante Ayuntamientos": "Presupuesto liquidado. Gastos por habitante. Ayuntamientos",
    "gastos por habitante": "Presupuesto liquidado. Gastos por habitante. Ayuntamientos",
    "los gastos por habitante": "Presupuesto liquidado. Gastos por habitante. Ayuntamientos",
    "gastos por habitante ayuntamientos": "Presupuesto liquidado. Gastos por habitante. Ayuntamientos",
    "los gastos por habitante ayuntamientos": "Presupuesto liquidado. Gastos por habitante. Ayuntamientos",
    "Presupuesto liquidado Ingresos por habitante Ayuntamientos": "Presupuesto liquidado. Ingresos por habitante. Ayuntamientos",
    "ingresos por habitante": "Presupuesto liquidado. Ingresos por habitante. Ayuntamientos",
    "los ingresos por habitante": "Presupuesto liquidado. Ingresos por habitante. Ayuntamientos",
    "ingresos por habitante ayuntamientos": "PPresupuesto liquidado. Ingresos por habitante. Ayuntamientos",
    "los ingresos por habitante ayuntamientos": "Presupuesto liquidado. Ingresos por habitante. Ayuntamientos",
    "Presupuesto liquidado Gastos por habitante Cabildos": "Presupuesto liquidado. Gastos por habitante. Cabildos",
    "gastos por habitante cabildos": "Presupuesto liquidado. Gastos por habitante. Cabildos",
    "los gastos por habitante cabildos": "Presupuesto liquidado. Gastos por habitante. Cabildos",
    "Presupuesto liquidado Ingresos por habitante Cabildos": "Presupuesto liquidado. Ingresos por habitante. Cabildos",
    "ingresos por habitante cabildos": "Presupuesto liquidado. Gastos por habitante. Cabildos",
    "los ingresos por habitante cabildos": "Presupuesto liquidado. Gastos por habitante. Cabildos"
}

locations_check = {
    "Canarias",
    "Arrecife",
    "Haría",
    "San Bartolomé",
    "Teguise",
    "Tías",
    "Tinajo",
    "Yaiza",
    "Antigua",
    "Betancuria",
    "Oliva",
    "Pájara",
    "Puerto del Rosario",
    "Tuineje",
    "Agaete",
    "Agüimes"
    "Artenara",
    "Arucas",
    "Firgas",
    "Gáldar",
    "Ingenio",
    "Mogán",
    "Moya",
    "Palmas de Gran Canaria",
    "San Bartolomé de Tirajana",
    "Aldea de San Nicolás",
    "Santa Brígida",
    "Santa Lucía de Tirajana",
    "Santa María de Guía de Gran Canaria",
    "Tejeda",
    "Telde",
    "Teror",
    "Valsequillo de Gran Canaria",
    "Valleseco",
    "Vega de San Mateo",
    "Adeje",
    "Arafo",
    "Arico",
    "Arona",
    "Buenavista del Norte",
    "Candelaria",
    "Fasnia",
    "Garachico",
    "Granadilla de Abona",
    "Guancha",
    "Guía de Isora",
    "Güímar",
    "Icod de los Vinos",
    "San Cristóbal de La Laguna",
    "Matanza de Acentejo",
    "Orotava",
    "Puerto de La Cruz",
    "Realejos",
    "Rosario",
    "San Juan de la Rambla",
    "San Miguel de Abona",
    "Santa Úrsula",
    "Santiago del Teide",
    "Sauzal",
    "Silos",
    "Tacoronte",
    "Tanque",
    "Tegueste",
    "Victoria de Acentejo",
    "Vilaflor de Chasna",
    "Agulo",
    "Alajeró",
    "Hermigua",
    "San Sebastián de La Gomera",
    "Valle Gran Rey",
    "Vallehermoso",
    "Barlovento",
    "Breña Alta",
    "Breña Baja",
    "Fuencaliente de La Palma",
    "Garafía",
    "Llanos de Aridane",
    "Paso",
    "Puntagorda",
    "Puntallana",
    "San Andrés y Sauces",
    "Santa Cruz de La Palma",
    "Tazacorte",
    "Tijarafe",
    "Villa de Mazo",
    "Frontera",
    "Valverde",
    "Pinar de El Hierro",
    "Lanzarote",
    "Gran Canaria",
    "Tenerife",
    "La Gomera",
    "La Palma",
    "El Hierro",
    "Ceuta y Melilla",
    "Andalucía",
    "Aragón",
    "Principado de Asturias",
    "Illes Balears",
    "Cantabria",
    "Castilla y León",
    "Castilla - La Mancha",
    "Cataluña",
    "Comunitat Valenciana",
    "Extremadura",
    "Galicia",
    "Comunidad de Madrid",
    "Madrid",
    "Región de Murcia",
    "Comunidad Foral de Navarra",
    "Navarra",
    "País Vasco",
    "Rioja",
    "Ceuta",
    "Melilla",
    "Albacete",
    "Alacant",
    "Alicante",
    "Almería",
    "Araba",
    "Álava",
    "Asturias",
    "Ávila",
    "Badajoz",
    "Illes Balears",
    "Balears",
    "Islas Baleares",
    "Baleares",
    "Barcelona",
    "Bizkaia",
    "Burgos",
    "Cáceres",
    "Cádiz",
    "Cantabria",
    "Castelló",
    "Castellón",
    "Ceuta",
    "Ciudad Real",
    "Córdoba",
    "Coruña",
    "A Coruña",
    "Cuenca",
    "Gipuzkoa",
    "Girona",
    "Gerona",
    "Granada",
    "Guadalajara",
    "Huelva",
    "Huesca",
    "Jaén",
    "León",
    "Lleida",
    "Lérida",
    "Lugo",
    "Madrid",
    "Málaga",
    "Melilla",
    "Murcia",
    "Navarra",
    "Ourense",
    "Palencia",
    "Palmas",
    "Pontevedra",
    "Rioja",
    "Salamanca",
    "Santa Cruz de Tenerife",
    "Segovia",
    "Sevilla",
    "Soria",
    "Tarragona",
    "Teruel",
    "Toledo",
    "Valladolid",
    "Zamora",
    "Zaragoza",
    "València",
    "Valencia",
    "Lanzarote",
    "Lanzarote - Este",
    "Lanzarote - Norte",
    "Lanzarote - Suroeste",
    "Fuerteventura",
    "Fuerteventura - Centro",
    "Fuerteventura - Norte",
    "Fuerteventura - Sur",
    "Gran Canaria - Área Metropolitana",
    "Gran Canaria - Área Metropolitana",
    "Gran Canaria - Norte",
    "Gran Canaria Norte - Centro Norte",
    "Gran Canaria Norte - Noroeste",
    "Gran Canaria Norte - Oeste",
    "Gran Canaria - Sur",
    "Gran Canaria Sur - Sur",
    "Gran Canaria Sur - Sureste",
    "Tenerife - Área Metropolitana",
    "Tenerife - Área Metropolitana",
    "Tenerife - Norte",
    "Tenerife Norte - Acentejo",
    "Tenerife Norte - Daute",
    "Tenerife Norte - Icod",
    "Tenerife Norte - Valle de La Orotava",
    "Tenerife - Sur",
    "Tenerife Sur - Abona",
    "Tenerife Sur - Suroeste",
    "Tenerife Sur - Valle de Güímar",
    "La Gomera",
    "La Gomera - Norte",
    "La Gomera - Sur",
    "La Palma",
    "La Palma - Capitalina",
    "La Palma - Noreste",
    "La Palma - Noroeste",
    "La Palma - Valle de Aridane",
    "El Hierro",
    "El Hierro - El Hierro",
    "España"
}

hombres_indicadores = {
    'Población inactiva. Hombres': 'POBLACION_INACTIVA_HOMBRES',
    'Tasa de empleo. Hombres': 'TASA_EMPLEO_HOMBRES',
    'Tasa de paro. Hombres': 'TASA_PARO_HOMBRES',
    'Paro registrado. Hombres': 'PARO_REGISTRADO_HOMBRES',
    'Nacimientos. Hombres': 'NACIMIENTOS_HOMBRES'
}

mujeres_indicadores = {
    'Población inactiva. Mujeres': 'POBLACION_INACTIVA_MUJERES',
    'Tasa de empleo. Mujeres': 'TASA_EMPLEO_MUJERES',
    'Tasa de paro. Mujeres': 'TASA_PARO_MUJERES',
    'Paro registrado. Mujeres': 'PARO_REGISTRADO_MUJERES',
    'Defunciones. Mujeres': 'DEFUNCIONES_MUJERES'
}

indicators_with_sex = [
    "Población inactiva",
    "Tasa de actividad",
    "Tasa de empleo",
    "Tasa de paro",
    "Paro registrado",
    "Defunciones",
    "Nacimientos",
    "Población",
    "Defunciones",
    "Migraciones. Saldo migratorio",
    "Población parada",
    "Población ocupada",
    "Población activa",
    "Afiliaciones a la Seguridad Social",
    "Afiliaciones a la Seguridad Social. Empleos asalariados",
    "Afiliaciones a la Seguridad Social. Empleos autónomos",
    "Tasa bruta de mortalidad",
    "Población extranjera"
]

months ={
    "enero": "m01",
    "febrero": "m02" ,
    "marzo": "m03",
    "abril": "m04",
    "mayo": "m05",
    "junio": "m06",
    "julio": "m07",
    "agosto": "m08",
    "septiembre": "m09",
    "octubre": "m10",
    "noviembre": "m11",
    "diciembre": "m12"
}