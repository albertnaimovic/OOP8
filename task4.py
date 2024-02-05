from dataclasses import dataclass
from typing import List


@dataclass
class Employee:
    employee_id: int
    name: str
    age: int
    salary: float
    department: str


@dataclass
class Department:
    department_id: int
    name: str
    employee: List[Employee]

    def average_salary(self) -> float:
        avg_salary = sum([x.salary for x in self.employee]) / len(self.employee)
        return avg_salary


@dataclass
class EmployeeManagement:
    departments: List[Department]

    def total_salary(self) -> float:
        employees = [x.employee for x in self.departments]
        employees = [item for sublist in employees for item in sublist]
        return sum([x.salary for x in employees])

    def get_employees_in_age_range(self, min_age: int, max_age: int) -> List[Employee]:
        employees = [x.employee for x in self.departments]
        employees = [item for sublist in employees for item in sublist]
        return [x for x in employees if min_age <= x.age <= max_age]

    def sort_employees_by_salary(self) -> List[Employee]:
        employees = [x.employee for x in self.departments]
        employees = [item for sublist in employees for item in sublist]
        return sorted(employees, key=lambda x: x.salary, reverse=True)

    def filter_employees_by_department(self, department_name) -> List[Department]:
        for x in self.departments:
            if department_name == x.name:
                return x
            return


emp_1 = Employee(employee_id=1, name="Jonas", age=14, salary=5464.0, department="IT")
emp_2 = Employee(employee_id=2, name="Valdas", age=13, salary=5234.0, department="IT")
emp_3 = Employee(employee_id=3, name="Marius", age=35, salary=2464.0, department="IT")
emp_4 = Employee(
    employee_id=4, name="Giedrius", age=34, salary=464.0, department="Management"
)
emp_5 = Employee(
    employee_id=5, name="Arturas", age=66, salary=1464.0, department="Management"
)

it = Department(department_id=10, name="IT", employee=[emp_1, emp_2, emp_3])
management = Department(department_id=20, name="Management", employee=[emp_4, emp_5])

emp_management = EmployeeManagement(departments=[it, management])

print(emp_management.total_salary())
print(emp_management.get_employees_in_age_range(min_age=14, max_age=35))
print(emp_management.sort_employees_by_salary())
print(emp_management.filter_employees_by_department("IT"))
print(it.average_salary())
