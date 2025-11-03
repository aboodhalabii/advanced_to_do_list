CREATE TYPE status_type AS ENUM (
    'PENDING',
    'IN_PROGRESS',
    'COMPLETED',
    'DELETED'
);



CREATE TABLE user (
  id SERIAL PRIMARY KEY,
  username Text UNIQUE NOT NULL,
  password Text NOT NULL,
  email Text UNIQUE NOT NULL,
   created_at DATETIME NOT NULL DEFAULT (),
   updated_at DATETIME NOT NULL DEFAULT (),
);

CREATE TABLE todo (
  id SERIAL PRIMARY KEY,
  title Text UNIQUE NOT NULL,
  email Text UNIQUE NOT NULL,
  description Text UNIQUE,
 status status_type DEFAULT 'PENDING',
  user_id int,
  duedate TIMESTAMP,
   created_at DATETIME NOT NULL DEFAULT NOW(),
   updated_at DATETIME NOT NULL DEFAULT NOW(),
    CONSTRAINT fk_useer
        FOREIGN KEY (user_id) 
        REFERENCES user (id)
        ON DELETE CASCADE 
);

CREATE TABLE subtodo (
  id SERIAL PRIMARY KEY,
  title Text UNIQUE NOT NULL,
  email Text UNIQUE NOT NULL,
  description Text UNIQUE,
  status status_type DEFAULT 'PENDING',
  tudo_id int,
  duedate TIMESTAMP,
   created_at DATETIME NOT NULL DEFAULT NOW(),
   updated_at DATETIME NOT NULL DEFAULT NOW(),
   CONSTRAINT fk_todo
        FOREIGN KEY (todo_id) 
        REFERENCES todo (id)
        ON DELETE CASCADE 
);