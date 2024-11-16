import uuid

from fastapi import FastAPI, HTTPException, status

app = FastAPI()


@app.get("/")
async def root():
    return "OK"


@app.get("/api/health")
async def health_check():
    return "OK"


@app.get("/plants/{plant_uuid}")
async def get_plant(plant_uuid: str):
    """Get a plant details by its uuid."""
    if plant_uuid in ["1", str(uuid.UUID(int=0))]:
        return {"plant_id": plant_uuid, "plant_name": "Thai"}

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f'Plant "{plant_uuid}" not found'
    )
