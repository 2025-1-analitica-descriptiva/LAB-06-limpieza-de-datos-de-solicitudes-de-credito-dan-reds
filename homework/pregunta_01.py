"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    import pandas as pd 
    import os.path
    
    # subir los datos
    df = pd.read_csv('./files/input/solicitudes_de_credito.csv', sep=';', encoding="UTF-8")
    
    df = df.drop(columns=['Unnamed: 0'])

    df['sexo'] = df['sexo'].str.lower()  # Convertir a minúsculas

    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.lower() # Convertir a minúsculas

    df['idea_negocio'] = df['idea_negocio'].str.lower()  # Convertir a minúsculas
    
    df['idea_negocio'] = df['idea_negocio'].str.replace('_', ' ').str.replace('-', ' ').str.strip()

    df['barrio'] = df['barrio'].str.lower()  # Convertir a minúsculas

    df['barrio'] = df['barrio'].str.replace('_', ' ').str.replace('-', ' ')

    df['comuna_ciudadano'] = df['comuna_ciudadano'].astype(int)  # Convertir a cadena

    # Convertir a datetime la columna 'fecha_de_beneficio'
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True, errors='coerce', format='mixed')

    # Eliminar "$" de la columna 'monto_del_credito' y convertir a entero
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('$','')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace(',','')
    df['monto_del_credito'] = df['monto_del_credito'].str.replace('.00','')
    df['monto_del_credito'] = df['monto_del_credito'].str.strip()

    df['línea_credito'] = df['línea_credito'].str.lower()  # Convertir a minúsculas

    df['línea_credito'] = df['línea_credito'].str.strip().str.replace('_', ' ').str.replace('-', ' ').str.strip()

    # Eliminar registros duplicados
    df.drop_duplicates(inplace=True)

    df.dropna(inplace=True)
    
    df.to_csv('./files/output/solicitudes_de_credito.csv', sep=';')

