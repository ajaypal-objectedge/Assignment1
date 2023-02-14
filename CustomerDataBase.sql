-- Table: public.Customer

-- DROP TABLE IF EXISTS public."Customer";

CREATE TABLE IF NOT EXISTS public."Customer"
(
    id integer PRIMARY KEY,
    "firstName" text COLLATE pg_catalog."default" NOT NULL,
    "lastName" text COLLATE pg_catalog."default",
    address text COLLATE pg_catalog."default",
    dob date,
    "createdBy " timestamp without time zone,
    "updatedBy" timestamp without time zone
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Customer"
    OWNER to postgres;