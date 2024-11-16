from uuid import UUID, uuid4
import enum
import sqlalchemy as sa

from sqlalchemy import Column, ForeignKey, Table, Relationship, Field
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime, date
from typing import Optional, List


class BaseModel(DeclarativeBase):
    
    __abstract__ = True
    
    id: UUID = Field(
        default=None,
        sa_column=sa.Column(
            "id",
            sa.UUID(as_uuid=True),
            primary_key=True,
            default=uuid4,
        ),
    )
    created_at: datetime = Field(
        default=None,
        sa_column=sa.Column(
            "created_at",
            sa.DateTime(),
            server_default=sa.func.now(),
        ),
    )
    updated_at: datetime = Field(
        default=None,
        sa_column=sa.Column(
            "updated_at",
            sa.DateTime(),
            server_default=sa.func.now(),
            onupdate=sa.func.now(),
        ),
    )
    

class Patient(BaseModel, table=True):
    
    __tablename__ = "patient"

    snils: str = Field(
        default=None,
        sa_column=sa.Column(
            "snils",
            primary_key=True,
        ),
    )
    fio: str
    birthday: date = Field(
        default=None,
        sa_column=sa.Column(
            "birthday",
            sa.Date(),
        ),
    )
    is_man: bool = Field(default=True)
    patient_parameter: List["PatientParameter"] = Relationship(
        back_populates="patient"
    )

    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d["id"] = str(self.id)
        d["birthday"] = self.birthday.isoformat()
        d["created_at"] = self.created_at.replace(microsecond=0).isoformat()
        d["updated_at"] = self.updated_at.replace(microsecond=0).isoformat()
        return d
    

class BodySystem(BaseModel, table=True):
    
    __tablename__ = "body_system"

    name: str

    states: List["SystemState"] = Relationship(back_populates="body_system")

    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d["id"] = str(self.id)
        d["created_at"] = self.created_at.replace(microsecond=0).isoformat()
        d["updated_at"] = self.updated_at.replace(microsecond=0).isoformat()
        return d


class SystemStateParameterLink(BaseModel, table=True):
    """ Промежуточная таблица для связи many-to-many"""
    system_state: UUID | None = Field(
        default=None, foreign_key="system_state.id", primary_key=True
    )
    parameter: UUID | None = Field(
        default=None, foreign_key="parameter.id", primary_key=True
    )


class SystemState(BaseModel, table=True):
    
    __tablename__ = "system_state"

    name: str

    system_id: UUID = Field(foreign_key="body_system.id")
    body_system: Optional[BodySystem] = Relationship(back_populates="states")

    parameters: list["Parameter"] = Relationship(
        back_populates="states", link_model=SystemStateParameterLink
    )

    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d["id"] = str(self.id)
        d["created_at"] = self.created_at.replace(microsecond=0).isoformat()
        d["updated_at"] = self.updated_at.replace(microsecond=0).isoformat()
        return d


class Measurement(BaseModel, table=True):
    
    __tablename__ = "measurement"
    
    name: str
    parameters: List["Parameter"] = Relationship(back_populates="measurement")

    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d["id"] = str(self.id)
        d["created_at"] = self.created_at.replace(microsecond=0).isoformat()
        d["updated_at"] = self.updated_at.replace(microsecond=0).isoformat()
        return d


class Parameter(BaseModel, table=True):
    
    __tablename__ = "parameter"

    name: str
    states: list[SystemState] = Relationship(
        back_populates="parameters", link_model=SystemStateParameterLink
    )

    measurement_id: UUID = Field(foreign_key="measurement.id", nullable=True)
    measurement: Optional[Measurement] = Relationship(back_populates="parameters")
    parameter_condition: List["ParameterCondition"] = Relationship(
        back_populates="parameter"
    )
    patient_parameter: Optional["PatientParameter"] = Relationship(
        back_populates="patient_parameter"
    )

    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d["id"] = str(self.id)
        d["created_at"] = self.created_at.replace(microsecond=0).isoformat()
        d["updated_at"] = self.updated_at.replace(microsecond=0).isoformat()
        return d


class ConditionType(enum.Enum):
    gt = ">"
    lt = "<"
    gte = ">="
    lte = "<="
    eq = "="
    
class Sex(enum.Enum):
    both = "both"
    male = "male"
    female = "female"

class DeviationType(enum.Enum):
    NORMAL = "Норма"
    MODERATE = "Умеренные отклонения"
    MARKED = "Выраженные отклонения"
    CRITICAL = "Критические отклонения"


class ParameterCondition(BaseModel, table=True):
    
    __tablename__ = "parameter_condition"

    parameter_id: UUID = Field(foreign_key="parameter.id")
    parameter: Optional[Parameter] = Relationship(back_populates="parameter_condition")

    condition_type: str = Field(sa.Column(sa.Enum(ConditionType)), nullable=True)
    deviation_type: str = Field(sa.Column(sa.Enum(DeviationType)), nullable=True)
    sex: str = Field(sa.Column(sa.Enum(Sex)), nullable=True)

    is_age: bool = Field(default=False)
    value: float | None
    
    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d["id"] = str(self.id)
        d["parameter_id"] = str(self.parameter_id)
        d["created_at"] = self.created_at.replace(microsecond=0).isoformat()
        d["updated_at"] = self.updated_at.replace(microsecond=0).isoformat()
        return d


class PatientParameter(BaseModel, table=True):
    
    __tablename__ = "patient_parameter"
    
    parameter_id: UUID = Field(foreign_key="parameter.id")
    patient_parameter: Optional["Parameter"] = Relationship(
        back_populates="patient_parameter"
    )
    name: str = Field(nullable=True)

    patient_id: UUID = Field(foreign_key="patient.id")
    patient: Optional["Patient"] = Relationship(
        back_populates="patient_parameter"
    )

    value: float | None
    check_datetime: datetime = Field(
        default=None,
        sa_column=sa.Column(
            "check_date",
            sa.DateTime(),
        ),
    )

    def __init__(self, *args, **kwargs):
        """Инициализация названия параметра"""
        super().__init__(**kwargs)
        if self.patient_parameter:
            self.name = self.patient_parameter.name

    def dict(self, *args, **kwargs) -> dict:
        d = super().dict(*args, **kwargs)
        d["id"] = str(self.id)
        d["check_datetime"] = self.created_at.replace(microsecond=0).isoformat()
        # d["check_datetime"] = self.check_datetime.strftime("%d.%m.%Y %H:%M")
        d["created_at"] = self.created_at.replace(microsecond=0).isoformat()
        d["updated_at"] = self.updated_at.replace(microsecond=0).isoformat()
        return d

    def formated_dict(self, *args, **kwargs) -> dict:
        """Метод нужен для формирование словоря значений и даты проверки"""
        d = self.dict(*args, **kwargs)
        d["check_datetime"] = self.check_datetime.strftime("%d.%m.%Y %H:%M")
        d.pop("id")
        d.pop("name")
        d.pop("patient_id")
        d.pop("parameter_id")
        d.pop("created_at")
        d.pop("updated_at")
        return d
