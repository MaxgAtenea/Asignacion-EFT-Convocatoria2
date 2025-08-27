import pandas as pd
from . import constants
from .base import AsignacionBase

from .constants import COLUMNA_VALOR_PROGRAMA
from .constants import RECURSOS_POR_RUTA
from .constants import COLUMNA_CUPOS_MAXIMOS

class AsignacionCerrados(AsignacionBase):
    """
    ## TODO: Terminar de escribir el objetivo de la clase
    Clase encargada de gestionar la asignación de recursos para la ruta 'Cerrados'.
    """

    def __init__(self, data, recursos_iniciales =  None):
        
        if recursos_iniciales:
            super().__init__(recursos_iniciales)
        else:
            super().__init__(RECURSOS_POR_RUTA["cerrados"])
        
        self.data = data
        self.primera_asignacion = pd.DataFrame()
        
        #Ordenamos programas siguiendo criterios (condición necesaria y previa para la asignacion de recursos)
        self._ordenar_programas()     
        
        #Garantiza que al instanciar la clase, se calcule la asignacion
        self.asignar_recursos()
        #Identificar los programas con cupos disponibles después de la asignacion
        self._identificar_programas_disponibles()

        
    def asignar_recursos(self):
        """
        TODO :  Completar documentación
        
        Asigna recursos a programas de grupos cerrados hasta agotar el saldo total disponible.
    
        Retorna:
            pd.DataFrame: DataFrame con columnas de cupos y recursos asignados, y el saldo restante.
        """
        data = self.data.copy()
        
        data['cupos_asignados_2E'] = 0  
        data['recurso_asignado_2E'] = 0.0
        data['saldo_total_remanente'] = 0.0
    
    
        saldo_total = self.recursos_iniciales
    
        for idx, row in data.iterrows():
            costo = row[COLUMNA_VALOR_PROGRAMA]
            cupos = min(row['numero_cupos_ofertar'], row[COLUMNA_CUPOS_MAXIMOS])

            #TO DO: esta condicion debería ser parte del contrato de la clase AsignacionBase()
            if pd.isna(costo) or costo <= 0 or pd.isna(cupos) or cupos <= 0:
                data.at[idx, 'saldo_total_remanente'] = saldo_total
                continue
    
            recurso_necesario = costo * cupos
    
            if saldo_total >= recurso_necesario:
                data.at[idx, 'cupos_asignados_2E'] = cupos
                data.at[idx, 'recurso_asignado_2E'] = recurso_necesario
                saldo_total -= recurso_necesario
            else:
                
                cupos_posibles = saldo_total // costo
                recurso_asignado = cupos_posibles * costo
                
                data.at[idx, 'cupos_asignados_2E'] = cupos_posibles
                data.at[idx, 'recurso_asignado_2E'] = recurso_asignado
                saldo_total -= recurso_asignado
    
            data.at[idx, 'saldo_total_remanente'] = saldo_total
    
            if saldo_total <= 0:
                break
                
        # Paso 5: Calcular recursos asignados
        data['recurso_asignado_2E'] = data['cupos_asignados_2E'] * data[COLUMNA_VALOR_PROGRAMA]
        data['cupos_sobrantes_2E'] = data['numero_cupos_ofertar'] - data['cupos_asignados_2E']
        
        self.recursos_disponibles = saldo_total 
        self.recursos_asignados = self.recursos_iniciales - self.recursos_disponibles

        self.primera_asignacion = data

    def _ordenar_programas(self,usar_cod_cno=False):
        """
        Ordena los programas dentro del DataFrame según criterios establecidos.
        Si usar_cod_cno es True, cod_CNO se usará como primer criterio de orden.
        Actualiza self.data.
    
        Criterios de orden:
        1. (Opcional) cod_CNO
        2. Mayor puntaje
        3. Mayor número de cupos ofertados
        4. Mayor meta de vinculación
        5. Menor costo
        6. Menor duración
    .
    
        Retorna:
            pd.DataFrame: DataFrame ordenado según los criterios establecidos.
        """
        df = self.data.copy()
        
        columnas = []
        orden = []
    
        if usar_cod_cno:
            columnas.append('cod_CNO')
            orden.append(True)
    
        columnas += [
            'Puntaje (nuevos y cerrados)',
            'numero_cupos_ofertar',
            'Meta de vinculación',
            COLUMNA_VALOR_PROGRAMA,
            'duracion_horas_programa'
        ]
    
        orden += [False, False, False, True, True]
    
        self.data = df.sort_values(by=columnas, ascending=orden).reset_index(drop=True)

    def _identificar_programas_disponibles(self):
        """
        Identifica cuales programas después del la asignación quedaron con cupos disponibles.
        """        
        data = self.primera_asignacion.copy()
        
        grupos_cerrados_remanente = data[
            data['cupos_sobrantes_2E'] > 0
        ].reset_index(drop=True)

        self.programas_remanente = grupos_cerrados_remanente

    def __reasignar_remanente(self):
        """
        TODO: Implementar función.
        Propuesta: hacer la funcion asignar_recursos() reutilizable
        """
                