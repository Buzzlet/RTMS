CREATE DATABASE rtms CHARACTER SET utf8;

USE rtms;

CREATE TABLE user (
	user_id     VARCHAR(20),
	user_name   VARCHAR(40),
	user_lvl    INTEGER,
	user_status VARCHAR(10),
	last_login  DATETIME,
	bad_logins  INTEGER
);

CREATE TABLE tkt (
	tkt_num       VARCHAR(10),
	title         VARCHAR(50),
	description   VARCHAR(255),
	status        VARCHAR(10),
	priority      INTEGER,
	precedence    INTEGER,
	requestor     VARCHAR(50),
	plant         VARCHAR(10),
	assigned_to   VARCHAR(20),
	create_date   DATE,
	goal_date     DATE,
	complete_date DATE,
	branch        VARCHAR(40)
);	

CREATE TABLE task (
	tkt_num       VARCHAR(10),
	task_num      INTEGER,
	title         VARCHAR(50),
	description   VARCHAR(255),
	status        VARCHAR(10),
	priority      INTEGER,
	precedence    INTEGER,
	requestor     VARCHAR(50),
	plant         VARCHAR(10),
	assigned_to   VARCHAR(20),
	create_date   DATE,
	goal_date     DATE,
	complete_date DATE,
	branch        VARCHAR(40)
);
	
CREATE TABLE note (
	ref_table VARCHAR(20),
	id        INTEGER,
	note      VARCHAR(255)
);