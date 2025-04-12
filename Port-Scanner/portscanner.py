import socket
import ssl
import concurrent.futures
import re
import threading
import argparse

PROTOCOL_PAYLOADS = {
    21: b'USER anonymous\r\n',
    22: None,
    25: b'HELO test\r\n',
    80: b'GET / HTTP/1.1\r\nHost: target\r\n\r\n',
    110: b'USER test\r\n',
    143: b'A001 LOGIN test test\r\n',
    443: b'GET / HTTP/1.1\r\nHost: target\r\n\r\n',
    3306: b'\x03\x00\x00\x01\x85\xa2\x03\x00',
    6379: b'INFO\r\n'
}

SCANNED_PORTS = set()
lock = threading.Lock()

def portscan(target, port):
    with lock:
        if port in SCANNED_PORTS:
            return None
        SCANNED_PORTS.add(port)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        if s.connect_ex((target, port)) == 0:
            with lock:
                print(f"\n[+] Port {port} is open")
            return bannergrab(target, port, s)
    return None

def cleanbanner(banner):
    headers = banner.split("\r\n")
    useful_headers = [h for h in headers if re.match(r"^(Server|Date|Content-Type):", h)]
    return "\n".join(useful_headers)

def bannergrab(target, port, sock):
    try:
        if port == 443:
            with ssl.create_default_context().wrap_socket(sock, server_hostname=target) as ssl_sock:
                ssl_sock.sendall(PROTOCOL_PAYLOADS.get(port, b''))
                banner = ssl_sock.recv(2048).decode(errors="ignore").strip()
        else:
            if port in PROTOCOL_PAYLOADS and PROTOCOL_PAYLOADS[port]:
                sock.sendall(PROTOCOL_PAYLOADS[port])
            banner = sock.recv(2048).decode(errors="ignore").strip()

        if banner:
            if port in [80, 443]:
                banner = cleanbanner(banner)
            with lock:
                print(f"[+] Port {port} Banner:\n{banner}\n")
            return banner
    except (socket.timeout, ConnectionRefusedError, UnicodeDecodeError, ssl.SSLError):
        pass
    except Exception as e:
        print(f"[-] Error grabbing banner on {target}:{port}: {e}")

    return None

def main():
    parser = argparse.ArgumentParser(description="Port scanner with banner grabbing.")
    parser.add_argument("target", help="Target IP or Domain")
    args = parser.parse_args()

    target = args.target
    ports = sorted(set(PROTOCOL_PAYLOADS.keys()).union(set(range(20, 1025))))

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(portscan, [target] * len(ports), ports)

    print("[+] Scan completed.")

if __name__ == "__main__":
    main()
