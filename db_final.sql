CREATE TABLE public.brand (
    brand_id int4 NOT NULL,
    brand_name varchar(30) NOT NULL,
    CONSTRAINT brand_pk PRIMARY KEY (brand_id)
);

CREATE TABLE public.producer (
    producer_id int4 NOT NULL,
    producer_name varchar(30) NOT NULL,
    country varchar(50) NOT NULL,
    CONSTRAINT producer_pk PRIMARY KEY (producer_id)
);

CREATE TABLE public.electric_vehicle (
    vehicle_id int4 NOT NULL,
    vehicle_name varchar(30) NOT NULL,
    CONSTRAINT electric_vehicle_pk PRIMARY KEY (vehicle_id)
);
CREATE TABLE public.registerd_vehicles (
    id int4 NOT NULL,
    region_name varchar(30) NOT NULL,
    registered_vehicles int4 NOT NULL,
    electr_car_rate float4 NOT NULL,
    "date" timestamp NOT NULL,
    CONSTRAINT registerd_vehicles_pk PRIMARY KEY (id)
);

ALTER TABLE public.electric_vehicle ADD brand_id int4 NULL;
ALTER TABLE public.electric_vehicle ADD CONSTRAINT electric_vehicle_brand_fk FOREIGN KEY (brand_id) REFERENCES public.brand(brand_id);
ALTER TABLE public.electric_vehicle ADD producer_id int4 NULL;
ALTER TABLE public.electric_vehicle ADD CONSTRAINT electric_vehicle_producer_fk FOREIGN KEY (producer_id) REFERENCES public.producer(producer_id);