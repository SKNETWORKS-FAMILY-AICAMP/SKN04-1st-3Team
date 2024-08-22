CREATE TABLE `Region_DB` (
	`region_id`	serial	NOT NULL,
	`region_name`	VARCHAR(30)	NULL,
	`registered_car`	INT4	NULL,
	`electr_car_rate`	FLOAT	NULL
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

