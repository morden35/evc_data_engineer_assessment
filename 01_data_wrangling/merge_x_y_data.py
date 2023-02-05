"""
The goal of this file is to:
    1. Download Vendor Y's data from the API
    2. Merge Vendor Y's data with Vendor X's data
    3. Save merged data as csv file
"""

import pandas as pd
import requests


def download_vendor_y():
    """
    This function downloads Vendor Y's data form the API. If the download is successful,
    the downloaded data is passed to merge_vendor_x_y_data. If the download fails,
    we return a message with the status code.
    """
    url = "https://k4clzaf58d.execute-api.us-east-1.amazonaws.com/default/handle_users"
    response = requests.get(url)
    if response.status_code == 200:
        y_data = response.json()
        merge_vendor_x_y_data(y_data)
    else:
        return f"API Error: {response.status_code}"


def merge_vendor_x_y_data(y_data):
    """This function takes in Vendor Y's data in json format. It then converts the json
    to a pandas dataframe. It then imports Vendor X's data as a pandas dataframe. It then
    converts the column datatypes and renames columns for each dataframe. Finally, the functions
    merges the two dataframes into one, and saves as a csv file.
    """
    x_data_df = pd.read_csv("data/vendor_x_data.csv") # 147 rows, 55 columns
    y_data_df = pd.json_normalize(y_data['data']) # 147 rows, 55 columns
    
    # convert x_data_df column types
    x_data_df = x_data_df.astype({'VENDOR_ID': 'object',
                                'STATUS': 'object',
                                'TRACKING_SOURCE': 'object',
                                'TRACKING_ID': 'object',
                                'DATE_OF_BIRTH': 'datetime64',
                                'EMAIL_ADDRESS': 'object',
                                'CITIZENSHIP_CONFIRMED': 'bool',
                                'SALUTATION': 'object',
                                'FIRST_NAME': 'object',
                                'MIDDLE_NAME': 'object',
                                'LAST_NAME': 'object',
                                'NAME_SUFFIX': 'object',
                                'HOME_ADDRESS': 'object',
                                'HOME_UNIT': 'int32',
                                'HOME_CITY': 'object',
                                'HOME_COUNTY': 'object',
                                'HOME_STATE': 'object',
                                'HOME_ZIP_CODE': 'object',
                                'MAILING_ADDRESS': 'object',
                                'MAILING_UNIT': 'int32',
                                'MAILING_CITY': 'object',
                                'MAILING_COUNTY': 'object',
                                'MAILING_STATE': 'object',
                                'MAILING_ZIP_CODE': 'object',
                                'PARTY': 'object',
                                'RACE': 'object',
                                'PHONE': 'object',
                                'PHONE_TYPE':'object',
                                'OPT_IN_TO_VENDOR_EMAIL': 'bool',
                                'OPT_IN_TO_VENDOR_SMS': 'bool',
                                'OPT_IN_TO_PARTNER_EMAIL': 'bool',
                                'OPT_IN_TO_PARTNER_SMSROBOCALL': 'bool',
                                'VOLUNTEER_FOR_VENDOR': 'bool',
                                'VOLUNTEER_FOR_PARTNER': 'bool',
                                'PRE_REGISTERED': 'bool',
                                'REGISTRATION_DATE': 'datetime64',
                                'FINISH_WITH_STATE': 'bool',
                                'BUILT_VIA_API': 'bool',
                                'SUBMITTED_VIA_STATE_API': 'bool',
                                'REGISTRATION_SOURCE': 'object',
                                'SHIFT_ID': 'int32',
                                'SHIFT_TYPE': 'int32',
                                'OFFICE': 'object',
                                'VENDOR_A_SHIFT_ID': 'int32',
                                'SALUTATION_STANDARDIZED': 'object',
                                'HAS_MAILING_ADDRESS_STANDARDIZED': 'bool',
                                'HAS_STATE_LICENSE_STANDARDIZED': 'bool',
                                'HAS_SSN_STANDARDIZED': 'bool',
                                'PREDICTED_GENDER': 'object',
                                'ORG': 'object',
                                'EVC_ID': 'object',
                                'PROGRAM_STATE': 'object',
                                'PARTNER_ID': 'int32',
                                'FIELD_START': 'datetime64',
                                'FIELD_END': 'datetime64'})
    # rename x_data_df columns
    x_data_df = x_data_df.rename(columns={'VENDOR_ID': 'vendor_id',
                                        'STATUS': 'status',
                                        'TRACKING_SOURCE': 'tracking_source',
                                        'TRACKING_ID': 'tracking_id',
                                        'DATE_OF_BIRTH': 'date_of_birth',
                                        'EMAIL_ADDRESS': 'email_address',
                                        'CITIZENSHIP_CONFIRMED': 'citizenship_confirmed',
                                        'SALUTATION': 'salutation',
                                        'FIRST_NAME': 'first_name',
                                        'MIDDLE_NAME': 'middle_name',
                                        'LAST_NAME': 'last_name',
                                        'NAME_SUFFIX': 'name_suffix',
                                        'HOME_ADDRESS': 'home_address',
                                        'HOME_UNIT': 'home_unit',
                                        'HOME_CITY': 'home_city',
                                        'HOME_COUNTY': 'home_county',
                                        'HOME_STATE': 'home_state',
                                        'HOME_ZIP_CODE': 'home_zip_code',
                                        'MAILING_ADDRESS': 'mailing_address',
                                        'MAILING_UNIT': 'mailing_unit',
                                        'MAILING_CITY': 'mailing_city',
                                        'MAILING_COUNTY': 'mailing_county',
                                        'MAILING_STATE': 'mailing_state',
                                        'MAILING_ZIP_CODE': 'mailing_zip_code',
                                        'PARTY': 'party',
                                        'RACE': 'race',
                                        'PHONE': 'phone',
                                        'PHONE_TYPE': 'phone_type',
                                        'OPT_IN_TO_VENDOR_EMAIL': 'opt_in_to_vendor_email',
                                        'OPT_IN_TO_VENDOR_SMS': 'opt_in_to_vendor_sms',
                                        'OPT_IN_TO_PARTNER_EMAIL': 'opt_in_to_partner_email',
                                        'OPT_IN_TO_PARTNER_SMSROBOCALL': 'opt_in_to_partner_smsrobocall',
                                        'VOLUNTEER_FOR_VENDOR': 'volunteer_for_vendor',
                                        'VOLUNTEER_FOR_PARTNER': 'volunteer_for_partner',
                                        'PRE_REGISTERED': 'pre_registered',
                                        'REGISTRATION_DATE': 'registration_date',
                                        'FINISH_WITH_STATE': 'finish_with_state',
                                        'BUILT_VIA_API': 'built_via_api',
                                        'SUBMITTED_VIA_STATE_API': 'submitted_via_state_api',
                                        'REGISTRATION_SOURCE': 'registration_source',
                                        'SHIFT_ID': 'shift_id',
                                        'SHIFT_TYPE': 'shift_type',
                                        'OFFICE': 'office',
                                        'VENDOR_A_SHIFT_ID': 'vendor_a_shift_id',
                                        'SALUTATION_STANDARDIZED': 'salutation_standardized',
                                        'HAS_MAILING_ADDRESS_STANDARDIZED': 'has_mailing_address_standardized',
                                        'HAS_STATE_LICENSE_STANDARDIZED': 'has_state_license_standardized',
                                        'HAS_SSN_STANDARDIZED': 'has_ssn_standardized',
                                        'PREDICTED_GENDER': 'predicted_gender',
                                        'ORG': 'org',
                                        'EVC_ID': 'evc_id',
                                        'PROGRAM_STATE': 'program_state',
                                        'PARTNER_ID': 'partner_id',
                                        'FIELD_START': 'field_start',
                                        'FIELD_END': 'field_end'})

    # take care of ambiguous date column
    # years 00 - 23 are ambiguous
    # since folks can't vote until age 18, years 06-23 we will assume are from the 20th century
    # let's assume 00-05 are from the 21st century
    for idx, dob in enumerate(y_data_df['dob']):
        if int(dob[:2]) > 5:
            y_data_df['dob'][idx] = '19' + dob
        else:
            y_data_df['dob'][idx] = '20'+ dob
    y_data_df['dob'] = pd.to_datetime(y_data_df['dob'], yearfirst=True)
    
    # convert y_data_df column types
    y_data_df = y_data_df.astype({'registration_id': 'object',
                                'status': 'object',
                                'tracking_source': 'object',
                                'tracking_id': 'object',
                                'email': 'object',
                                'citizenship_confirmed': 'bool',
                                'salutation': 'object',
                                'first_name': 'object',
                                'middle_name': 'object',
                                'last_name': 'object',
                                'name_suffix': 'object',
                                'home_address': 'object',
                                'home_unit': 'int32',
                                'home_city': 'object',
                                'home_county': 'object',
                                'home_state': 'object',
                                'home_zip_code': 'object',
                                'mailing_address': 'object',
                                'mailing_unit': 'int32',
                                'mailing_city': 'object',
                                'mailing_county': 'object',
                                'mailing_state': 'object',
                                'mailing_zip_code': 'object',
                                'party': 'object',
                                'race': 'object',
                                'phone': 'object',
                                'phone_type': 'object',
                                'opt_in_to_vendor_email': 'bool',
                                'opt_in_to_vendor_sms': 'bool',
                                'opt_in_to_partner_email': 'bool',
                                'opt_in_to_partner_smsrobocall': 'bool',
                                'volunteer_for_vendor': 'bool',
                                'volunteer_for_partner': 'bool',
                                'pre_registered': 'bool',
                                'registration_date': 'datetime64',
                                'finish_with_state': 'bool',
                                'built_via_api': 'bool',
                                'submitted_via_state_api': 'bool',
                                'registration_source': 'object',
                                'shift_id': 'int32',
                                'shift_type': 'int32',
                                'office': 'object',
                                'vendor_a_shift_id': 'int32',
                                'salutation_standardized': 'object',
                                'has_mailing_address_standardized': 'bool',
                                'has_state_license_standardized': 'bool',
                                'has_ssn_standardized': 'bool',
                                'predicted_gender': 'object',
                                'org': 'object',
                                'evc_id': 'object',
                                'program_state': 'object',
                                'partner_id': 'int32',
                                'field_start': 'datetime64',
                                'field_end': 'datetime64'})

    # rename y_data_df columns
    y_data_df = y_data_df.rename(columns={'registration_id': 'vendor_id',
                                          'dob': 'date_of_birth',
                                          'email': 'email_address'})

    # merge 2 dataframes
    merged_df = x_data_df.merge(y_data_df, how='outer') # 294 rows, 55 columns

    # save merged data to data/all_vendors.csv
    merged_df.to_csv("data/all_vendors.csv", index=False)


if __name__ == "__main__":
    download_vendor_y()
