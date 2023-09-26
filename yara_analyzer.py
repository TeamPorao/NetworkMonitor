import os
import json
import pyshark
import requests
import tempfile
import yara  # Import the yara module
import re 

# Replace with your YARA rule file path
YARA_RULES_FILE = '/home/nine/Downloads/Challenge_FINAL/ransom.yar'

def get_hex_dump(packet):
    try:
        hex_dump = packet.tcp.payload.replace(":", "")
        return hex_dump
    except AttributeError:
        return None

def scan_with_yara(hex_dump, yara_rules):
    matches = yara_rules.match(data=bytes.fromhex(hex_dump))
    return matches

def apply_yara_rules(hex_dump):
    # Compile the YARA rules from the file
    try:
        yara_rules = yara.compile(YARA_RULES_FILE)
    except yara.Error as e:
        print(f"Error compiling YARA rules: {e}")
        return False

    # Match the hex dump against the YARA rules
    try:
        matches = yara_rules.match(data=bytes.fromhex(hex_dump))
        return bool(matches)  # True if there are matches, else False
    except yara.Error as e:
        print(f"Error applying YARA rules: {e}")
        return False

def main():
    pcap_file = '/home/nine/Downloads/Challenge_FINAL/filtered_data.pcap'
    output_file = '/home/nine/Downloads/Challenge_FINAL/frontend/Desktop/js-desktop/dados.json'

    if not os.path.exists(pcap_file):
        print(f"The file {pcap_file} does not exist.")
        return

    pcap = pyshark.FileCapture(pcap_file, display_filter='tcp')

    # Compile YARA rules
    yara_rules = yara.compile(YARA_RULES_FILE)

    results = []

    for packet in pcap:
        source_ip = packet.ip.src
        dest_ip = packet.ip.dst
        hex_dump = get_hex_dump(packet)
        capture_time = packet.sniff_time.strftime('%Y-%m-%d_%H-%M-%S')
        filename = f"capture_{capture_time}.porao"

        if hex_dump is not None:
            print(f"Hex Dump: {hex_dump}")  # Print the hex dump
            malware_detected = apply_yara_rules(hex_dump)

            result_entry = {
                'source_ip': source_ip,
                'destination_ip': dest_ip,
                'filename': filename,
                'malware_detected': malware_detected
            }
            results.append(result_entry)

    with open(output_file, 'w') as json_file:
        json.dump(results, json_file, indent=4)

if __name__ == "__main__":
    main()
