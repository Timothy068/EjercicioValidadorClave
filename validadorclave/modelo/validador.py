# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod


class ReglaValidacion(ABC):

    def __init__(self, longitud_esperada: int):
        self.longitud_esperada_: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if self.longitud_esperada_ == clave:
            return True

    def _contiene_mayusculas(self, clave: str) -> bool:
        return clave.isupper()

    def _contiene_minusculas(self, clave: str) -> bool:
        return clave.islower()

    def _contiene_numero(self, clave: str) -> bool:
        return clave.isdigit()

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):

    def __init__(self, longitud_esperada: int):
        super().__init__(longitud_esperada)

    def contiene_caracter_especial(self, clave: str) -> bool:
        especiales = "@_#$%"
        for caracter in clave:
            if caracter in especiales:
                return True

    def es_valida(self, clave: str) -> bool:
        super().es_valida(clave)
        if super()._validar_longitud(clave):
            if super()._contiene_mayusculas(clave):
                if super()._contiene_minusculas(clave):
                    if super()._contiene_numero(clave):
                        if self.contiene_caracter_especial(clave):
                            return True


class ReglaValidacionCalisto(ReglaValidacion):

    def __init__(self, longitud_esperada: int):
        super().__init__(longitud_esperada)

    def contiene_calisto(self, clave: str) -> bool:
        mayusculas = 0
        if "calisto" in clave:
            for i in clave:
                if i.isupper():
                    mayusculas += 1

        if mayusculas >= 2 and mayusculas != len(clave):
            return True

    def es_valida(self, clave: str) -> bool:
        super().es_valida(clave)
        if super()._validar_longitud(clave):
            if super()._contiene_numero(clave):
                if self.contiene_calisto(clave):
                    return True


class Validador:

    def __init__(self, regla: ReglaValidacion):
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool:
        pass

