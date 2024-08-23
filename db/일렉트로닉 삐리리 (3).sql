CREATE TABLE `Region_DB` (
	`region_id`	serial	NOT NULL,
	`region_name`	VARCHAR(30)	NULL
);

CREATE TABLE `Vehicle_DB` (
	`vehicle_id`	serial	NOT NULL,
	`vehicle_name`	VARCHAR(30)	NULL,
	`electr_engine`	BOOLEAN	NULL,
	`battery_id`	serial	NOT NULL,
	`producer_id`	serial	NOT NULL
);

CREATE TABLE `Battery_Producer_DB` (
	`producer_id`	serial	NOT NULL,
	`producer_name`	VARCHAR(30)	NULL,
	`country`	VARCHAR(20)	NULL
);

CREATE TABLE `Battery_DB` (
	`battery_id`	serial	NOT NULL
);

CREATE TABLE `Untitled` (
	`battery_id`	serial	NOT NULL,
	`producer_id`	serial	NOT NULL
);

CREATE TABLE `Date_DB` (
	`date_id`	serial	NOT NULL,
	`date`	TIMESTAMP	NULL	COMMENT ''%Y-%m-%d %H:%M:%S''
);

CREATE TABLE `Monthly_DB` (
	`id`	serial	NOT NULL,
	`registered_car`	INT4	NULL,
	`electr_car_rate`	FLOAT	NULL,
	`region_id`	serial	NOT NULL,
	`date_id`	serial	NOT NULL
);

ALTER TABLE `Region_DB` ADD CONSTRAINT `PK_REGION_DB` PRIMARY KEY (
	`region_id`
);

ALTER TABLE `Vehicle_DB` ADD CONSTRAINT `PK_VEHICLE_DB` PRIMARY KEY (
	`vehicle_id`
);

ALTER TABLE `Battery_Producer_DB` ADD CONSTRAINT `PK_BATTERY_PRODUCER_DB` PRIMARY KEY (
	`producer_id`
);

ALTER TABLE `Battery_DB` ADD CONSTRAINT `PK_BATTERY_DB` PRIMARY KEY (
	`battery_id`
);

ALTER TABLE `Untitled` ADD CONSTRAINT `PK_UNTITLED` PRIMARY KEY (
	`battery_id`,
	`producer_id`
);

ALTER TABLE `Date_DB` ADD CONSTRAINT `PK_DATE_DB` PRIMARY KEY (
	`date_id`
);

ALTER TABLE `Monthly_DB` ADD CONSTRAINT `PK_MONTHLY_DB` PRIMARY KEY (
	`id`
);

ALTER TABLE `Vehicle_DB` ADD CONSTRAINT `FK_Battery_DB_TO_Vehicle_DB_1` FOREIGN KEY (
	`battery_id`
)
REFERENCES `Battery_DB` (
	`battery_id`
);

ALTER TABLE `Vehicle_DB` ADD CONSTRAINT `FK_Battery_Producer_DB_TO_Vehicle_DB_1` FOREIGN KEY (
	`producer_id`
)
REFERENCES `Battery_Producer_DB` (
	`producer_id`
);

ALTER TABLE `Untitled` ADD CONSTRAINT `FK_Battery_DB_TO_Untitled_1` FOREIGN KEY (
	`battery_id`
)
REFERENCES `Battery_DB` (
	`battery_id`
);

ALTER TABLE `Untitled` ADD CONSTRAINT `FK_Battery_Producer_DB_TO_Untitled_1` FOREIGN KEY (
	`producer_id`
)
REFERENCES `Battery_Producer_DB` (
	`producer_id`
);

ALTER TABLE `Monthly_DB` ADD CONSTRAINT `FK_Region_DB_TO_Monthly_DB_1` FOREIGN KEY (
	`region_id`
)
REFERENCES `Region_DB` (
	`region_id`
);

ALTER TABLE `Monthly_DB` ADD CONSTRAINT `FK_Date_DB_TO_Monthly_DB_1` FOREIGN KEY (
	`date_id`
)
REFERENCES `Date_DB` (
	`date_id`
);

