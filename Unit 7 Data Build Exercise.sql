-- Definition of the underlying schema:
CREATE SCHEMA IF NOT EXISTS school_database DEFAULT CHARACTER SET utf8;
USE school_database;

-- Create students table:
CREATE TABLE IF NOT EXISTS school_database.students(
    student_number INT NOT NULL,
    first_name VARCHAR (100) NOT NULL,
    last_name VARCHAR (100) NOT NULL,
    birth_date DATE NOT NULL,
    PRIMARY KEY (student_number));

-- Create courses table:
CREATE TABLE IF NOT EXISTS school_database.courses(
    course_name VARCHAR(100) NOT NULL,
    teacher_name VARCHAR (100) NOT NULL,
    PRIMARY KEY (course_name));

-- Create teacher table:
CREATE TABLE IF NOT EXISTS school_database.teacher(
    teacher_name VARCHAR (100) NOT NULL,
    teacher_title VARCHAR (100) NOT NULL,
    PRIMARY KEY (teacher_name));

# Create exams table:
CREATE TABLE IF NOT EXISTS school_database.exams(
    course_name VARCHAR (100) NOT NULL,
    student_number INT NOT NULL,
    exam_score INT NOT NULL,
    support_needed VARCHAR(100) NOT NULL,
    PRIMARY KEY(course_name, student_number));

-- Create exam boards table:
CREATE TABLE IF NOT EXISTS school_database.exam_boards(
    course_name VARCHAR(100) NOT NULL,
    exam_board VARCHAR(100) NOT NULL,
    PRIMARY KEY(course_name));

-- Insert data into students table:
INSERT INTO students(student_number, first_name, last_name, birth_date) VALUES
(1001, 'Bob', 'Baker', '2001-08-25'),
(1002, 'Sally', 'Davies', '1999-10-02'),
(1003, 'Mark', 'Hanmill', '1995-06-05'),
(1004, 'Anas', 'Ali', '1980-08-03'),
(1005, 'Cheuk', 'Yin', '2002-05-01');

-- Insert data into courses table:
INSERT INTO courses(course_name, teacher_name) VALUES
('Computer Science', 'Jones'),
('Maths', 'Parker'),
('Physics', 'Peters'),
('Biology', 'Patel'),
('Music', 'Daniels');

-- Insert data into teacher table:
INSERT INTO teacher(teacher_name, teacher_title) VALUES
('Jones', 'Mr'),
('Parker', 'Ms'),
('Peters', 'Mr'),
('Patel', 'Mrs'),
('Daniels', 'Ms');

-- Insert data into exams table:
INSERT INTO exams(course_name, student_number, exam_score, support_needed) VALUES
('Computer Science', 1001, 78, 'No'),
('Maths', 1001, 78, 'No'),
('Physics', 1001, 78, 'No'),
('Maths', 1002, 55, 'Yes'),
('Biology', 1002, 55, 'Yes'),
('Music', 1002, 55, 'Yes'),
('Computer Science', 1003, 90, 'No'),
('Maths', 1003, 90, 'No'),
('Physics', 1003, 90, 'No'),
('Maths', 1004, 70, 'No'),
('Physics', 1004, 70, 'No'),
('Biology', 1004, 70, 'No'),
('Computer Science', 1005, 45, 'Yes'),
('Maths', 1005, 45, 'Yes'),
('Music', 1005, 45, 'Yes');

-- Insert data into exam_boards table:
INSERT INTO exam_boards(course_name, exam_board) VALUES
('Computer Science', 'BCS'),
('Maths', 'EdExcel'),
('Physics', 'OCR'),
('Maths', 'AQA'),
('Biology', 'WJEC'),
('Music', 'AQA'),
('Computer Science', 'BCS'),
('Maths', 'EdExcel'),
('Physics', 'OCR'),
('Maths', 'AQA'),
('Physics', 'OCR'),
('Biology', 'WJEC'),
('Computer Science', 'BCS'),
('Maths', 'EdExcel'),
('Music', 'AQA');

-- Test for referential integrity:

-- To check this I run queries on the database and review whether I produce errors when joining the tables by their primary and foreign keys:
SELECT *
FROM students
INNER JOIN exams ON students.student_number = exams.student_number;

SELECT *
FROM exams
INNER JOIN exam_boards ON exams.course_name = exam_boards.course_name;

SELECT *
FROM courses
INNER JOIN teacher ON courses.teacher_name = teacher.teacher_name;