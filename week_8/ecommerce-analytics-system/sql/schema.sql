create table customers(
    customer_id int primary key,
    customer_name varchar(50) not null,
    email varchar(50) not null unique,
    registration_date date not null, 
    customer_type check (customer_type in ("REGULAr","premium","vip"))
)

