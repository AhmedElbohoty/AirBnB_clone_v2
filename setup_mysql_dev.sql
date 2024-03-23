-- Script that prepares a MySQL server for the project:

-- 1- A database hbnb_dev_db
-- 2- A new user hbnb_dev (in localhost)
-- 3- The password of hbnb_dev should be set to hbnb_dev_pwd
-- 4- hbnb_dev should have all privileges on the database hbnb_dev_db (and only this database)
-- 5- hbnb_dev should have SELECT privilege on the database performance_schema (and only this database)
-- 6- If the database hbnb_dev_db or the user hbnb_dev already exists, your script should not fail

-- 1
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- 2 and 3
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- 4
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- 5
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;