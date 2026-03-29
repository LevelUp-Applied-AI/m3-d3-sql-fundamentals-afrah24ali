import sqlite3


# Task 1
def top_departments(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT d.name, SUM(e.salary) AS total_salary
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
    GROUP BY d.name
    ORDER BY total_salary DESC
    LIMIT 3;
    """

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()
    return result


# Task 2
def employees_with_projects(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT e.name, p.name
    FROM employees e
    INNER JOIN project_assignments pa ON e.emp_id = pa.emp_id
    INNER JOIN projects p ON pa.project_id = p.project_id;
    """

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()
    return result


# Task 3
def salary_rank_by_department(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = """
    SELECT 
        e.name,
        d.name,
        e.salary,
        RANK() OVER (
            PARTITION BY e.dept_id
            ORDER BY e.salary DESC
        ) as rank
    FROM employees e
    JOIN departments d ON e.dept_id = d.dept_id
    ORDER BY d.name, e.salary DESC;
    """

    cursor.execute(query)
    result = cursor.fetchall()

    conn.close()
    return result


if __name__ == "__main__":
    db_path = "drill.db"

    print(top_departments(db_path))
    print(employees_with_projects(db_path))
    print(salary_rank_by_department(db_path))