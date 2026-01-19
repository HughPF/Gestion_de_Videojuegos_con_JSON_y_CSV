"""
Paquete gestor de videojuegos.

Contiene la lógica principal del catálogo:
- Operaciones CRUD
- Búsquedas
- Estadísticas
"""

from .catalogo import crear, leer, eliminar
from .busquedas import (
    buscar_exacto,
    buscar_parcial,
    buscar_por_genero
)
from .estadisticas import (
    total_videojuegos,
    conteo_por_genero
)
