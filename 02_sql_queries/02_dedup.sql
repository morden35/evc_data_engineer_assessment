-- https://stackoverflow.com/questions/6127338/mysql-select-distinct-unique-but-return-all-columns
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
