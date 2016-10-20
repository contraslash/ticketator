create user ticket_user_db with password 'ticket4everyone';
create database tickets_db;
grant all privileges on database tickets_db to ticket_user_db;