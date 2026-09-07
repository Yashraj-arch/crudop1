from database import db_connection
from schema import Employee, Salary


def get_all_employees():
    conn = db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM employeetab")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows


def get_employee(emp_id: int):
    conn = db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM employeetab WHERE emp__id = %s",
        (emp_id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    return row


def add_employee(employee: Employee):
    conn = db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO employeetab (emp__id, name, dept, city)
        VALUES (%s, %s, %s, %s)
        """,
        (
            employee.emp_id,
            employee.name,
            employee.dept,
            employee.city,
        )
    )

    conn.commit()

    cur.close()
    conn.close()

    return {"employee added successfully"}


def update_employee(emp_id: int, employee: Employee):
    conn = db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE employeetab
        SET name = %s,
            dept = %s,
            city = %s
        WHERE emp__id = %s
        """,
        (
            employee.name,
            employee.dept,
            employee.city,
            emp_id
        )
    )

    conn.commit()

    cur.close()
    conn.close()

    return {"employee updated successfully"}


def delete_employee(emp_id: int):
    conn = db_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM employeetab WHERE emp__id = %s",
        (emp_id,)
    )

    conn.commit()

    cur.close()
    conn.close()

    return {"employee deleted successfully"}


def get_employee_with_salary(emp_id: int):
    conn = db_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute(
        """
        SELECT
            e.name,
            e.dept,
            e.city,
            s.basic_pay,
            s.hra,
            s.deductions,
            s.salary_date
        FROM employeetab e
        JOIN salarytab s ON e.emp__id = s.emp__id
        WHERE e.emp__id = %s
        """,
        (emp_id,)
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows


def get_all_employees_with_salary():
    conn = db_connection()
    cur = conn.cursor(dictionary=True)

    cur.execute(
        """
        SELECT
            e.emp__id,
            e.name,
            e.dept,
            e.city,
            s.basic_pay,
            s.hra,
            s.deductions,
            s.salary_date
        FROM employeetab e
        JOIN salarytab s ON e.emp__id = s.emp__id
        """
    )

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows


def get_all_salaries():
    conn = db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM salarytab")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows


def get_salary(salary_id: int):
    conn = db_connection()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM salarytab WHERE salary_id = %s",
        (salary_id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    return row


def add_salary(salary: Salary):
    conn = db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO salarytab (emp__id, basic_pay, hra, deductions, salary_date)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            salary.emp_id,
            salary.basic_pay,
            salary.hra,
            salary.deductions,
            salary.salary_date,
        )
    )

    conn.commit()

    cur.close()
    conn.close()

    return {"salary added successfully"}


def update_salary(salary_id: int, salary: Salary):
    conn = db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE salarytab
        SET emp__id = %s,
            basic_pay = %s,
            hra = %s,
            deductions = %s,
            salary_date = %s
        WHERE salary_id = %s
        """,
        (
            salary.emp_id,
            salary.basic_pay,
            salary.hra,
            salary.deductions,
            salary.salary_date,
            salary_id
        )
    )

    conn.commit()

    cur.close()
    conn.close()

    return {"salary updated successfully"}


def delete_salary(salary_id: int):
    conn = db_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM salarytab WHERE salary_id = %s",
        (salary_id,)
    )

    conn.commit()

    cur.close()
    conn.close()

    return {"salary deleted successfully"}