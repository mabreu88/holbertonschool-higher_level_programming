-- a script that creates a table second_table in the database hbtn_0c_0 in your MySQL server and add multiples rows.
create table if not exists second_table (id INT, name VARCHAR(256), score INT);
insert into second_table values ('1', 'John', '10');
insert into second_table values ('2', 'Alex', '3');
insert into second_table values ('3', 'Bob', '14');
insert into second_table values ('4', 'George', '8');