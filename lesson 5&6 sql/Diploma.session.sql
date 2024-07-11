--@block
CREATE DATABASE IF NOT EXISTS Diploma;

--@block
USE Diploma;

--@block
CREATE TABLE IF NOT EXISTS Students
(
  id          INT PRIMARY KEY AUTO_INCREMENT,
  name        VARCHAR(255) NOT NULL,
  surname     VARCHAR(255) NOT NULL,
  patronymic  VARCHAR(255) NOT NULL,
  groupNumber VARCHAR(255) NOT NULL
)

--@block
CREATE TABLE IF NOT EXISTS Subjects
(
  id   INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL
)

--@block
CREATE TABLE IF NOT EXISTS Marks
(
  id         INT PRIMARY KEY AUTO_INCREMENT,
  student_id INT NOT NULL,
  subject_id INT NOT NULL,
  mark       INT NOT NULL
)

--@block
ALTER TABLE Marks
  ADD FOREIGN KEY (student_id) REFERENCES Students(id),
  ADD FOREIGN KEY (subject_id) REFERENCES Subjects(id)

--@block
INSERT INTO Students (name, surname, groupNumber)
VALUES ('ahmed', 'moussa', 'AB-11'),
       ('khalid', 'amr', 'NE-22'),
       ('saif', 'elsady', 'HP-33')

--@block
INSERT INTO Subjects (name)
VALUES ('Математика'),
       ('English'),
       ('History')

--@block
INSERT INTO Marks (student_id, subject_id, mark)
VALUES (1, 1, 5),
       (1, 2, 4),
       (1, 3, 3),
       (2, 1, 4),
       (2, 2, 5),
       (2, 3, 4),
       (3, 1, 3),
       (3, 2, 4),
       (3, 3, 5)

--@block
SELECT * FROM Students

--@block
SELECT * FROM Subjects

--@block
SELECT * FROM Marks, Students, Subjects