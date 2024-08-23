CREATE TABLE Electronic_Vehicle (
	vehicle_id	serial	NOT NULL,
	vehicle_name	VARCHAR(30)	NULL,
	brand_id	serial	NOT NULL,
	producer_id2	serial	NOT NULL,
	battery_id	serial	NOT NULL
);

CREATE TABLE Producer (
	producer_id	serial	NOT NULL,
	producer_name	VARCHAR(30)	NULL,
	country	VARCHAR(20)	NULL
);

CREATE TABLE Battery (
	battery_id	serial	NOT NULL
);

CREATE TABLE Vehicle_status (
	id	serial	NOT NULL,
	monthly	TIMESTAMP	NULL,
	region	VARCHAR(20)	NULL,
	registered_car	INT4	NULL,
	electr_car_rate	FLOAT	NULL
);

CREATE TABLE Battery_Producer (
	producer_id	serial	NOT NULL,
	battery_id	serial	NOT NULL
);

ALTER TABLE Electronic_Vehicle ADD CONSTRAINT PK_ELECTRONIC_VEHICLE PRIMARY KEY (
	vehicle_id
);

ALTER TABLE Producer ADD CONSTRAINT PK_PRODUCER PRIMARY KEY (
	producer_id
);

ALTER TABLE Battery ADD CONSTRAINT PK_BATTERY PRIMARY KEY (
	battery_id
);

ALTER TABLE Vehicle_status ADD CONSTRAINT PK_VEHICLE_STATUS PRIMARY KEY (
	id
);

ALTER TABLE Battery_Producer ADD CONSTRAINT PK_BATTERY_PRODUCER PRIMARY KEY (
	producer_id,
	battery_id
);

ALTER TABLE Electronic_Vehicle ADD CONSTRAINT FK_Producer_TO_Electronic_Vehicle_1 FOREIGN KEY (
	brand_id
)
REFERENCES Producer (
	producer_id
);

ALTER TABLE Electronic_Vehicle ADD CONSTRAINT FK_Battery_Producer_TO_Electronic_Vehicle_1 FOREIGN KEY (
	producer_id2
)
REFERENCES Battery_Producer (
	producer_id
);

ALTER TABLE Electronic_Vehicle ADD CONSTRAINT FK_Battery_Producer_TO_Electronic_Vehicle_2 FOREIGN KEY (
	battery_id
)
REFERENCES Battery_Producer (
	battery_id
);

ALTER TABLE Battery_Producer ADD CONSTRAINT FK_Producer_TO_Battery_Producer_1 FOREIGN KEY (
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

