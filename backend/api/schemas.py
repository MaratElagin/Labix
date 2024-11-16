from pydantic import BaseModel, Field

from datetime import date, datetime
from typing import List, Optional
from enum import Enum
from uuid import UUID



class PatientBase(BaseModel):
    id: str | None = None
    snils: str
    fio: str
    birthday: date
    is_man: bool


class PatientsListBase(BaseModel):
    patients: list[PatientBase] | None


class BodySystemBase(BaseModel):
    class Config:
        populate_by_name = True

    id: str | None = None
    name: str
    created_at: datetime = None
    updated_at: datetime = None


class BodySystemListBase(BaseModel):
    body_system_list: list[BodySystemBase] | None


class SystemStateBase(BaseModel):
    id: str | None = None
    name: str
    system_id: UUID | None = None
    created_at: datetime = None
    updated_at: datetime = None


class SystemStateListBase(BaseModel):
    system_state_list: list[SystemStateBase] | None


class MeasurementBase(BaseModel):
    id: str | None = None
    name: str
    created_at: datetime = None
    updated_at: datetime = None


class MeasurementListBase(BaseModel):
    measurement_list: list[MeasurementBase] | None


class ConditionTypeBase(str, Enum):
    gt = ">"
    lt = "<"
    gte = ">="
    lte = "<="
    eq = "="


class SexBase(str, Enum):
    Male = "male"
    Female = "female"
    Both = "both"


class DeviationTypeBase(str, Enum):
    Normal = "Норма"
    Moderate = "Умеренные отклонения"
    Marked = "Выраженные отклонения"
    Critical = "Критические отклонения"


class ParameterConditionBase(BaseModel):
    parameter_id: str | None = None
    condition_type: ConditionTypeBase | None = None
    deviation_type: DeviationTypeBase | None = None
    sex: SexBase | None = None
    is_age: bool = False
    value: float | None = None
    created_at: datetime = None
    updated_at: datetime = None


class ParameterConditionListBase(BaseModel):
    parameter_list: list[ParameterConditionBase] | None


class ParameterBase(BaseModel):
    id: str | None = None
    name: str
    measurement_id: UUID | None = None
    created_at: datetime = None
    updated_at: datetime = None


class ParameterListBase(BaseModel):
    parameter_list: list[ParameterBase] | None


class PatientParameterBase(BaseModel):
    class Config:
        populate_by_name = True

    # mh_id: str | None = None
    parameter_id: UUID | None = None
    name: str | None = None
    value: float | None = None
    check_datetime: datetime = None
    created_at: datetime = None
    updated_at: datetime = None


class PatientParameterBaseList(BaseModel):
    patient_parameter_list: list[PatientParameterBase] | None


