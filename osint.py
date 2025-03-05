import requests
from colorama import Fore, Style, init
import sys
import os
import base64 as b64
import binascii as ba

username = input(Fore.RED + "target" + Fore.WHITE + "@")

headers = {
    'accept-language': 'en-US;q=1.0',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'user-agent': 'Instagram 337.0.3.23.54 (iPhone12,1; iOS 16_6; en_US; en; scale=2.00; 828x1792; 577210397) AppleWebKit/420+',
}

data = {
    "q": username,
}

try:
    response = requests.post("https://i.instagram.com/api/v1/users/lookup/", headers=headers, data=data)
    response.raise_for_status()    

    response_json = response.json()

    print(Fore.WHITE + "Response Details:")

    print(Fore.RED + "Multiple Users Found: " + Fore.WHITE + str(response_json.get('multiple_users_found', 'N/A')))
    print(Fore.RED + "Email Sent: " + Fore.WHITE + str(response_json.get('email_sent', 'N/A')))
    print(Fore.RED + "SMS Sent: " + Fore.WHITE + str(response_json.get('sms_sent', 'N/A')))
    print(Fore.RED + "WA Sent: " + Fore.WHITE + str(response_json.get('wa_sent', 'N/A')))
    print(Fore.RED + "Lookup Source: " + Fore.WHITE + response_json.get('lookup_source', 'N/A'))
    print(Fore.RED + "Corrected Input: " + Fore.WHITE + response_json.get('corrected_input', 'N/A'))
    print(Fore.RED + "Show UHL Entry in Verification Steps: " + Fore.WHITE + str(response_json.get('show_uhl_entry_in_verification_steps', 'N/A')))
    print(Fore.RED + "UHL Entry Eligible CPS: " + Fore.WHITE + str(response_json.get('uhl_entry_eligible_cps', 'N/A')))
    print(Fore.RED + "Obfuscated Phone: " + Fore.WHITE + response_json.get('obfuscated_phone', 'N/A'))

    user = response_json.get('user', {})
    print(Fore.RED + "User Information:")
    print(Fore.RED + "  Full Name: " + Fore.WHITE + user.get('full_name', 'N/A'))
    print(Fore.RED + "  Username: " + Fore.WHITE + user.get('username', 'N/A'))
    print(Fore.RED + "  Profile Pic URL: " + Fore.WHITE + user.get('profile_pic_url', 'N/A'))
    print(Fore.RED + "  Verified: " + Fore.WHITE + str(user.get('is_verified', 'N/A')))

    print(Fore.RED + "Has Valid Phone: " + Fore.WHITE + str(response_json.get('has_valid_phone', 'N/A')))
    print(Fore.RED + "Can Email Reset: " + Fore.WHITE + str(response_json.get('can_email_reset', 'N/A')))
    print(Fore.RED + "Can SMS Reset: " + Fore.WHITE + str(response_json.get('can_sms_reset', 'N/A')))
    print(Fore.RED + "Can WA Reset: " + Fore.WHITE + str(response_json.get('can_wa_reset', 'N/A')))
    print(Fore.RED + "Is WA Timing Signal: " + Fore.WHITE + str(response_json.get('is_wa_timing_signal', 'N/A')))
    print(Fore.RED + "WA Account Recovery Type: " + Fore.WHITE + response_json.get('wa_account_recovery_type', 'N/A'))
    print(Fore.RED + "Can P2S Reset: " + Fore.WHITE + str(response_json.get('can_p2s_reset', 'N/A')))
    print(Fore.RED + "Can Flashcall Reset: " + Fore.WHITE + str(response_json.get('can_flashcall_reset', 'N/A')))
    print(Fore.RED + "Phone Number: " + Fore.WHITE + response_json.get('phone_number', 'N/A'))
    print(Fore.RED + "Email: " + Fore.WHITE + str(response_json.get('email', 'N/A')))

    print(Fore.RED + "FB Login Option: " + Fore.WHITE + str(response_json.get('fb_login_option', 'N/A')))
    print(Fore.RED + "P2S Option Position: " + Fore.WHITE + response_json.get('p2s_option_position', 'N/A'))
    print(Fore.RED + "Autosend Disabled: " + Fore.WHITE + str(response_json.get('autosend_disabled', 'N/A')))
    print(Fore.RED + "Toast Message: " + Fore.WHITE + response_json.get('toast_message', 'N/A'))
    print(Fore.RED + "Can Recover with Code: " + Fore.WHITE + str(response_json.get('can_recover_with_code', 'N/A')))
    print(Fore.RED + "Status: " + Fore.WHITE + response_json.get('status', 'N/A'))

except requests.RequestException as e:
    print(Fore.RED + f"An error occurred: {e}")