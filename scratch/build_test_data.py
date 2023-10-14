#!/usr/bin/env python3
import json

from netaddr import IPAddress, IPNetwork

IPV4_TEST_LIST = [
    "10.0.0.0/8",  # RFC1918 - private unicast
    "100.64.0.0/10",  # RFC6598 - shared address space (sort of private)
    "169.254.0.0/16",  # RFC3927 - link-local unicast
    "224.0.0.0/24",  # RFC5771 - local network control block multicast
    "224.1.0.0/16",  # RFC5771 - reserved multicast
    "239.0.0.0/8",  # RFC5771 - administratively scoped block multicast
    "8.8.8.0/24",  # RFC6890 - public unicast - LVLT-GOGL-8-8-8
]

IPV6_TEST_LIST = [
    "100::/64",  # RFC6666 - Discard-Only Address Block"
    "2000::/3",  # RFC3587 - Global Unicast
    "2001::/23",  # RFC2928 - IETF Protocol Assignments
    "64:ff9b::/96",  # RFC6052 - IPv4/IPv6 Translation
    "fc00::/7",  # RFC4193 - Unique Local Unicast
    "fe80::/10",  # RFC4291 - Link-Local Unicast
    "ff00::/8",  # RFC3513 - Multicast
]


def expand_ip_list(ip_list: list[str], ipver: int) -> list[str]:
    """Build a list of IP addresses & networks using seed data."""
    ip_expanded_test_list = []

    if ipver == 4:
        loopback_mask_length = 32
    if ipver == 6:
        loopback_mask_length = 128

    for ip_range in ip_list:
        network = IPNetwork(ip_range)
        first_usable_ip = str(network.ip + 1)
        first_usable_ip_with_prefix = f"{first_usable_ip}/{network.prefixlen}"
        loopback_ip = f"{IPAddress(first_usable_ip)}/{loopback_mask_length}"
        broadcast_ip = f"{network.broadcast}/{network.prefixlen}"

        ip_expanded_test_list.append(str(network))
        ip_expanded_test_list.append(first_usable_ip_with_prefix)
        ip_expanded_test_list.append(first_usable_ip)
        ip_expanded_test_list.append(loopback_ip)
        ip_expanded_test_list.append(broadcast_ip)

    return ip_expanded_test_list


ipv4_expanded_test_list = sorted(expand_ip_list(IPV4_TEST_LIST, 4))
ipv6_expanded_test_list = sorted(expand_ip_list(IPV6_TEST_LIST, 6))

final_expanded_test_list = {
    "ipv4": ipv4_expanded_test_list,
    "ipv6": ipv6_expanded_test_list,
}

# Write the expanded list to a JSON file
with open("test.json", "w", encoding="utf-8") as json_file:
    json.dump(final_expanded_test_list, json_file, indent=4)  # Indent with 4 spaces
    json_file.write("\n")  # Add an empty line

print("Data has been written to test.json")
