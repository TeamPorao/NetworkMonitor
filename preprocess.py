import subprocess

input_pcap_file = "/home/nine/Downloads/Challenge_FINAL/captured_data.pcap"
output_pcap_file = "/home/nine/Downloads/Challenge_FINAL/filtered_data.pcap"
display_filter = "media.type"
try:
    subprocess.run(["tshark", "-r", input_pcap_file, "-w", output_pcap_file, "-Y", display_filter],check=True)
    print(f"[*] Pacotes filtrados salvos em: {output_pcap_file}")
except subprocess.CalledProcessError as e:
    print(f"[*] Erro ao executar TShark: {e}")