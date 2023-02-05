create table s_f33890ec9c814bb1d9227550d09e9947.vendor_x_registrations_deduped as (
  select
    *
  from
    (
      select
        *,
        row_number() over (partition by vendor_id, status)
      from
        vendor_x_registrations_raw
    ) as rows
  where
    row_number = 1
);
