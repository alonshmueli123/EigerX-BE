create table departments (
  id integer,
  name text,
  location text,
  primary key(id)
);

create table employee (
  id integer,
  name text,
  salary integer,
  dept_id integer,
  primary key(id),
  constraint fk_dept_id
  	FOREIGN KEY(dept_id)
	  REFERENCES departments(id)
);

insert into departments (id, name, location) values
(1, 'Executive', 'Sydney'),
(2, 'Production', 'Sydney'),
(3, 'Resources', 'Cape Town'),
(4, 'Technical', 'Texas'),
(5, 'Management', 'Paris')
;

insert into employee (id, name, salary, dept_id) values
(1, 'Candice', 4685, 1),
(2, 'Julia', 2559, 2),
(3, 'Bob', 4405, 4),
(4, 'Scarlet', 2350, 1),
(5, 'Ileana', 1151, 4)
;

select departments.name as department_name,
       count(employee.id) as employee_count
  from departments
  left join employee on departments.id = employee.dept_id
 group by departments.name
 order by employee_count desc, department_name asc
;