-- Homework 4

--1. Создайте таблицу movies с полями movies_type, director, year_of_issue, length_in_minutes, rate.
DROP TABLE IF EXISTS 
    movies,
    movies_before_1990,
    movies_1990_2000,
    movies_2000_2010,
    movies_2010_2020,
    movies_after_2020,
    movies_length_less_40,
    movies_length_40_to_90,
    movies_length_90_to_130,
    movies_length_more_130,
    rating_less_5,
    rating_5_to_8,
    rating_8_to_10;

CREATE TABLE movies (
    id BIGINT NOT NULL,
    movies_type INT NOT NULL,
    director CHARACTER VARYING NOT NULL,
    year_of_issue DATE NOT NULL,
    length_in_minutes FLOAT NOT NULL,
    rate INT NOT NULL
);

--2. Сделайте таблицы для горизонтального партицирования по году выпуска (до 1990, 1990 -2000, 2000- 2010, 2010-2020, после 2020).
CREATE TABLE movies_before_1990 (CHECK (year_of_issue < '1990-01-01')) INHERITS (movies);
CREATE TABLE movies_1990_2000 (CHECK (year_of_issue >= '1990-01-01' AND year_of_issue < '2000-01-01')) INHERITS (movies);
CREATE TABLE movies_2000_2010 (CHECK (year_of_issue >= '2000-01-01' AND year_of_issue < '2010-01-01')) INHERITS (movies);
CREATE TABLE movies_2010_2020 (CHECK (year_of_issue >= '2010-01-01' AND year_of_issue < '2020-01-01')) INHERITS (movies);
CREATE TABLE movies_after_2020 (CHECK (year_of_issue >= '2020-01-01')) INHERITS (movies);

--3. Сделайте таблицы для горизонтального партицирования по длине фильма (до 40 минута, от 40 до 90 минут, от 90 до 130 минут, более 130 минут).
CREATE TABLE movies_length_less_40 (CHECK (length_in_minutes <= 40)) INHERITS (movies);
CREATE TABLE movies_length_40_to_90 (CHECK (length_in_minutes > 40 AND length_in_minutes <= 90)) INHERITS (movies);
CREATE TABLE movies_length_90_to_130 (CHECK (length_in_minutes > 90 AND length_in_minutes <= 130)) INHERITS (movies);
CREATE TABLE movies_length_more_130 (CHECK (length_in_minutes > 130)) INHERITS (movies);;

--4. Сделайте таблицы для горизонтального партицирования по рейтингу фильма (ниже 5, от 5 до 8, от 8до 10).
CREATE TABLE rating_less_5 (CHECK (rate < 5)) INHERITS (movies);
CREATE TABLE rating_5_to_8 (CHECK (rate >= 5 AND rate < 8)) INHERITS (movies);
CREATE TABLE rating_8_to_10 (CHECK (rate >= 8 AND rate <= 10)) INHERITS (movies);

--5. Создайте правила добавления данных для каждой таблицы.
CREATE RULE movies_insert_before_1990 AS
ON INSERT TO movies
WHERE (year_of_issue < '1990-01-01')
DO INSTEAD INSERT INTO movies_before_1990 VALUES (NEW.*);

CREATE RULE movies_insert_1990_2000 AS
ON INSERT TO movies
WHERE (year_of_issue >= '1990-01-01' AND year_of_issue < '2000-01-01')
DO INSTEAD INSERT INTO movies_1990_2000 VALUES (NEW.*);

CREATE RULE movies_insert_2000_2010 AS
ON INSERT TO movies
WHERE (year_of_issue >= '2000-01-01' AND year_of_issue < '2010-01-01')
DO INSTEAD INSERT INTO movies_2000_2010 VALUES (NEW.*);

CREATE RULE movies_insert_2010_2020 AS
ON INSERT TO movies
WHERE (year_of_issue >= '2010-01-01' AND year_of_issue < '2020-01-01')
DO INSTEAD INSERT INTO movies_2010_2020 VALUES (NEW.*);

CREATE RULE movies_insert_after_2020 AS
ON INSERT TO movies
WHERE (year_of_issue >= '2020-01-01')
DO INSTEAD INSERT INTO movies_after_2020 VALUES (NEW.*);


CREATE RULE movies_insert_length_less_40 AS
ON INSERT TO movies
WHERE (length_in_minutes <= 40)
DO INSTEAD INSERT INTO movies_length_less_40 VALUES (NEW.*);

CREATE RULE movies_insert_length_40_to_90 AS
ON INSERT TO movies
WHERE (length_in_minutes > 40 AND length_in_minutes <= 90)
DO INSTEAD INSERT INTO movies_length_40_to_90 VALUES (NEW.*);

CREATE RULE movies_insert_length_90_to_130 AS
ON INSERT TO movies
WHERE (length_in_minutes > 90 AND length_in_minutes <= 130)
DO INSTEAD INSERT INTO movies_length_90_to_130 VALUES (NEW.*);

CREATE RULE movies_insert_length_more_130 AS
ON INSERT TO movies
WHERE (length_in_minutes > 130)
DO INSTEAD INSERT INTO movies_length_more_130 VALUES (NEW.*);

CREATE RULE movies_insert_rating_less_5 AS
ON INSERT TO movies
WHERE (rate < 5)
DO INSTEAD INSERT INTO rating_less_5 VALUES (NEW.*);

CREATE RULE movies_insert_rating_5_to_8 AS
ON INSERT TO movies
WHERE (rate >= 5 AND rate < 8)
DO INSTEAD INSERT INTO rating_5_to_8 VALUES (NEW.*);

CREATE RULE movies_insert_rating_8_to_10 AS
ON INSERT TO movies
WHERE (rate >= 8 AND rate <= 10)
DO INSTEAD INSERT INTO rating_8_to_10 VALUES (NEW.*);

--6. Добавьте фильмы так, чтобы в каждой таблице было не менее 3 фильмов.
INSERT INTO movies (id, movies_type, director, year_of_issue, length_in_minutes, rate) VALUES
(1, 1, 'Director A', '1985-05-10', 100, 6),
(2, 1, 'Director B', '1980-07-15', 90, 7),
(3, 1, 'Director C', '1975-03-20', 120, 8),
(4, 2, 'Director D', '1991-05-10', 110, 5),
(5, 2, 'Director E', '1995-07-15', 95, 6),
(6, 2, 'Director F', '1999-03-20', 130, 9),
(7, 3, 'Director G', '2001-05-10', 115, 7),
(8, 3, 'Director H', '2005-07-15', 85, 8),
(9, 3, 'Director I', '2009-03-20', 140, 6),
(10, 4, 'Director J', '2011-05-10', 105, 7),
(11, 4, 'Director K', '2015-07-15', 95, 6),
(12, 4, 'Director L', '2019-03-20', 130, 8),
(13, 5, 'Director M', '2021-05-10', 120, 9),
(14, 5, 'Director N', '2022-07-15', 90, 5),
(15, 5, 'Director O', '2023-03-20', 110, 7),
(16, 6, 'Director P', '1992-01-01', 40, 6),
(17, 6, 'Director Q', '2003-06-12', 30, 7),
(18, 6, 'Director R', '2015-11-22', 35, 5),
(19, 7, 'Director S', '1988-08-08', 85, 7),
(20, 7, 'Director T', '1998-09-09', 70, 6),
(21, 7, 'Director U', '2008-10-10', 60, 8),
(22, 8, 'Director V', '1995-05-05', 100, 7),
(23, 8, 'Director W', '2005-06-06', 120, 8),
(24, 8, 'Director X', '2015-07-07', 110, 9),
(25, 9, 'Director Y', '2000-03-03', 140, 6),
(26, 9, 'Director Z', '2010-04-04', 150, 7),
(27, 9, 'Director AA', '2020-05-05', 160, 8),
(28, 10, 'Director AB', '1993-03-03', 100, 4),
(29, 10, 'Director AC', '2003-04-04', 120, 3),
(30, 10, 'Director AD', '2013-05-05', 110, 2),
(31, 11, 'Director AE', '1997-06-06', 100, 6),
(32, 11, 'Director AF', '2007-07-07', 120, 7),
(33, 11, 'Director AG', '2017-08-08', 110, 5),
(34, 12, 'Director AH', '1996-09-09', 100, 9),
(35, 12, 'Director AI', '2006-10-10', 120, 8),
(36, 12, 'Director AJ', '2016-11-11', 110, 10);

--7. Добавьте пару фильмов с рейтингом выше 10.
INSERT INTO movies (id, movies_type, director, year_of_issue, length_in_minutes, rate) VALUES
(37, 13, 'Christopher Nolan', '2014-11-07', 169, 11),
(38, 14, 'Ridley Scott', '2015-10-02', 144, 11);

--8. Сделайте выбор из всех таблиц, в том числе из основной.
SELECT *
FROM movies;

SELECT *
FROM movies
WHERE movies.length_in_minutes = 160;

SELECT *
FROM movies
WHERE movies.rate = 11;

SELECT *
FROM ONLY movies;

	

