from fastapi import FastAPI, HTTPException
from models import reportes, Report

app = FastAPI()


@app.get("/reportes/{reporte_id}", response_model=Report)
async def obtener_reporte(reporte_id: int):
    reporte = next((r for r in reportes if r.id == reporte_id), None)

    if reporte is None:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")

    return reporte


@app.get("/reportes", response_model=list[Report])
async def obtener_reportes():
    return reportes


@app.get("/reportes_activos", response_model=list[Report])
async def obtener_reportes_activos():
    reportes_activos = [r for r in reportes if r.activo]
    return reportes_activos


@app.post("/reportes", response_model=Report)
async def crear_reporte(reporte: Report):
    reportes.append(reporte)
    return reporte


@app.patch("/reportes/{reporte_id}")
async def desactivar_reporte(reporte_id: int):
    reporte = next((r for r in reportes if r.id == reporte_id), None)
    if reporte is None:
        raise HTTPException(status_code=404, detail="Reporte no encontrado")

    reporte.activo = False

    return f"Se ha eliminado el reporte {reporte_id}"
