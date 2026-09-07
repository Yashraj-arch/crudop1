from fastapi import APIRouter, HTTPException
from schema import Employee, Salary
import repositories

employee_router = APIRouter(prefix="/employees", tags=["Employees"])
salary_router = APIRouter(prefix="/salaries", tags=["Salaries"])


# ---------- Employee CRUD ----------

@employee_router.get("/")
def get_all_employees():
    return repositories.get_all_employees()


@employee_router.get("/{emp_id}")
def get_employee(emp_id: int):
    employee = repositories.get_employee(emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@employee_router.post("/")
def add_employee(employee: Employee):
    existing = repositories.get_employee(employee.emp_id)
    if existing:
        raise HTTPException(status_code=400, detail="Employee with this emp_id already exists")
    return repositories.add_employee(employee)


@employee_router.put("/{emp_id}")
def update_employee(emp_id: int, employee: Employee):
    existing = repositories.get_employee(emp_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return repositories.update_employee(emp_id, employee)


@employee_router.delete("/{emp_id}")
def delete_employee(emp_id: int):
    existing = repositories.get_employee(emp_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return repositories.delete_employee(emp_id)


# ---------- Employee + Salary combined views ----------

@employee_router.get("/{emp_id}/salary")
def get_employee_with_salary(emp_id: int):
    existing = repositories.get_employee(emp_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    rows = repositories.get_employee_with_salary(emp_id)
    if not rows:
        raise HTTPException(status_code=404, detail="No salary records found for this employee")
    return rows


@employee_router.get("/with-salary/all")
def get_all_employees_with_salary():
    return repositories.get_all_employees_with_salary()


# ---------- Salary CRUD ----------

@salary_router.get("/")
def get_all_salaries():
    return repositories.get_all_salaries()


@salary_router.get("/{salary_id}")
def get_salary(salary_id: int):
    salary = repositories.get_salary(salary_id)
    if salary is None:
        raise HTTPException(status_code=404, detail="Salary record not found")
    return salary


@salary_router.post("/")
def add_salary(salary: Salary):
    employee = repositories.get_employee(salary.emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found, cannot add salary")
    return repositories.add_salary(salary)


@salary_router.put("/{salary_id}")
def update_salary(salary_id: int, salary: Salary):
    existing = repositories.get_salary(salary_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Salary record not found")
    return repositories.update_salary(salary_id, salary)


@salary_router.delete("/{salary_id}")
def delete_salary(salary_id: int):
    existing = repositories.get_salary(salary_id)
    if existing is None:
        raise HTTPException(status_code=404, detail="Salary record not found")
    return repositories.delete_salary(salary_id)