-- Create the table users if this doesn't exists
create table if not exists users (
    id int not null auto_increment,
    email varchar(255) not null unique,
    name varchar(255),
    primary key(id)
);