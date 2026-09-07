from pydantic import BaseModel
from datetime import date


class Employee(BaseModel):
    emp_id: int
    name: str
    dept: str
    city: str


class Salary(BaseModel):
    emp_id: int
    basic_pay: float
    hra: float
    deductions: float
    salary_date: date