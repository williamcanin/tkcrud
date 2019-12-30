create table if not exists clients
(
    id             int auto_increment
        primary key,
    name           varchar(100) not null,
    address        varchar(100) not null,
    date_of_birth  date         not null,
    sex            varchar(19)  not null,
    marital_status varchar(19)  null,
    rg             varchar(19)  not null,
    cpf            varchar(19)  not null,
    cell_phone     varchar(19)  not null,
    email          varchar(100) null
);