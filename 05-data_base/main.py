from models import Department, Employee
from conexion import engine, BaseModel, session

def save_data():
    department1 = Department(name='IT') 
    department2 = Department(name='HR') 
    session.add(department1) 
    session.add(department2) 
    session.commit() 
    employee1 = Employee(name='John', surname='Doe', document='12345678', department_id=department1.id)
    employee2 = Employee(name='Jane', surname='Smith', document='87654321', department_id=department2.id) 
    session.add(employee1) 
    session.add(employee2) 
    session.commit()
    
    print(department1.id, department1.name)
    print(department2.id, department2.name)
    
def getAll(): 
    departments = session.query(Department).all() 
    for department in departments:
        print(department)
        
def getById(id:int):
    department = session.query(Department).filter_by(id=id).first() 
    if department: 
        print(f'getById - ',department) 
    else: 
        print(f'Department with id {id} not found.')
        
def getAmountDepartments(): 
    amount = session.query(Department).count() 
    print(f'Amount of departments: {amount}')
    
def getEmployeesByDepartment(department_id:int):
    employees = session.query(Employee).filter_by(department_id=department_id).all() 
    print(f'Employees in department {department_id}:') 
    for employee in employees: 
        print(employee)


if __name__ == '__main__':
    BaseModel.metadata.create_all(engine)
    # save_data()
    getAll()
    getById(1) 
    getById(3)
    getAmountDepartments()
    getEmployeesByDepartment(2)  