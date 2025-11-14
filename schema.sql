-- Create the users table
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    role TEXT NOT NULL
);

-- Insert some sample users
INSERT INTO users (name, email, role) VALUES
('Rajat', 'rajat@example.com', 'Admin'),
('Neha', 'neha@example.com', 'Editor'),
('Amit', 'amit@example.com', 'Viewer');
