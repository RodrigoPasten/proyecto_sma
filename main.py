from fastapi import FastAPI, HTTPException, status, APIRouter
from contextlib import asynccontextmanager
from models import (
    medidas,
    usuarios,
    organismos,
    Medidas,
    Usuarios,
    Organismos,
    create_db_and_tables,
    create_organismos,
    create_usuarios,
    create_medidas,
    create_indicadores,
    create_reportes
)

""" @asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    create_db_and_tables
    yield
    # Clean up the ML models and release the resources
    # create_db_and_tables.clear() """

app = FastAPI(
    title="Sistema de Monitoreo PPDA CQP",
    description="""
    API para gestionar reportes de organismos responsables del Plan de Prevención y Descontaminación Atmosférica (PPDA).
    Permite registrar, consultar y visualizar los avances del plan.
    """,
    version="1.0.0",
    contact={
        "name": "Superintendencia del Medio Ambiente",
        "email": "grupo5@talentofuturo.cl",
    },
    #lifespan=lifespan
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    create_organismos()
    create_usuarios(),
    create_medidas(),
    create_indicadores(),
    create_reportes()
    
router = APIRouter()

# CRUD REPORTES

""" @app.get("/reportes/{reporte_id}", response_model=Reportes, tags=["Reportes"])
async def obtener_reporte(reporte_id: int):
    reporte = next((r for r in reportes if r.id == reporte_id), None)

    if reporte is None:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")

    return reporte


@app.get("/reportes", response_model=list[Reportes])
async def obtener_reportes():
    return reportes


@app.get("/reportes_activos", response_model=list[Reportes])
async def obtener_reportes_activos():
    reportes_activos = [r for r in reportes if r.activo]
    return reportes_activos


@app.post("/reportes", response_model=Reportes, status_code=status.HTTP_201_CREATED)
async def crear_reporte(reporte: Reportes):
    if reporte not in reportes:
        reportes.append(reporte)
        return reporte
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El reporte ingresado con ID {reporte.id} ya existe",
        )


@app.delete("/reportes/{reporte_id}")
async def desactivar_reporte(reporte_id: int):
    reporte = next((r for r in reportes if r.id == reporte_id), None)
    if reporte is None:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")

    reporte.activo = False

    return f"Se ha eliminado el reporte {reporte_id}" """


# CRUD MEDIDAS


@app.get("/medidas/{medida_id}", response_model=Medidas)
async def obtener_medida(medida_id: int):
    medida = next((r for r in medidas if r.id == medida_id), None)

    if medida is None:
        raise HTTPException(status_code=404, detail="Medida no encontrada")

    return medida


@app.get("/medidas", response_model=list[Medidas])
async def obtener_medidas():
    return medidas


@app.get("/medidas_activos", response_model=list[Medidas])
async def obtener_medidas_activos():
    medidas_activos = [r for r in medidas if r.activo]
    return medidas_activos


@app.post("/medidas", response_model=Medidas, status_code=status.HTTP_201_CREATED)
async def crear_medida(medida: Medidas):
    if medida not in medidas:
        medidas.append(medida)
        return medida
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"La medida ingresada con ID {medida.id} ya existe",
        )


@app.delete("/medidas/{medida_id}")
async def desactivar_medida(medida_id: int):
    medida = next((r for r in medidas if r.id == medida_id), None)
    if medida is None:
        raise HTTPException(status_code=404, detail="Medida no encontrada")

    medida.activo = False

    return f"Se ha eliminado la medida {medida_id}"


# CRUD USUARIO


@app.get("/usuarios/{usuario_id}", response_model=Usuarios)
async def obtener_usuario(usuario_id: int):
    usuario = next((r for r in usuarios if r.id == usuario_id), None)

    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return usuario


@app.get("/usuarios", response_model=list[Usuarios])
async def obtener_usuarios():
    return usuarios


@app.get("/usuarios_activos", response_model=list[Usuarios])
async def obtener_usuarios_activos():
    usuarios_activos = [r for r in usuarios if r.activo]
    return usuarios_activos


@app.post("/usuarios", response_model=Usuarios, status_code=status.HTTP_201_CREATED)
async def crear_usuario(usuario: Usuarios):
    if usuario not in usuarios:
        usuarios.append(usuario)
        return usuario
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El usuario ingresado con ID {usuario.id} ya existe",
        )


@app.delete("/usuarios/{usuario_id}")
async def desactivar_usuario(usuario_id: int):
    usuario = next((r for r in usuarios if r.id == usuario_id), None)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario.activo = False

    return f"Se ha eliminado el usuario {usuario_id}"


# CRUD ORGANISMOS


@app.get("/organismos/{organismo_id}", response_model=Organismos)
async def obtener_organismo(organismo_id: int):
    organismo = next((r for r in organismos if r.id == organismo_id), None)

    if organismo is None:
        raise HTTPException(status_code=404, detail="Organismo no encontrado")

    return organismo


@app.get("/organismos", response_model=list[Organismos])
async def obtener_organismos():
    return organismos


@app.get("/organismos_activos", response_model=list[Organismos])
async def obtener_organismos_activos():
    organismos_activos = [r for r in organismos if r.activo]
    return organismos_activos


@app.post("/organismos", response_model=Organismos, status_code=status.HTTP_201_CREATED)
async def crear_organismo(organismo: Organismos):
    if organismo not in organismos:
        organismos.append(organismo)
        return organismo
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El organismo ingresado con ID {organismo.id} ya existe",
        )


@app.delete("/organismos/{organismo_id}")
async def desactivar_organismo(organismo_id: int):
    organismo = next((r for r in organismos if r.id == organismo_id), None)
    if organismo is None:
        raise HTTPException(status_code=404, detail="Organismo no encontrado")

    organismo.activo = False

    return f"Se ha eliminado el organismo {organismo_id}"


# CRUD INDICADORES


""" @app.get("/indicadores/{indicador_id}", response_model=Indicadores)
async def obtener_indicador(indicador_id: int):
    indicador = next((r for r in indicadores if r.id == indicador_id), None)

    if indicador is None:
        raise HTTPException(status_code=404, detail="Indicador no encontrado")

    return indicador


@app.get("/indicadores", response_model=list[Indicadores])
async def obtener_indicadors():
    return indicadores


@app.get("/indicadores_activos", response_model=list[Indicadores])
async def obtener_indicadors_activos():
    indicadors_activos = [r for r in indicadores if r.activo]
    return indicadors_activos


@app.post(
    "/indicadores", response_model=Indicadores, status_code=status.HTTP_201_CREATED
)
async def crear_indicador(indicador: Indicadores):
    if indicador not in indicadores:
        indicadores.append(indicador)
        return indicador
    else:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"El indicador ingresado con ID {indicador.id} ya existe",
        )


@app.delete("/indicadores/{indicador_id}")
async def desactivar_indicador(indicador_id: int):
    indicador = next((r for r in indicadores if r.id == indicador_id), None)
    if indicador is None:
        raise HTTPException(status_code=404, detail="Indicador no encontrado")

    indicador.activo = False

    return f"Se ha eliminado el indicador {indicador_id}" """
