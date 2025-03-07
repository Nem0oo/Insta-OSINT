import requests
import sys
from pathlib import Path
import json

def main():
    usage = "Usage : osint.py [username] [--json path/to/file.json]"
    pathJSON = ""
    match(len(sys.argv)):
        case 1:
            username = input("target : @")
        case 2:
            if sys.argv[1] != "--json":
                username = sys.argv[1]
            else:
                print(usage)
                quit()
        case 4:
            username = sys.argv[1]
            pathJSON = sys.argv[3]
        case _:
            print(usage)
            quit()

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
        if pathJSON != "":
            with open(Path(pathJSON), "w") as f:
                json.dump(response_json,f)

        print("Response Details:")

        print("Multiple Users Found: " + str(response_json.get('multiple_users_found', 'N/A')))
        print("Email Sent: " + str(response_json.get('email_sent', 'N/A')))
        print("SMS Sent: " + str(response_json.get('sms_sent', 'N/A')))
        print("WA Sent: " + str(response_json.get('wa_sent', 'N/A')))
        print("Lookup Source: " + response_json.get('lookup_source', 'N/A'))
        print("Corrected Input: " + response_json.get('corrected_input', 'N/A'))
        print("Show UHL Entry in Verification Steps: " + str(response_json.get('show_uhl_entry_in_verification_steps', 'N/A')))
        print("UHL Entry Eligible CPS: " + str(response_json.get('uhl_entry_eligible_cps', 'N/A')))
        print("Obfuscated Phone: " + response_json.get('obfuscated_phone', 'N/A'))

        user = response_json.get('user', {})
        print("User Information:")
        print(" -  Full Name: " + user.get('full_name', 'N/A'))
        print(" -  Username: " + user.get('username', 'N/A'))
        print(" -  Profile Pic URL: " + user.get('profile_pic_url', 'N/A'))
        print(" -  Verified: " + str(user.get('is_verified', 'N/A')))

        print("Has Valid Phone: " + str(response_json.get('has_valid_phone', 'N/A')))
        print("Can Email Reset: " + str(response_json.get('can_email_reset', 'N/A')))
        print("Can SMS Reset: " + str(response_json.get('can_sms_reset', 'N/A')))
        print("Can WA Reset: " + str(response_json.get('can_wa_reset', 'N/A')))
        print("Is WA Timing Signal: " + str(response_json.get('is_wa_timing_signal', 'N/A')))
        print("WA Account Recovery Type: " + response_json.get('wa_account_recovery_type', 'N/A'))
        print("Can P2S Reset: " + str(response_json.get('can_p2s_reset', 'N/A')))
        print("Can Flashcall Reset: " + str(response_json.get('can_flashcall_reset', 'N/A')))
        print("Phone Number: " + response_json.get('phone_number', 'N/A'))
        print("Email: " + str(response_json.get('email', 'N/A')))

        print("FB Login Option: " + str(response_json.get('fb_login_option', 'N/A')))
        print("P2S Option Position: " + response_json.get('p2s_option_position', 'N/A'))
        print("Autosend Disabled: " + str(response_json.get('autosend_disabled', 'N/A')))
        print("Toast Message: " + response_json.get('toast_message', 'N/A'))
        print("Can Recover with Code: " + str(response_json.get('can_recover_with_code', 'N/A')))
        print("Status: " + response_json.get('status', 'N/A'))

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()