from pydantic import BaseModel

class Report(BaseModel):
    id: int
    nombre: str
    descripcion: str
    observacion: str
    fecha: str
    activo: bool
    
class Medidas(BaseModel):
    id: int
    nombre: str
    descripcion: str
    observacion: str
    fecha: str
    activo: bool
    reporte_id: int

reportes = [
    Report(id=1, nombre="Reporte 1", descripcion="Descripción del reporte 1", observacion="Observación 1", fecha="2025-02-01", activo=True),
    Report(id=2, nombre="Reporte 2", descripcion="Descripción del reporte 2", observacion="Observación 2", fecha="2025-02-02", activo=True),
    Report(id=3, nombre="Reporte 3", descripcion="Descripción del reporte 3", observacion="Observación 3", fecha="2025-02-03", activo=True),
    Report(id=4, nombre="Reporte 4", descripcion="Descripción del reporte 4", observacion="Observación 4", fecha="2025-02-03", activo=False),
]
