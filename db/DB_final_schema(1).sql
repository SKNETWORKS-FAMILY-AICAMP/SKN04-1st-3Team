CREATE TABLE Electronic_Vehicle (
	vehicle_id	INT4	NOT NULL,
	vehicle_name	VARCHAR(30)	NULL,
	brand_id	INT4	NOT NULL,
	producer_id	serial	NOT NULL
);

CREATE TABLE Producer (
	producer_id	INT4	NOT NULL,
	producer_name	VARCHAR(30)	NULL,
	country	VARCHAR(20)	NULL
);

CREATE TABLE Vehicle_status (
	register_id	INT4	NOT NULL,
	year	TIMESTAMP	NULL,
	region	VARCHAR(20)	NULL,
	registered_car	INT4	NULL,
	registered_electr_car	FLOAT	NULL
);

CREATE TABLE Brand (
	brand_id	INT4	NOT NULL,
	brand_name	VARCHAR(30)	NULL
);

CREATE TABLE back (
	url	text	NULL,
	API	text	NULL
);

CREATE TABLE FAQ (
	faq_id	INT4	NOT NULL,
	Question	text	NULL,
	Answer	text	NULL
);

ALTER TABLE Electronic_Vehicle ADD CONSTRAINT PK_ELECTRONIC_VEHICLE PRIMARY KEY (
	vehicle_id
);

ALTER TABLE Producer ADD CONSTRAINT PK_PRODUCER PRIMARY KEY (
	producer_id
);

ALTER TABLE Vehicle_status ADD CONSTRAINT PK_VEHICLE_STATUS PRIMARY KEY (
	register_id
);

ALTER TABLE Brand ADD CONSTRAINT PK_BRAND PRIMARY KEY (
	brand_id
);

ALTER TABLE FAQ ADD CONSTRAINT PK_FAQ PRIMARY KEY (
	faq_id
);

ALTER TABLE Electronic_Vehicle ADD CONSTRAINT FK_Brand_TO_Electronic_Vehicle_1 FOREIGN KEY (
	brand_id
)
REFERENCES Brand (
	brand_id
);

ALTER TABLE Electronic_Vehicle ADD CONSTRAINT FK_Producer_TO_Electronic_Vehicle_1 FOREIGN KEY (
	producer_id
)
REFERENCES Producer (
	producer_id
);

