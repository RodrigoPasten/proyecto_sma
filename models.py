from pydantic import BaseModel
from typing import Annotated
from fastapi import Depends
# SQLMODEL
from sqlmodel import Field, Session, SQLModel, create_engine, select

# CREATING MODEL for DB
class Organismos(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    email: str = Field(default=None, index=True)
    sigla: str = Field(default=None, index=True)
    activo: bool = Field(default=True, index=True)
    
class Usuarios(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    email: str = Field(default=None, index=True)
    password: str = Field(default=None, index=True)
    rol: str = Field(default=None, index=True)
    activo: bool = Field(default=True, index=True)
    
    organismo_id: int | None = Field(default=None, foreign_key="organismos.id")
    
class Medidas(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    descripcion: str = Field(default=None, index=True)
    activo: bool = Field(default=True, index=True)
    
    organismo_id: int = Field(default=None, foreign_key="organismos.id")
    usuario_id: int = Field(default=None, foreign_key="usuarios.id")

class Indicadores(SQLModel, table= True):
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    tipo: str = Field(default=None, index=True)
    formula: str = Field(default=None, index=True)
    unidad: str = Field(default=None, index=True)
    activo: bool = Field(default=True, index=True)
    
    medida_id: int = Field(default=None, foreign_key="medidas.id")

class Reportes(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    fecha: str = Field(default=None, index=True)
    valor: int = Field(default=None, index=True)
    activo: bool = Field(default=True, index=True)
    
    indicador_id: int = Field(default=None, foreign_key="indicadores.id")
    organismo_id: int = Field(default=None, foreign_key="organismos.id")
    usuario_id: int = Field(default=None, foreign_key="usuarios.id")

# CREATE ENGINE TO CONNECT TO DB

database_user = "postgres"
database_password = "pgadmin"
database_host = "localhost"  # or the IP address of your PostgreSQL server
database_port = 5432         # Default PostgreSQL port
database_name = "db_sma"

postgres_url = f"postgresql://{database_user}:{database_password}@{database_host}:{database_port}/{database_name}"
engine = create_engine(postgres_url)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
def create_organismos():
    organismo_1 = Organismos(
        nombre="Ministerio de Salud", 
        email="contacto@minsalud.cl", 
        sigla="MINSAL"
    )
    organismo_2 = Organismos(
        nombre="Ministerio de Educación", 
        email="info@mineduc.cl", 
        sigla="MINEDUC"
    )
    organismo_3 = Organismos(
        nombre="Ministerio de Economía", 
        email="economia@mineco.cl", 
        sigla="MINECO"
    )

    # Replace `engine` with your actual database engine
    with Session(engine) as session:
        session.add(organismo_1)
        session.add(organismo_2)
        session.add(organismo_3)

        session.commit()

def create_usuarios():
    usuario_1 = Usuarios(
        nombre="Juan Pérez",
        email="juan.perez@example.com",
        password="securepassword123",
        rol="Administrador",
        organismo_id=1  # Assuming this Organismo exists
    )
    usuario_2 = Usuarios(
        nombre="María González",
        email="maria.gonzalez@example.com",
        password="mypassword456",
        rol="Usuario",
        organismo_id=2  # Assuming this Organismo exists
    )
    usuario_3 = Usuarios(
        nombre="Carlos López",
        email="carlos.lopez@example.com",
        password="password789",
        rol="Supervisor",
        organismo_id=1  # Assuming this Organismo exists
    )

    with Session(engine) as session:
        session.add(usuario_1)
        session.add(usuario_2)
        session.add(usuario_3)

        session.commit()

def create_medidas():
    medida_1 = Medidas(
        nombre="Medida 1",
        descripcion="Primera medida tomada para mejorar los procesos.",
        organismo_id=1,  # Assuming this Organismo exists
        usuario_id=1     # Assuming this Usuario exists
    )
    medida_2 = Medidas(
        nombre="Medida 2",
        descripcion="Medida de contingencia aplicada en 2023.",
        organismo_id=2,  # Assuming this Organismo exists
        usuario_id=2     # Assuming this Usuario exists
    )
    medida_3 = Medidas(
        nombre="Medida 3",
        descripcion="Estrategia de optimización de recursos.",
        organismo_id=1,  # Assuming this Organismo exists
        usuario_id=3     # Assuming this Usuario exists
    )

    with Session(engine) as session:
        session.add(medida_1)
        session.add(medida_2)
        session.add(medida_3)

        session.commit()

def create_indicadores():
    indicador_1 = Indicadores(
        nombre="Indicador de Rendimiento",
        tipo="Porcentaje",
        formula="(logros / metas) * 100",
        unidad="%",
        activo=True,
        medida_id=1  # Assuming this Medida exists
    )
    indicador_2 = Indicadores(
        nombre="Indicador de Productividad",
        tipo="Ratio",
        formula="producción / horas_trabajadas",
        unidad="unidades/hora",
        activo=True,
        medida_id=2  # Assuming this Medida exists
    )
    indicador_3 = Indicadores(
        nombre="Indicador de Eficiencia",
        tipo="Porcentaje",
        formula="(resultados / recursos) * 100",
        unidad="%",
        activo=False,
        medida_id=3  # Assuming this Medida exists
    )

    with Session(engine) as session:
        session.add(indicador_1)
        session.add(indicador_2)
        session.add(indicador_3)

        session.commit()

def create_reportes():
    reporte_1 = Reportes(
        fecha="2025-01-15",
        valor=85,
        activo=True,
        indicador_id=1,  # Assuming this Indicador exists
        organismo_id=1,  # Assuming this Organismo exists
        usuario_id=1     # Assuming this Usuario exists
    )
    reporte_2 = Reportes(
        fecha="2025-01-16",
        valor=90,
        activo=True,
        indicador_id=2,  # Assuming this Indicador exists
        organismo_id=2,  # Assuming this Organismo exists
        usuario_id=2     # Assuming this Usuario exists
    )
    reporte_3 = Reportes(
        fecha="2025-01-17",
        valor=70,
        activo=False,
        indicador_id=3,  # Assuming this Indicador exists
        organismo_id=1,  # Assuming this Organismo exists
        usuario_id=3     # Assuming this Usuario exists
    )

    with Session(engine) as session:
        session.add(reporte_1)
        session.add(reporte_2)
        session.add(reporte_3)

        session.commit()


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]