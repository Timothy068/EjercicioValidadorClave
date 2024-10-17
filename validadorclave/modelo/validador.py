# TODO: Implementa el código del ejercicio aquí
from abc import ABC, abstractmethod


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada_: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> None:
        if len(clave) <= self.longitud_esperada_:
            raise ReglaValidacionGanimedesException("La clave debe tener una longitud de más de {} caracteres".format(self.longitud_esperada_))

    def _contiene_mayusculas(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minusculas(self, clave: str) -> bool:
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        especiales = "@_#$%"
        return any(c in especiales for c in clave)

    def es_valida(self, clave: str) -> bool:
        self._validar_longitud(clave)
        if not self._contiene_mayusculas(clave):
            raise ReglaValidacionGanimedesException("La clave debe contener al menos una letra mayúscula")
        if not self._contiene_minusculas(clave):
            raise ReglaValidacionGanimedesException("La clave debe contener al menos una letra minúscula")
        if not self._contiene_numero(clave):
            raise ReglaValidacionGanimedesException("La clave debe contener al menos un número")
        if not self.contiene_caracter_especial(clave):
            raise ReglaValidacionGanimedesException("La clave debe contener al menos un caracter especial (@, _, #, $, %)")
        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(6)

    def contiene_calisto(self, clave: str) -> bool:
        mayusculas = sum(1 for c in clave if c in 'CALISTO' and c.isupper())
        return 1 < mayusculas < len('CALISTO')

    def es_valida(self, clave: str) -> bool:
        self._validar_longitud(clave)
        if not self._contiene_numero(clave):
            raise ReglaValidacionCalistoException("La clave debe contener al menos un número")
        if not self.contiene_calisto(clave):
            raise ReglaValidacionCalistoException("La palabra 'calisto' debe estar escrita con al menos dos letras en mayúscula")
        return True


class Validador:
    def __init__(self, regla: ReglaValidacion):
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool:
        return self.regla.es_valida(clave)
