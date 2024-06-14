-- Create the database if it does not exist
DO $$ 
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_database WHERE datname = 'srecord_db') THEN
      PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE srecord_db');
   END IF;
END
$$;

-- Create the user if it does not exist
DO $$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'srecord_user') THEN
      CREATE ROLE srecord_user LOGIN PASSWORD 'your_password';
   END IF;
END
$$;

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON DATABASE srecord_db TO srecord_user;

