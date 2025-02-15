from fastapi import FastAPI, HTTPException, status, APIRouter
from contextlib import asynccontextmanager
from sqlmodel import Session, select
from models import (
    Medidas,
    Usuarios,
    Organismos,
    Indicadores,
    Reportes,
    create_db_and_tables,
    create_organismos,
    create_usuarios,
    create_medidas,
    create_indicadores,
    create_reportes,
    engine,
    SessionDep,
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
    🌱 **API para gestionar reportes de organismos responsables del Plan de Prevención y Descontaminación Atmosférica (PPDA).**  
    📊 Permite registrar, consultar y visualizar los avances del plan de forma eficiente.
    """,
    version="1.0.0",
    terms_of_service="https://www.sma.gob.cl/terminos",
    contact={
        "name": "Superintendencia del Medio Ambiente",
        "email": "grupo5@talentofuturo.cl",
        "url": "https://www.sma.gob.cl",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    swagger_ui_parameters={
        "defaultModelsExpandDepth": -1,  # Oculta los modelos de la vista inicial
        "theme": "dark",
        "defaultModelRendering": "example",  # Muestra ejemplos en lugar de esquemas JSON
        "displayRequestDuration": True,  # Muestra el tiempo de respuesta
        "docExpansion": "none",  # Mantiene los endpoints colapsados
        "filter": True,  # Agrega un cuadro de búsqueda en los endpoints
    },
)
from fastapi.openapi.docs import get_redoc_html




@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    create_organismos()
    (create_usuarios(),)
    (create_medidas(),)
    (create_indicadores(),)
    create_reportes()


router = APIRouter()

# CRUD REPORTES


@app.get("/reportes/{reporte_id}", response_model=Reportes, tags=["Reportes"])
async def obtener_reporte(reporte_id: int):
    with Session(engine) as session:
        reporte = session.get(Reportes, reporte_id)
        if not reporte:
            raise HTTPException(status_code=404, detail="Reporte no encontrado")
        return reporte


@app.get("/reportes", response_model=list[Reportes], tags=["Reportes"])
async def obtener_reportes():
    with Session(engine) as session:
        reportes = session.exec(select(Reportes)).all()
        return reportes


@app.get("/reportes_activos", response_model=list[Reportes], tags=["Reportes"])
async def obtener_reportes_activos():
    with Session(engine) as session:
        reportes = session.exec(select(Reportes).where(Reportes.activo)).all()
        return reportes


@app.post(
    "/reportes",
    response_model=Reportes,
    status_code=status.HTTP_201_CREATED,
    tags=["Reportes"],
)
async def crear_reporte(reporte: Reportes):
    with Session(engine) as session:
        reportes = session.exec(select(Reportes)).all()
        if reporte not in reportes:
            db_reporte = Reportes.model_validate(reporte)
            session.add(db_reporte)
            session.commit()
            session.refresh(db_reporte)
            return db_reporte
        else:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"El reporte ingresado con ID {reporte.id} ya existe",
            )


@app.delete("/reportes/{reporte_id}", tags=["Reportes"])
async def desactivar_reporte(reporte_id: int, session: SessionDep):
    reporte_db = session.get(Reportes, reporte_id)
    if not reporte_db:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")
    reporte_db.activo = False
    session.add(reporte_db)
    session.commit()
    session.refresh(reporte_db)

    return {"message": f"Se ha desactivado el reporte {reporte_id}"}


# CRUD MEDIDAS


@app.get("/medidas/{medida_id}", response_model=Medidas, tags=["Medidas"])
async def obtener_medida(medida_id: int):
    with Session(engine) as session:
        medida = session.get(Medidas, medida_id)
        if medida is None:
            raise HTTPException(status_code=404, detail="Medida no encontrada")
        return medida


@app.get("/medidas", response_model=list[Medidas], tags=["Medidas"])
async def obtener_medidas():
    with Session(engine) as session:
        medidas = session.exec(select(Medidas)).all()
        return medidas


@app.get("/medidas_activos", response_model=list[Medidas], tags=["Medidas"])
async def obtener_medidas_activos():
    with Session(engine) as session:
        medidas_activas = session.exec(select(Medidas).where(Medidas.activo)).all()
        return medidas_activas


@app.post(
    "/medidas",
    response_model=Medidas,
    status_code=status.HTTP_201_CREATED,
    tags=["Medidas"],
)
async def crear_medida(medida: Medidas):
    with Session(engine) as session:
        medidas = session.exec(select(Medidas)).all()
        if medida not in medidas:
            db_medida = Medidas.model_validate(medida)
            session.add(db_medida)
            session.commit()
            session.refresh(db_medida)
            return db_medida
        else:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"La medida ingresada con ID {medida.id} ya existe",
            )


@app.delete("/medidas/{medida_id}", tags=["Medidas"])
async def desactivar_medida(medida_id: int, session: SessionDep):
    medida_db = session.get(Medidas, medida_id)
    if not medida_db:
        raise HTTPException(status_code=404, detail="Medida no encontrada")
    medida_db.activo = False
    session.add(medida_db)
    session.commit()
    session.refresh(medida_db)

    return {"message": f"Se ha eliminado la medida {medida_id}"}


# CRUD USUARIO


@app.get("/usuarios/{usuario_id}", response_model=Usuarios, tags=["Usuarios"])
async def obtener_usuario(usuario_id: int):
    with Session(engine) as session:
        usuario = session.get(Usuarios, usuario_id)
        if usuario is None:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return usuario


@app.get("/usuarios", response_model=list[Usuarios], tags=["Usuarios"])
async def obtener_usuarios():
    with Session(engine) as session:
        usuarios = session.exec(select(Usuarios)).all()
        return usuarios


@app.get("/usuarios_activos", response_model=list[Usuarios], tags=["Usuarios"])
async def obtener_usuarios_activos():
    with Session(engine) as session:
        usuarios = session.exec(select(Usuarios).where(Usuarios.activo)).all()
        return usuarios


@app.post(
    "/usuarios",
    response_model=Usuarios,
    status_code=status.HTTP_201_CREATED,
    tags=["Usuarios"],
)
async def crear_usuario(usuario: Usuarios):
    with Session(engine) as session:
        usuarios = session.exec(select(Usuarios)).all()
        if usuario not in usuarios:
            db_usuario = Usuarios.model_validate(usuario)
            session.add(db_usuario)
            session.commit()
            session.refresh(db_usuario)
            return db_usuario
        else:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"El usuario ingresado con ID {usuario.id} ya existe",
            )


@app.delete("/usuarios/{usuario_id}", tags=["Usuarios"])
async def desactivar_usuario(usuario_id: int, session: SessionDep):
    usuario_db = session.get(Usuarios, usuario_id)
    if not usuario_db:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    usuario_db.activo = False
    session.add(usuario_db)
    session.commit()
    session.refresh(usuario_db)

    return {"message": f"Se ha eliminado el usuario {usuario_id}"}


# CRUD ORGANISMOS


@app.get("/organismos/{organismo_id}", response_model=Organismos, tags=["Organismos"])
async def obtener_organismo(organismo_id: int):
    with Session(engine) as session:
        organismo = session.get(Organismos, organismo_id)
        if organismo is None:
            raise HTTPException(status_code=404, detail="Organismo no encontrado")
        return organismo


@app.get("/organismos", response_model=list[Organismos], tags=["Organismos"])
async def obtener_organismos():
    with Session(engine) as session:
        organismos = session.exec(select(Organismos)).all()
        return organismos


@app.get("/organismos_activos", response_model=list[Organismos], tags=["Organismos"])
async def obtener_organismos_activos():
    with Session(engine) as session:
        organismos = session.exec(select(Organismos).where(Organismos.activo)).all()
        return organismos


@app.post(
    "/organismos",
    response_model=Organismos,
    status_code=status.HTTP_201_CREATED,
    tags=["Organismos"],
)
async def crear_organismo(organismo: Organismos):
    with Session(engine) as session:
        organismos = session.exec(select(Organismos)).all()
        if organismo not in organismos:
            db_organismo = Organismos.model_validate(organismo)
            session.add(db_organismo)
            session.commit()
            session.refresh(db_organismo)
            return db_organismo
        else:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"El organismo ingresado con ID {organismo.id} ya existe",
            )


@app.delete("/organismos/{organismo_id}", tags=["Organismos"])
async def desactivar_organismo(organismo_id: int, session: SessionDep):
    organismo_db = session.get(Organismos, organismo_id)
    if not organismo_db:
        raise HTTPException(status_code=404, detail="Organismo no encontrado")
    organismo_db.activo = False
    session.add(organismo_db)
    session.commit()
    session.refresh(organismo_db)

    return {"message": f"Se ha eliminado el organismo {organismo_id}"}


# CRUD INDICADORES


@app.get(
    "/indicadores/{indicador_id}", response_model=Indicadores, tags=["Indicadores"]
)
async def obtener_indicador(indicador_id: int):
    with Session(engine) as session:
        indicador = session.get(Indicadores, indicador_id)
        if indicador is None:
            raise HTTPException(status_code=404, detail="Indicador no encontrado")
        return indicador


@app.get("/indicadores", response_model=list[Indicadores], tags=["Indicadores"])
async def obtener_indicadors():
    with Session(engine) as session:
        indicadores = session.exec(select(Indicadores)).all()
        return indicadores


@app.get("/indicadores_activos", response_model=list[Indicadores], tags=["Indicadores"])
async def obtener_indicadors_activos():
    with Session(engine) as session:
        indicadores = session.exec(select(Indicadores).where(Indicadores.activo)).all()
        return indicadores


@app.post(
    "/indicadores",
    response_model=Indicadores,
    status_code=status.HTTP_201_CREATED,
    tags=["Indicadores"],
)
async def crear_indicador(indicador: Indicadores):
    with Session(engine) as session:
        indicadores = session.exec(select(Indicadores)).all()
        if indicador not in indicadores:
            db_indicador = Indicadores.model_validate(indicador)
            session.add(db_indicador)
            session.commit()
            session.refresh(db_indicador)
            return db_indicador
        else:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"El indicador ingresado con ID {indicador.id} ya existe",
            )


@app.delete("/indicadores/{indicador_id}", tags=["Indicadores"])
async def desactivar_indicador(indicador_id: int, session: SessionDep):
    indicador_db = session.get(Indicadores, indicador_id)
    if not indicador_db:
        raise HTTPException(status_code=404, detail="Indicador no encontrado")
    indicador_db.activo = False
    session.add(indicador_db)
    session.commit()
    session.refresh(indicador_db)

    return {"message": f"Se ha eliminado el indicador {indicador_id}"}
