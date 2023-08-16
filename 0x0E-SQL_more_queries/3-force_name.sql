-- creates the table force_name on MYSQL Server
-- if table already exist, the script should not fail
CREATE TABLE IF NOT EXISTS `force_name` (`id` INT, `name` VARCHAR(256) NOT NULL);
