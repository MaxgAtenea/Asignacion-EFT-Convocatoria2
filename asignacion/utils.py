import os
from datetime import datetime
import pandas as pd


def imprimir_recursos_por_ruta(recursos: dict):
    """Imprime los recursos por ruta en formato tabla con separadores de miles."""
    print("{:<10} | {:>20}".format("Ruta", "Recursos"))
    print("-" * 35)
    for ruta, valor in recursos.items():
        print("{:<10} | {:>20}".format(ruta, f"{int(valor):,}".replace(",", ".")))



def exportar_log_errores(errores: list[str], nombre_archivo_log: str = "validacion.log") -> None:
    """
    Exporta una lista de errores a un archivo de log en ../output/logs/.

    Parámetros:
        errores (list): Lista de strings con mensajes de error.
        nombre_archivo_log (str): Nombre del archivo a crear o modificar.
    """
    if not errores:
        return  # Nada que exportar

    # Crear directorio si no existe
    ruta_logs = os.path.join("..", "output", "logs")
    os.makedirs(ruta_logs, exist_ok=True)

    # Ruta completa del log
    ruta_completa = os.path.join(ruta_logs, nombre_archivo_log)

    # Escribir errores en el archivo
    with open(ruta_completa, "a", encoding="utf-8") as log_file:
        log_file.write(f"\n--- LOG DE VALIDACIÓN ({datetime.now()}): ---\n")
        for error in errores:
            log_file.write(f"- {error}\n")
        print(f"Los errores quedaron logeados en: {ruta_completa}")



def merge_without_duplicates(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    df2_columns: list,
    merge_on: list,
    suffixes: tuple = ("_first", "_second"),
    how: str = "outer",
    indicator: bool = True
) -> pd.DataFrame:
    """
    Merge two DataFrames after dropping duplicated columns in both.

    Parameters
    ----------
    df1 : pd.DataFrame
        First DataFrame.
    df2 : pd.DataFrame
        Second DataFrame (subset of columns will be used).
    df2_columns : list
        Columns to keep from df2.
    merge_on : list
        List of columns to merge on.
    suffixes : tuple, optional
        Suffixes for overlapping column names, by default ("_first", "_second").
    how : str, optional
        Type of merge to perform, by default "outer".
    indicator : bool, optional
        Whether to add a merge indicator column, by default True.

    Returns
    -------
    pd.DataFrame
        Merged DataFrame with duplicate columns removed.
    """
    
    # Select only relevant columns from df2
    df2 = df2[df2_columns]

    # Drop duplicate column names in both
    df1 = df1.loc[:, ~df1.columns.duplicated()]
    df2 = df2.loc[:, ~df2.columns.duplicated()]

    # Merge
    merged = pd.merge(
        df1, df2,
        on=merge_on,
        suffixes=suffixes,
        how=how,
        indicator=indicator
    )

    return merged

