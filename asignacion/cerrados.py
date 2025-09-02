import pandas as pd
from . import constants
from .base import AsignacionBase

from .constants import RECURSOS_POR_RUTA

class AsignacionCerrados(AsignacionBase):
    """
    ## TODO: Terminar de escribir el objetivo de la clase
    Clase encargada de gestionar la asignación de recursos para la ruta 'Cerrados'.
    """

    def __init__(self, data, recursos_iniciales =  None, col_cupos_reemplazo = "numero_cupos_ofertar"):
        
        if recursos_iniciales:
            super().__init__(recursos_iniciales)
        else:
            super().__init__(RECURSOS_POR_RUTA["cerrados"])
        
        self.data = data
        self.primera_asignacion = pd.DataFrame()
        
        #Ordenamos programas siguiendo criterios (condición necesaria y previa para la asignacion de recursos)
        self._ordenar_programas(col_cupos_reemplazo = col_cupos_reemplazo)     
        
        #Garantiza que al instanciar la clase, se calcule la asignacion
        self.asignar_recursos()
        #Identificar los programas con cupos_disp disponibles después de la asignacion
        self._identificar_programas_disponibles()

        
    def asignar_recursos(self):
        """
        TODO :  Completar documentación
        
        Asigna recursos a programas de grupos cerrados hasta agotar el saldo total disponible.
    
        Retorna:
            pd.DataFrame: DataFrame con columnas de cupos_disp y recursos asignados, y el saldo restante.
        """
        data = self.data.copy()
        
        data['cupos_asignados'] = 0  
        data['recurso_asignado'] = 0.0
        #data['saldo_total_remanente'] = 0.0
    
    
        saldo_total = self.recursos_iniciales
    
        for idx, row in data.iterrows():
            costo_unitario = row['valor_programa']
            cupos_disp = row['numero_cupos_ofertar']
            cupos_minimos_disp = row['numero_minimo_cupos']

            #TO DO: esta condicion debería ser parte del contrato de la clase AsignacionBase()
            if pd.isna(costo_unitario) or costo_unitario <= 0 or pd.isna(cupos_disp) or cupos_disp <= 0:
                #data.at[idx, 'saldo_total_remanente'] = saldo_total
                continue
    
            recurso_necesario = costo_unitario * cupos_disp
            recurso_necesario_minimo = cupos_minimos_disp * costo_unitario
    
            if saldo_total >= recurso_necesario:
                #El saldo es suficiente para financiar todos los cupos
                data.at[idx, 'cupos_asignados'] = cupos_disp
                data.at[idx, 'recurso_asignado'] = recurso_necesario
                saldo_total -= recurso_necesario
                
            elif recurso_necesario >= saldo_total >= recurso_necesario_minimo:
                
                cupos_posibles = saldo_total // costo_unitario
                recurso_asignado = cupos_posibles * costo_unitario
                
                data.at[idx, 'cupos_asignados'] = cupos_posibles
                data.at[idx, 'recurso_asignado'] = recurso_asignado
                saldo_total -= recurso_asignado
            else:
                #El saldo no es suficiente: continuar con el siguiente programa priorizado  
                data.at[idx, 'cupos_asignados'] = 0
                data.at[idx, 'recurso_asignado'] = 0
    
            #data.at[idx, 'saldo_total_remanente'] = saldo_total
    
            if saldo_total <= 0:
                break
                
        # Paso 5: Calcular recursos asignados
        data['recurso_asignado'] = data['cupos_asignados'] * data['valor_programa']
        data['cupos_sobrantes'] = data['numero_cupos_ofertar'] - data['cupos_asignados']
        
        self.recursos_disponibles = saldo_total 
        self.recursos_asignados = self.recursos_iniciales - self.recursos_disponibles

        self.primera_asignacion = data

    def _ordenar_programas(self,usar_cod_cno=False, col_cupos_reemplazo = "numero_cupos_ofertar" ):
        """
        Ordena los programas dentro del DataFrame según criterios establecidos.
        Si usar_cod_cno es True, cod_CNO se usará como primer criterio de orden.
        Actualiza self.data.
    
        Criterios de orden:
        1. (Opcional) cod_CNO
        2. Mayor puntaje
        3. Mayor número de cupos_disp ofertados
        4. Mayor meta de vinculación
        5. Menor costo_unitario
        6. Menor duración
        7. IPO
        8. ISOEFT
    .
        Params:
            col_cupos_reemplazo: Distingue la columna original de numero_cupos_ofertar
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
            'puntaje',
            col_cupos_reemplazo,
            'meta_vinculacion',
            'valor_programa',
            'duracion_horas_programa',
            'ipo',
            'isoeft'
        ]
    
        orden += [False, False, False, True, True, False, False]
    
        self.data = (
            df.sort_values(by=columnas, ascending=orden)
                .reset_index(drop=True)
                .assign(orden_priorizacion=lambda x: range(1, len(x)+1))
        )

    def _identificar_programas_disponibles(self):
        """
        Identifica cuales programas después del la asignación quedaron con cupos_disp disponibles.
        """        
        data = self.primera_asignacion.copy()
        
        grupos_cerrados_remanente = data[
            data['cupos_sobrantes'] > 0
        ]#.reset_index(drop=True)

        self.programas_remanente = grupos_cerrados_remanente

    def __reasignar_remanente(self):
        """
        TODO: Implementar función.
        Propuesta: hacer la funcion asignar_recursos() reutilizable
        """
                