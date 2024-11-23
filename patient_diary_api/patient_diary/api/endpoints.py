import json
import os
import pandas as pd
from pathlib import Path
from ninja import NinjaAPI
from .schemas import AnalyseData, PatientData
from .utils import process_patient_data


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "patient_diary.settings")
api = NinjaAPI()

DATA_STORAGE_FILE = Path("./data")


@api.post("/add-diary-record/{snils}")
def post_patient_snils(request, snils: str):
    file_path = DATA_STORAGE_FILE / f"{snils}.json"
    if file_path.exists():
        print("File exists")
        return file_path
    else:
        return {"error": "Patient not found"}, 404


@api.get("/get-patient-data/{snils}")
def get_patient_data(request, snils: str):
    file_path = DATA_STORAGE_FILE / f"{snils}.json"
    if not file_path.exists():
        return {"error": "Patient not found"}, 404

    patient_data = process_patient_data(file_path)

    return {
        "snils": patient_data.snils,
        "analyzes": [
            {
                "marker": analyze.marker,
                "value": analyze.value,
                "normal": analyze.normal,
                "unitOfMeasurement": analyze.unitOfMeasurement,
                "problem": analyze.problem,
            }
            for analyze in patient_data.analyzes
        ],
        "syndromes": [
            {
                "system": syndrome.system,
                "problems": syndrome.problems,
            }
            for syndrome in patient_data.syndromes
        ],
    }
