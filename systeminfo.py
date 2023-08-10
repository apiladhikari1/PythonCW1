import platform
import socket

def get_system_info():
    system_info = {}

    # Get general system information
    system_info['System'] = platform.system()
    system_info['Node Name'] = platform.node()
    system_info['Release'] = platform.release()
    system_info['Version'] = platform.version()
    system_info['Machine'] = platform.machine()
    system_info['Processor'] = platform.processor()

    # Get network information
    system_info['Hostname'] = socket.gethostname()
    system_info['IP Address'] = socket.gethostbyname(socket.gethostname())

    return system_info

if __name__ == "__main__":
    system_info = get_system_info()

    # Display system information
    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")
