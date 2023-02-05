create table s_f33890ec9c814bb1d9227550d09e9947.vendor_x_registrations_deduped(
    vendor_id  varchar,
    status  varchar,
    tracking_source  varchar,
    tracking_id  varchar,
    date_of_birth date,
    email_address  varchar,
    citizenship_confirmed bool,
    salutation  varchar,
    first_name  varchar,
    middle_name  varchar,
    last_name  varchar,
    name_suffix  varchar,
    home_address  varchar,
    home_unit int4,
    home_city  varchar,
    home_county  varchar,
    home_state   varchar,
    home_zip_code   varchar,
    mailing_address   varchar,
    mailing_unit int4,
    mailing_city  varchar,
    mailing_county  varchar,
    mailing_state  varchar,
    mailing_zip_code  varchar,
    party  varchar,
    race  varchar,
    phone  varchar,
    phone_type  varchar,
    opt_in_to_vendor_email bool,
    opt_in_to_vendor_sms bool,
    opt_in_to_partner_email bool,
    opt_in_to_partner_smsrobocall bool,
    volunteer_for_vendor bool,
    volunteer_for_partner bool,
    pre_registered bool,
    registration_date timestamp,
    finish_with_state bool,
    built_via_api bool,
    submitted_via_state_api bool,
    registration_source  varchar,
    shift_id int4,
    shift_type int4,
    office  varchar,
    vendor_a_shift_id int4,
    salutation_standardized  varchar,
    has_mailing_address_standardized bool,
    has_state_license_standardized bool,
    has_ssn_standardized bool,
    predicted_gender  varchar,
    org  varchar,
    evc_id  varchar,
    program_state  varchar,
    partner_id  int4,
    field_start timestamp,
    field_end timestamp
)
