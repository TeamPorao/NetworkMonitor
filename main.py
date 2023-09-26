import subprocess

def start_packet_capture(interface, output_filename, capture_count=None, capture_duration=None):
    # Define the command to capture packets with tcpdump
    command = ["tcpdump", "-i", interface, "-w", output_filename]

    # Add options for packet count or duration if specified
    if capture_count is not None:
        command.extend(["-c", str(capture_count)])
    elif capture_duration is not None:
        command.extend(["-G", str(capture_duration), "-W", "1"])

    # Start the packet capture using subprocess
    process = subprocess.Popen(command)

    try:
        process.wait()
    except KeyboardInterrupt:
        print("\n[*] Capture interrupted. Stopping the capture.")
        process.terminate()

def main():
    network_interface = "wlp2s0"  # Replace with the correct interface name
    output_filename = "./captured_data.pcap"
    capture_count = None  # Set to the desired packet count or None
    capture_duration = None  # Set to the desired capture duration in seconds or None

    # Start packet capture
    start_packet_capture(network_interface, output_filename, capture_count, capture_duration)

if __name__ == "__main__":
    main()