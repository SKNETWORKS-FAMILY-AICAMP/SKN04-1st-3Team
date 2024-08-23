CREATE TABLE Region (
	region_id	serial	NOT NULL,
	region_name	VARCHAR(30)	NULL
);

CREATE TABLE Vehicle (
	vehicle_id	serial	NOT NULL,
	vehicle_name	VARCHAR(30)	NULL,
	electr_engine	BOOLEAN	NULL,
	battery_id	serial	NOT NULL,
	producer_id	serial	NOT NULL
);

CREATE TABLE Producer (
	producer_id	serial	NOT NULL,
	producer_name	VARCHAR(30)	NULL,
	country	VARCHAR(20)	NULL
);

CREATE TABLE Battery (
	battery_id	serial	NOT NULL
);

CREATE TABLE Battery_Producer (
	battery_id	serial	NOT NULL,
	producer_id	serial	NOT NULL
);

CREATE TABLE Date (
	date_id	serial	NOT NULL,
	date_	TIMESTAMP	NULL
	-- COMMENT "%Y-%m-%d %H:%M:%S" 
);

CREATE TABLE Monthly (
	id	serial	NOT NULL,
	registered_car	INT4	NULL,
	electr_car_rate	FLOAT	NULL,
	region_id	serial	NOT NULL,
	date_id	serial	NOT NULL
);

ALTER TABLE Region ADD CONSTRAINT PK_REGION PRIMARY KEY (
	region_id
);

ALTER TABLE Vehicle ADD CONSTRAINT PK_VEHICLE PRIMARY KEY (
	vehicle_id
);

ALTER TABLE Producer ADD CONSTRAINT PK_PRODUCER PRIMARY KEY (
	producer_id
);

ALTER TABLE Battery ADD CONSTRAINT PK_BATTERY PRIMARY KEY (
	battery_id
);

ALTER TABLE Battery_Producer ADD CONSTRAINT PK_BATTERY_PRODUCER PRIMARY KEY (
	battery_id,
	producer_id
);

ALTER TABLE Date ADD CONSTRAINT PK_DATE PRIMARY KEY (
	date_id
);

ALTER TABLE Monthly ADD CONSTRAINT PK_MONTHLY PRIMARY KEY (
	id
);

ALTER TABLE Vehicle ADD CONSTRAINT FK_Battery_TO_Vehicle_1 FOREIGN KEY (
	battery_id
)
REFERENCES Battery (
	battery_id
);

ALTER TABLE Vehicle ADD CONSTRAINT FK_Producer_TO_Vehicle_1 FOREIGN KEY (
	producer_id
)
REFERENCES Producer (
	producer_id
);

ALTER TABLE Battery_Producer ADD CONSTRAINT FK_Battery_TO_Battery_Producer_1 FOREIGN KEY (
	battery_id
)
REFERENCES Battery (
	battery_id
);

ALTER TABLE Battery_Producer ADD CONSTRAINT FK_Producer_TO_Battery_Producer_1 FOREIGN KEY (
	producer_id
)
REFERENCES Producer (
	producer_id
);

ALTER TABLE Monthly ADD CONSTRAINT FK_Region_TO_Monthly_1 FOREIGN KEY (
	region_id
)
REFERENCES Region (
	region_id
);

ALTER TABLE Monthly ADD CONSTRAINT FK_Date_TO_Monthly_1 FOREIGN KEY (
	date_id
)
REFERENCES Date (
	date_id
);

