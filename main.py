import subprocess

def start_packet_capture(interface, output_filename, capture_count=None, capture_duration=None):
    command = ["tcpdump", "-i", interface, "-w", output_filename]
    if capture_count is not None:
        command.extend(["-c", str(capture_count)])
    elif capture_duration is not None:
        command.extend(["-G", str(capture_duration), "-W", "1"])
    process = subprocess.Popen(command)
    try:
        process.wait()
    except KeyboardInterrupt:
        print("\n[*] Capture interrupted. Stopping the capture.")
        process.terminate()

def main():
    network_interface = "eth0"
    output_filename = "./captured_data.pcap"
    capture_count = None
    capture_duration = None
    start_packet_capture(network_interface, output_filename, capture_count, capture_duration)

if __name__ == "__main__":
    main()