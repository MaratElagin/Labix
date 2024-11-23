from pydantic import BaseModel
from typing import Optional, Union


class Syndrome(BaseModel):
    system: str
    problems: list[str]


class AnalyseData(BaseModel):
    marker: str
    value: float
    normal: str
    unitOfMeasurement: str
    problem: str | None
    syndromes: list[dict[str, str]] | None


class PatientData(BaseModel):
    fio: str = ""
    snils: str
    analyzes: list[AnalyseData]
    syndromes: Optional[list[Syndrome]]

    class Config:
        json_schema_extra = {
            "example": {
                "fio": "Иванов Иван Иванович",
                "snils": "11142234",
                "analyzes": [
                    {
                        "marker": "СРБ",
                        "value": 12.5,
                        "normal": "0-6",
                        "unitOfMeasurement": "ммHg",
                        "problem": "Аллергическая сенсибилизация",
                    },
                ],
                "syndromes": [
                    {
                        "system": "Иммунная система",
                        "problems": [
                            "Аллергическая сенсибилизация",
                            "Воспалительный ответ",
                        ],
                    }
                ],
            }
        }
