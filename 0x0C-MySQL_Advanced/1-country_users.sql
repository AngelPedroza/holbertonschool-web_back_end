-- Create the table users if this doesn't exists
-- with a new country parameter
create table if not exists users (
    id int not null auto_increment,
    email varchar(255) not null unique,
    name varchar(255),
    country enum('US', 'CO', 'TN') not null,
    primary key(id)
);