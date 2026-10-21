from datetime import date

# ConfigDict: from_attributes=True permite crear el schema desde un objeto SQLAlchemy
# Field: validaciones por campo (max_length, gt, lt, etc.)
from pydantic import BaseModel, ConfigDict, Field


# Respuesta con los datos completos del perfil
class ProfileResponse(BaseModel):
    # Permite que Pydantic cree el schema desde un objeto SQLAlchemy
    model_config = ConfigDict(from_attributes=True)

    id: int
    birth_date: date
    biological_sex: str
    height_cm: float
    current_weight_kg: float
    goal: str
    activity_level: str


# Datos que el usuario puede actualizar (todo opcional)
class ProfileUpdate(BaseModel):
    birth_date: date | None = None
    biological_sex: str | None = Field(None, max_length=20)
    height_cm: float | None = Field(None, gt=0, lt=300)
    current_weight_kg: float | None = Field(None, gt=0, lt=500)
    goal: str | None = Field(None, max_length=50)
    activity_level: str | None = Field(None, max_length=50)
