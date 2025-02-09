from pydantic import BaseModel

    
class Medidas(BaseModel):
    id: int
    nombre: str
    descripcion: str
    organismo_id: int
    usuario_id: int
    activo: bool

class Reportes(BaseModel):
    id: int
    fecha: str
    indicador_id: int
    organismo_id: int
    valor: int
    usuario_id: int
    activo: bool

class Usuarios(BaseModel):
    id: int
    nombre: str
    email: str
    password: str
    organismo_id: int
    rol: str
    activo: bool
    
class Organismos(BaseModel):
    id: int
    nombre: str
    sigla: str
    activo: bool

class Indicadores(BaseModel):
    id: int
    nombre: str
    tipo: str
    formula: str
    unidad: str
    medida_id: int
    activo: bool

medidas = [
    Medidas(id=1, nombre="Medida 1", descripcion="Descripción de la Medida 1", organismo_id=1, usuario_id=1, activo=True),
    Medidas(id=2, nombre="Medida 2", descripcion="Descripción de la Medida 2", organismo_id=2, usuario_id=2, activo=True),
    Medidas(id=3, nombre="Medida 3", descripcion="Descripción de la Medida 3", organismo_id=1, usuario_id=3, activo=True),
]

reportes = [
    Reportes(id=1, fecha="2025-02-01", indicador_id=1, organismo_id=1, valor=100, usuario_id=1, activo=True),
    Reportes(id=2, fecha="2025-02-02", indicador_id=2, organismo_id=2, valor=200, usuario_id=2, activo=True),
    Reportes(id=3, fecha="2025-02-03", indicador_id=3, organismo_id=3, valor=300, usuario_id=3, activo=True),
]

usuarios = [
    Usuarios(id=1, nombre="Usuario 1", email="usuario1@example.com", password="password1", organismo_id=1, rol="Admin", activo=True),
    Usuarios(id=2, nombre="Usuario 2", email="usuario2@example.com", password="password2", organismo_id=2, rol="User", activo=True),
    Usuarios(id=3, nombre="Usuario 3", email="usuario3@example.com", password="password3", organismo_id=3, rol="User", activo=True),
]

organismos = [
    Organismos(id=1, nombre="Organismo 1", sigla="ORG1", activo=True),
    Organismos(id=2, nombre="Organismo 2", sigla="ORG2", activo=True),
    Organismos(id=3, nombre="Organismo 3", sigla="ORG3", activo=True),
]

indicadores = [
    Indicadores(id=1, nombre="Indicador 1", tipo="Proporción", formula="a/b", unidad="%", medida_id=1, activo=True),
    Indicadores(id=2, nombre="Indicador 2", tipo="Tasa", formula="c*d", unidad="unidades", medida_id=2, activo=True),
    Indicadores(id=3, nombre="Indicador 3", tipo="Índice", formula="e/f", unidad="índice", medida_id=3, activo=True),
]