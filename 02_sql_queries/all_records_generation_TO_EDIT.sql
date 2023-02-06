drop table if exists s_f33890ec9c814bb1d9227550d09e9947.all_records;
create table s_f33890ec9c814bb1d9227550d09e9947.all_records as (
    select
        application_id
        , org_id
        , shift_id
        , first_name
        , middle_name
        , last_name
        , name_suffix
        , voting_street_address_one
        , voting_street_address_two
        , voting_city
        , voting_state
        , voting_zipcode
        , mailing_street_address_one
        , mailing_street_address_two
        , mailing_city
        , mailing_state
        , mailing_zipcode
        , county
        , gender
        , date_of_birth
        -- , phone_number
        , email_address
        , updated_at
        , party
        , name_prefix
        , ethnicity
        , latitude
        , longitude
        , completed
        , registration_date
        , shift_type
        , locations_state
        , program_type
        , program_sub_type
        , collection_medium
        , office
        , field_start
        , field_end
        , evc_month
        , evc_year
    from public.qc_vendor_data
)
union
select
  vendor_id as application_id,
  org as org_id,
  shift_id,
  first_name,
  middle_name,
  last_name,
  name_suffix,
  home_address as voting_street_address_on,
  home_unit as voting_street_address_two,
  home_city as voting_city,
  home_state as voting_state,
  home_zip_code as voting_zipcode,
  mailing_address as mailing_street_address_one,
  mailing_unit as mailing_street_address_two,
  mailing_city,
  mailing_state,
  mailing_zip_code as mailing_zipcode,
  mailing_county as county,
  predicted_gender as gender,
  date_of_birth,
  -- CAST(phone as int) as phone_number
  email_address,
  CAST(NULL AS timestamp) as updated_at,
  party,
  salutation as name_prefix,
  CAST(NULL AS varchar) as ethnicity,
  CAST(NULL AS float8) as latitude,
  CAST(NULL AS float8) as longitude,
  CAST(NULL AS bool) as completed,
  registration_date,
  shift_type,
  program_state as locations_state,
  'field' as program_type,
  'evc_funded' as program_sub_type,
  registration_source as collection_medium,
  office,
  field_start,
  field_end,
  CAST(NULL AS varchar) as evc_month,
  CAST(NULL AS varchar) as evc_year
from
  vendor_x_registrations_raw
