--- New database

CREATE DATABASE testdb;
CREATE USER test_user WITH PASSWORD '!Edu1234';
GRANT ALL PRIVILEGES ON DATABASE testdb TO test_user;

-- Create table and insert test data
\c testdb
CREATE TABLE test_table (id SERIAL PRIMARY KEY, content TEXT);
INSERT INTO test_table (content) VALUES ('Hello from PostgreSQL!');

GRANT CONNECT ON DATABASE testdb TO test_user;
GRANT USAGE ON SCHEMA public TO test_user;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO test_user;

-- also make sure future tables can be read:
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO test_user;

