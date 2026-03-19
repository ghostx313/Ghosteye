import platform
import socket


class sysinfo:
    try:

        def get_info(self):

            hostname = socket.gethostname()

            arch = platform.architecture()
            oprating_system = platform.platform()
            machine = platform.machine()
            node = platform.node()
            uname = platform.uname()
            sys = platform.system()
            release = platform.release()

            messages = print(
                f"sys_arch: {arch}\n"
                f"os_oprating: {oprating_system}\n"
                f"machine: {machine}"
                f"node: {node}\n"
                f"uname: {uname}\n"
                f"sys: {sys}\n"
                f"reslease: {release}\n"
                f"host_ipaddess:{hostname}"
            )

            print(messages)

    except Exception as e:
        print(f"invaild: {e}")


# D = sysinfo()
# D.get_info()
