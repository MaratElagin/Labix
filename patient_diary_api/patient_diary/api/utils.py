import json
import pandas as pd
from pathlib import Path
from .schemas import AnalyseData, PatientData
from .analyse import process_files, check


DATA_STORAGE_FILE = Path("./data")
FILTERED_DATA_PATH = Path("./data/filtered_data_with_sex.xlsx")
MARKER_RANGES_PATH = Path("./data/marker_ranges.json")


def get_patient_sindromes(file_path: str):
    output, _ = process_files(file_path, FILTERED_DATA_PATH, MARKER_RANGES_PATH)
    syndromes = []
    for system, problems in output.items():
        syndromes.append({"system": system, "problems": problems})
    return syndromes


def check_data_deviation(file_path: str):
    with open(file_path, "r") as f:
        data = json.load(f)

    with open(MARKER_RANGES_PATH, "r") as f:
        marker_ranges = json.load(f)

    parameter_deviation = check(data=data, marker_ranges=marker_ranges)
    return parameter_deviation


def process_patient_data(file_path: str) -> PatientData:
    # with open(file_path, "r") as f:
    #     patient = json.load(f)

    filtered_data_path = FILTERED_DATA_PATH
    marker_ranges_path = MARKER_RANGES_PATH

    output, merged_df = process_files(file_path, filtered_data_path, marker_ranges_path)

    parameter_deviation = check_data_deviation(file_path)

    analyzes = []
    for index, row in merged_df.iterrows():
        problem = None
        if row["Маркеры"] in output:
            system_name = list(output.keys())[0]
            problem = output[system_name]
        deviation_type = parameter_deviation.get(row["Маркеры"], (0, "="))
        if deviation_type[1] != "=":
            problem = (
                f"Повышенный уровень {row['Маркеры']}"
                if deviation_type[1] == "+"
                else f"Пониженный уровень {row['Маркеры']}"
            )
        analyze = AnalyseData(
            marker=row["Маркеры"],
            value=row["Значение"],
            normal=row["Норма"],
            unitOfMeasurement=row["Ед.изм."],
            problem=problem,
            syndromes=None,
        )
        analyzes.append(analyze)

    syndromes = get_patient_sindromes(file_path)
    patient_data = PatientData(
        snils=file_path.stem, analyzes=analyzes, syndromes=syndromes
    )

    return patient_data


# snils = "11142234"
# path = DATA_STORAGE_FILE / f"{snils}.json"

# print(get_patient_sindromes(path))
# print(process_patient_data(path))
# print(check_data_deviation(path))
