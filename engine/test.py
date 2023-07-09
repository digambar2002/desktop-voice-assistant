import subprocess
import re


def handle_call():
    # Implement your desired functionality here
    print("Incoming call alert!")


def monitor_calls():
    print("runnig")
    adb_command = ['adb', 'shell', 'dumpsys', 'telephony.registry']
    pattern = r"mCallState(?:String)?=\s*(\d+)"

    while True:
        print("runnig")
        result = subprocess.run(adb_command, capture_output=True, text=True)
        output = result.stdout.strip()

        match = re.search(pattern, output)
        if match:
            call_state = int(match.group().split("=")[1])
            if call_state == 2:  # CALL_STATE_RINGING
                handle_call()


monitor_calls()
