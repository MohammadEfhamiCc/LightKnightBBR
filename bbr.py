import os
import shutil
import platform
import subprocess

def show_image():
    ascii_art = """
$$$$$$$$$$$%%%$$$$$$$$%%%%%%%%%$$$%%%%$$%%$$$$$%$$%%%%%%%%%%%%%%%%%%%$
$$$$$$$$$%%%%$$$$$$$$%%%%%%%%%%**!!****%%%***%%$$%%$$%%%%%%%%%%%%%%%%%
$$$$$$$$%%%%$$$$$$$$%%%%%$$*!!!**!*****!::!***!!*$$$%$$$%%%%%%%%%%%%%%
$$$$$$$%%%%%$$$$$$$%%%%$%*:!%$*:!%**!:!*%!::::!::!*%$$%%%%%%%%%%%%%%%%
$$$$$$%%%%$$$$$$$$%%%$$*:!%$*!*!:!*%%*::!%*::::::!!!!%%%%%%%%%%%%%%%%%
$$$$$%%%%$$$$%%$$%%%$$!:%%!:*%%!::!!*%%:::%*:::::::**:*%%%%$%%%%%%%%%%
%%$$%%%%$$$$$$$$%%%%*:!$$$*%&$%$$*%$%%@@::!@!:::::::!%::%$$$%%%%%%%%%%
%%%%%%$$$$$$$$$%%%$!.*#@$@&&%*%$@@&@%%&#&@$$$:::::::!!*::*$%%%%%%%%%%%
%%%%%$$$$$$$$$%%%$!:%&$$*%%:*%*!*!*$$**!$@$*@!:::::!*!:!::!%%%%%%%%%%%
%%%%%$$$$$$$$%%%$!:%$%%!!$!:::*:%:::%::!**!%*%:::::!%$:::::!%%%%%%%%%%
%%%%%%$$$$$$%%%$*:**%%%:$%:::**:$:::$::**%:::%::::::%$!::!::*$%%%%%%%%
%%%%%%%$$$$%%%%%:*!!$%!*%*:!!%*!$!:!$!:**%!::%!:::::%%!::!*::%@%%%%%%%
%%%%%%%%$%%%%%$!**:%$%!%%%%*****%***$!:****!!%*:::::%%*::*%::*$$%%%%%$
$$$$$$$$%%%%%$%%$:!%%%%***!:::::::*%%%%%%**!!%*:::::%%*::*$::!$%%%%%$$
$$$$$$$%%%%%%$%&!:*$$**!%!!:::::::::!*%*$%$*!$!:::::%$%::%$:*:$$!$%$$$
$$$$$$%%%%%%%@$%::*%$%%$$$%::::::::*%$$@@@&$!$::::::$%%::%$:*:$$:%$$$$
$$$$$%%%%%%%%$%!::%!*%%%$@@*:::::::!:*$$@@$%@*::::::$*%::$$:%!$$!!$$$$
$$$$%%%%%%%%$*%!!!%!!*!!!!:::::::::::!***::!@::::::!%%%!!$%!%*%@*!$$$$
$$$%%%%%%%%%$**!!%*!!!%::::!!::::::::::::::**:::::!***%**@*%$%$$**$$$$
$%%%%%%%$$$$%**!*!!!!!%!::::::::::::::::::!%:::::!*%!$*%%@*$$%@%*$$$$%
%%%%%%$$$$$$****!!!!!!*%::::::::::::::::::%*!!!%!**$$@$$$%%%%%$$$$$$%%
%%%%%%$$%%%$!*%!!!!!:**$%!::::::!!::::***%%*%*****$$@$$$%%%%$%%%%%%%$$
%%%%$$%%%%%%!**!!!!::*$%%%*!::::::::::*%$$!!!!!!%%$$@$%%%%$%%%%%%%$$%%
%%%$$$%%%%$!!!!!!!!:!$%%%%%%*!:::::!!*%%$*!!!:!!*%&&&%%%$#S&@$$&$&S#@&
%%$$$$$$@%%::!!!!!::%@%%%%%%$$*%%%%%**%@$::::::!*$@@@@S#SSSSSSSSSSSSSS
%$$$$$$%#S*:::::::::&#####&&S@%@S#$@&#SS*:::::!*%$@$&SSSSSSSSSSSSSSSSS
%%$$$%%$S#::::!!:::!$*$@#SB#%!!#SSSS##S@:!::!:**SS##SSSSSSSSSSSSSSSSSS
%%%%%%@#S@:::!!!!!$S%.:%##%..*##@&####S%:!:!!!**SSSSBSSSS&S@%&##SSSSSS
%%%%%%$SS%!!!!!!!!!**.*S&!.*&S@$$$@###&!!!!!:!!$SSSSBSSSS@$$@##SSSSSSS
%$$$$&#S#*!!!!!!!!:!!:@$!%&SS@$$$@@##S@:!!!!!*!@S#&&@@$*%@##SSSSSSSSSS
%@SSSSSS@!!!!!!!!!!!!$@@#SS#@$&##SSSSS$!!!!!!*:@S@:::.:*#SSSSSSSSSSSSS
#SSS##S&%!!!!!!!!!!@&#####&@$&SSSSSSSS%!!!!:*%:$&!::.%#SSSSSSSSSSSSSSS
SSS##S#$%!!!!!!!*$&######@$$@$&SSSS###S&*!!!!:%*!%!::%#BSSSSSSSSSSSSSS
SSSSSS$%*!!!!!%@#######&$$@$&SSSS###S@*!!!!:%*!!%::@BSSSSSSSSSSSSSSSSS
SSSSS#$%*!!!%&########@$$$$@SSS#####S@*!!!!!**!!%!&SSSSSSSSSSSSSSSSSSS
    """
    print(ascii_art)

def show_main_menu():
    show_image()
    print("\nV 1.3")
    print("\nSpecial thanks to the Queen")
    print("\nView the project on GitHub: https://github.com/kalilovers")
    print("\nLightKnight Simple Script For Simple and Stable BBR")
    print("1_BBR Fq")
    print("2_BBR Fq_Codel(Recommend - Especially For IPSec And Local TUNS)")
    print("3_CakePlus (With BBR)")
    print("4_Restore Default BBR/Settings")
    print("5_Speed Test")
    print("0_Exit")

def show_fq_menu():
    print("\nFq")
    print("1_Delete Old File Then Setup(+Backup)")
    print("2_Setup Without Delete")
    print("0_Back")

def show_fq_codel_menu():
    print("\nFq_Codel")
    print("1_Delete Old File Then Setup(+Backup)")
    print("2_Setup Without Delete")
    print("0_Back")

def show_cake_menu():
    print("\nCakePlus")
    print("1_Delete Old File Then Setup(+Backup)")
    print("2_Setup Without Delete")
    print("0_Back")

def show_speed_test_menu():
    print("\nSpeed Test")
    print("1_Bench Method1")
    print("2_Bench Method2")
    print("3_Iperf3 (Between 2 Server)")
    print("4_Speedtest Ookla")
    print("0_Back")

def show_iperf_menu():
    print("\nChoose which one you are:")
    print("1_Client (iran or...)")
    print("2_Server (Kharej/Target or...)")
    print("0_Back")

def install_required_packages():
    print("Checking and installing required packages...")
    required_packages = ['iproute2', 'iptables']
    missing_packages = []
    for package in required_packages:
        result = subprocess.run(['dpkg', '-s', package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode != 0:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"The following packages are not installed: {', '.join(missing_packages)}")
        
        install_confirm = input("Do you want to install these packages? (y/n): ").strip().lower()
        
        if install_confirm in ['y', 'yes']:
            print(f"Installing: {', '.join(missing_packages)}")
            subprocess.run(['apt', 'update'])
            subprocess.run(['apt', 'install', '-y'] + missing_packages)
            print("Required packages have been installed.")
        else:
            print("Installation of required packages was skipped. Exiting the script.")
            exit(1)
    else:
        print("All required packages are installed.")
    
    return True

def check_kernel_and_os():
    print("Checking the compatibility of operating system and kernel...")
    try:
        with open("/etc/os-release", "r") as f:
            lines = f.readlines()
        distro = ""
        for line in lines:
            if line.startswith("ID="):
                distro = line.strip().split("=")[1].strip('"').lower()
                break
    except FileNotFoundError:
        distro = ""

    if distro not in ['ubuntu', 'debian']:
        print("The operating system is not supported. Only Ubuntu and Debian are supported.")
        return False

    kernel_version = platform.release()
    version_numbers = kernel_version.split(".")
    try:
        kernel_major = int(version_numbers[0])
        kernel_minor = int(version_numbers[1])
    except (IndexError, ValueError):
        print(f"Kernel version {kernel_version} could not be detected.")
        return False

    if kernel_major > 4 or (kernel_major == 4 and kernel_minor >= 9):
        print(f"The kernel version is compatible with BBR.")
        return True
    else:
        print(f"Kernel version {kernel_version} is not supported. Requires version 4.9 or higher.")
        return False

def check_kernel_and_os_cake():
    print("Checking the compatibility of operating system and kernel for Cake...")
    try:
        with open("/etc/os-release", "r") as f:
            lines = f.readlines()
        distro = ""
        for line in lines:
            if line.startswith("ID="):
                distro = line.strip().split("=")[1].strip('"').lower()
                break
    except FileNotFoundError:
        distro = ""

    if distro not in ['ubuntu', 'debian']:
        print("The operating system is not supported. Only Ubuntu and Debian are supported.")
        return False

    kernel_version = platform.release()
    version_numbers = kernel_version.split(".")
    try:
        kernel_major = int(version_numbers[0])
        kernel_minor = int(version_numbers[1])
    except (IndexError, ValueError):
        print(f"Kernel version {kernel_version} could not be detected.")
        return False

    if kernel_major > 4 or (kernel_major == 4 and kernel_minor >= 19):
        print(f"The kernel version is compatible with Cake and BBR.")
        return True
    else:
        print(f"Kernel version {kernel_version} is not supported. Requires version 4.19 or higher.")
        return False

def activate_ecn_persistent():
    print("Activating ECN persistently...")
    try:
        with open("/etc/sysctl.conf", "a") as f:
            f.write("\n# Enable ECN\n")
            f.write("net.ipv4.tcp_ecn = 1\n")
        subprocess.run(['sysctl', '-p'])
        print("ECN activated and will remain active after reboot.")
        return True
    except Exception as e:
        print(f"ECN activation error: {e}")
        return False

def configure_bbr(algorithm):
    print("Setting up BBR...")

    if activate_ecn_persistent():
        print("ECN has been activated with BBR.")

    try:
        with open("/etc/sysctl.conf", "a") as f:
            f.write(f"\n# {algorithm} Light Knight\n")
            f.write(f"net.core.default_qdisc = {algorithm}\n")
            f.write("net.ipv4.tcp_congestion_control = bbr\n")
        subprocess.run(['sysctl', '-p'])
        print("BBR settings applied.")
    except Exception as e:
        print(f"Error in setting BBR: {e}")
        return False

    if not setup_qdisc(algorithm):
        return False

    if not make_qdisc_persistent(algorithm):
        return False

    return True


def get_main_interface():
    """Find the main interface based on 'UP' status and highest MTU."""
    try:
        interfaces = os.listdir("/sys/class/net/")
        main_interface = None
        highest_mtu = -1
        virtual_interfaces = ['tun', 'docker', 'veth', 'lo', 'br', 'gre', 'sit', 'vxlan', 'tap', 'gretap', 'ipip']

        for interface in interfaces:
            if any(interface.startswith(v) for v in virtual_interfaces):
                continue

            result = subprocess.run(['ip', 'addr', 'show', interface], capture_output=True, text=True)
            if "UP" in result.stdout:
                try:
                    with open(f"/sys/class/net/{interface}/mtu", "r") as mtu_file:
                        mtu = int(mtu_file.read().strip())
                        if mtu > highest_mtu:
                            highest_mtu = mtu
                            main_interface = interface
                except Exception as e:
                    print(f"Error reading MTU for {interface}: {e}")

        if main_interface:
            print(f"Main interface detected: {main_interface} with MTU {highest_mtu}")
            return main_interface
        else:
            print("No main interface found.")
            return None

    except Exception as e:
        print(f"Error detecting main interface: {e}")
        return None


def setup_qdisc(algorithm):
    """Apply the Qdisc to the main interface."""
    print("Setting the queuing algorithm on the main network interface...")
    interface = get_main_interface()
    
    if not interface:
        print("No main network interface found. Exiting script.")
        return False

    try:
        subprocess.run(['tc', 'qdisc', 'replace', 'dev', interface, 'root', algorithm], check=True)
        print(f"The {algorithm} queuing algorithm was set on the {interface} interface.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error in setting the queuing algorithm on {interface}: {e}. Exiting script.")
        return False


def make_qdisc_persistent(algorithm):
    """Create a systemd service to persist the Qdisc settings after reboot."""
    print("Creating systemd service to preserve qdisc settings after reboot on the main interface...")

    interface = get_main_interface()
    
    if not interface:
        print("No main network interface found. Exiting script.")
        return False

    exec_command = f"/sbin/tc qdisc replace dev {interface} root {algorithm}"

    service_content = f"""[Unit]
Description=Set qdisc {algorithm} on the main network interface
After=network.target

[Service]
Type=oneshot
ExecStart=/bin/sh -c '{exec_command}'
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
"""
    service_path = "/etc/systemd/system/qdisc-setup.service"
    try:
        with open(service_path, "w") as f:
            f.write(service_content)
        subprocess.run(['systemctl', 'daemon-reload'])
        subprocess.run(['systemctl', 'enable', 'qdisc-setup.service'])
        subprocess.run(['systemctl', 'start', 'qdisc-setup.service'])
        print("The systemd service was successfully created and activated for the main interface.")
        return True
    except Exception as e:
        print(f"Error creating systemd service: {e}. Exiting script.")
        return False

def prompt_restart():
    while True:
        try:
            choice = input("The mission was successfully completed. Do you want to restart? (Required) Yes or No: ").strip().lower()

            if choice in ['n', 'no']:
                break
            elif choice in ['y', 'yes']:
                os.system("reboot")
                break
            else:
                print("Invalid input. Please enter Yes or No.")
        except UnicodeDecodeError:
            print("Invalid input. Please use only English characters.")

def delete_old_file_then_setup(algorithm):
    print("Deleting old files and setting new (+Backup)...")
    backup_path = "/etc/sysctl.confback"
    original_path = "/etc/sysctl.conf"

    try:
        if os.path.exists(original_path):
            shutil.copy(original_path, backup_path)
            os.remove(original_path)
            print("The old sysctl.conf file was deleted and backed up.")
        else:
            print("No original sysctl.conf file to delete.")
    except Exception as e:
        print(f"Error deleting old files: {e}")
        return False

    if configure_bbr(algorithm):
        prompt_restart()
    else:
        print("BBR settings encountered a problem.")
    return True

def setup_without_delete(algorithm):
    print("Setting up without deleting old files...")
    backup_path = "/etc/sysctl.confback"
    original_path = "/etc/sysctl.conf"

    try:
        if not os.path.exists(backup_path):
            shutil.copy(original_path, backup_path)
            print("sysctl.conf file backed up successfully.")
    except Exception as e:
        print(f"Error backing up sysctl.conf: {e}")
        return False

    if configure_bbr(algorithm):
        prompt_restart()
    else:
        print("BBR settings encountered a problem.")
    return True

def restore():
    print("Restoring default settings...")
    backup_path = "/etc/sysctl.confback"
    original_path = "/etc/sysctl.conf"

    try:
        if os.path.exists(backup_path):
            if os.path.exists(original_path):
                os.remove(original_path)
                print("Removed the original sysctl.conf file.")
            shutil.copy(backup_path, original_path)
            print("Restored sysctl.conf backup.")
            os.remove(backup_path)
            print("Backup sysctl.conf file removed.")
        else:
            print("No backup found for sysctl.conf.")
    except Exception as e:
        print(f"Error restoring sysctl.conf backup: {e}")

    service_path = "/etc/systemd/system/qdisc-setup.service"
    try:
        if os.path.exists(service_path):
            subprocess.run(['systemctl', 'disable', 'qdisc-setup.service'])
            os.remove(service_path)
            subprocess.run(['systemctl', 'daemon-reload'])
            print("The systemd service related to qdisc was removed.")
        if os.path.exists("/etc/systemd/system/multi-user.target.wants/qdisc-setup.service"):
            os.remove("/etc/systemd/system/multi-user.target.wants/qdisc-setup.service")
            print("Removed /etc/systemd/system/multi-user.target.wants/qdisc-setup.service.")
    except Exception as e:
        print(f"Error deleting systemd service: {e}")

    interface = get_main_interface()
    if interface:
        try:
            subprocess.run(['tc', 'qdisc', 'delete', 'dev', interface, 'root'], check=True)
            print(f"Default qdisc settings on {interface} were restored.")
        except subprocess.CalledProcessError:
            print(f"Default qdisc settings could not be reset on {interface}. Applying fq instead.")
            subprocess.run(['tc', 'qdisc', 'replace', 'dev', interface, 'root', 'fq'], check=True)
            print(f"The fq queuing algorithm was set on the {interface} interface.")
    else:
        print("No main network interface found to restore settings.")

    try:
        subprocess.run(['sysctl', '-p'])
        print("sysctl settings applied.")
    except Exception as e:
        print(f"Error applying sysctl settings: {e}")

    prompt_restart()
    return True


def run_bench_method1():
    print("Running Bench Method1...")
    os.system("wget -qO- bench.sh | bash")

def run_bench_method2():
    print("Running Bench Method2...")
    os.system("curl -Lso- bench.sh | bash")

def run_iperf_client():
    print("Starting Iperf3 as client...")
    os.system("apt update")
    os.system("apt install iperf3 -y")
    os.system("ufw allow 5201")
    server_ip = input("What is the IP address of your target server? Enter Your Target IP: ")
    os.system(f"iperf3 -c {server_ip} -i 1 -t 10 -P 20")
    input("The download speed test was done. To test the upload speed, press Enter...")
    os.system(f"iperf3 -c {server_ip} -R -i 1 -t 10 -P 20")
    input("The upload speed test was done. To Back to the menu, press Enter...")

def run_iperf_server():
    print("Starting Iperf3 as server...")
    os.system("apt update")
    os.system("apt install iperf3 -y")
    os.system("ufw allow 5201")
    os.system("iperf3 -s")
    input("You are active as a server, please do not log out. If it is finished, to Back to the menu, press Enter...")

def run_speedtest_ookla():
    print("Downloading and running Ookla Speedtest...")
    os.system("wget https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-linux-x86_64.tgz")
    os.system("tar zxvf ookla-speedtest-1.2.0-linux-x86_64.tgz")
    server_num = input("Enter your ookla-server number. Or press Enter to use the Amsterdam server by default: ")
    if not server_num:
        server_num = "54746"
    os.system(f"./speedtest -s {server_num}")
    input("SpeedTest Done, please do not log out. If it is finished, to Back to the menu, press Enter...")

def main():
    while True:
        show_main_menu()
        choice = input("Please enter your choice: ")

        if choice == '1':
            while True:
                show_fq_menu()
                fq_choice = input("Please enter your choice: ")
                if fq_choice == '1':
                    if check_kernel_and_os():
                        install_required_packages()
                        delete_old_file_then_setup("fq")
                elif fq_choice == '2':
                    if check_kernel_and_os():
                        install_required_packages()
                        setup_without_delete("fq")
                elif fq_choice == '0':
                    break
                else:
                    print("Invalid choice, please try again.")
        elif choice == '2':
            while True:
                show_fq_codel_menu()
                fq_codel_choice = input("Please enter your choice: ")
                if fq_codel_choice == '1':
                    if check_kernel_and_os():
                        install_required_packages()
                        delete_old_file_then_setup("fq_codel")
                elif fq_codel_choice == '2':
                    if check_kernel_and_os():
                        install_required_packages()
                        setup_without_delete("fq_codel")
                elif fq_codel_choice == '0':
                    break
                else:
                    print("Invalid choice, please try again.")
        elif choice == '3':
            while True:
                show_cake_menu()
                cake_choice = input("Please enter your choice: ")
                if cake_choice == '1':
                    if check_kernel_and_os_cake():
                        install_required_packages()
                        delete_old_file_then_setup("cake")
                elif cake_choice == '2':
                    if check_kernel_and_os_cake():
                        install_required_packages()
                        setup_without_delete("cake")
                elif cake_choice == '0':
                    break
                else:
                    print("Invalid choice, please try again.")
        elif choice == '4':
            restore()
        elif choice == '5':
            while True:
                show_speed_test_menu()
                speed_test_choice = input("Please enter your choice: ")
                if speed_test_choice == '1':
                    run_bench_method1()
                elif speed_test_choice == '2':
                    run_bench_method2()
                elif speed_test_choice == '3':
                    while True:
                        show_iperf_menu()
                        iperf_choice = input("Please enter your choice: ")
                        if iperf_choice == '1':
                            run_iperf_client()
                        elif iperf_choice == '2':
                            run_iperf_server()
                        elif iperf_choice == '0':
                            break
                        else:
                            print("Invalid choice, please try again.")
                elif speed_test_choice == '4':
                    run_speedtest_ookla()
                elif speed_test_choice == '0':
                    break
                else:
                    print("Invalid choice, please try again.")
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
