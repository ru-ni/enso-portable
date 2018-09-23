from enso import config
from telnetlib import Telnet

options = vars(config)
HOST = options["DD_WRT_HOST"].encode('ascii', 'ignore') if "DD_WRT_HOST" in options else b"192.168.1.1"
USER = options["DD_WRT_USER"].encode('ascii', 'ignore') if "DD_WRT_USER" in options else b"root"
PASSWORD = options["DD_WRT_PASSWORD"].encode('ascii', 'ignore') if "DD_WRT_PASSWORD" in options else b""
IFACE = options["DD_WRT_WIFI_INTERFACE"].encode('ascii', 'ignore') if "DD_WRT_WIFI_INTERFACE" in options else b"ra0"
MAC = options["DD_WRT_MAC"].encode('ascii', 'ignore') if "DD_WRT_MAC" in options else b"00:00:00:00:00:00"

def cmd_switch_wireless(ensoapi):
    """Turn wi-fi on/off"""
    tn = Telnet(HOST, 23)
    tn.read_until(b"login: ")
    tn.write(USER + b"\n")
    tn.read_until(b"Password: ")
    tn.write(PASSWORD + b"\n")
    tn.write("".join((b"ifconfig ", IFACE, "\n")))
    
    tn_out = tn.read_until(b"Interrupt")
    
    cmd = b""
    
    if tn_out.find(b" UP ") != -1:
        cmd = b" down"
    else:
        cmd = b" up"
    
    if len(cmd) != 0:
        tn.write(b"".join((b"ifconfig ", IFACE, cmd, b"\n")))
    
    tn.write("exit\n")
    tn.read_all()

def cmd_wake_slave(ensoapi):
    """Wake a slave server with a magic packet"""
    tn = Telnet(HOST, 23)
    tn.read_until(b"login: ")
    tn.write(USER + b"\n")
    tn.read_until(b"Password: ")
    tn.write(PASSWORD + b"\n")

    tn.write(b"/usr/sbin/wol -i 192.168.1.255 -p 9 " + MAC + b"\n") # provide a MAC address
    tn.write(b"exit\n")
    tn.read_all()

def cmd_wan_reconnect(ensoapi):
    """Reconnect WAN"""
    tn = Telnet(HOST, 23)
    tn.read_until(b"login: ")
    tn.write(USER + b"\n")
    tn.read_until(b"Password: ")
    tn.write(PASSWORD + b"\n")

    tn.write(b"killall -HUP pppd\n")
    tn.write(b"exit\n")
    tn.read_all()
