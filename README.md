# jsonschema_netaddr

Experimenting with extending jsonschema to support netaddr objects.

## Getting Started

launch the devcontainer in VS Code

```bash
$./main.py
✅ipv4_addresses - 10.0.0.1 - Validated successfully
❌ipv4_addresses - 10.0.0.1/32 is NOT a plain IPv4 address.
❌ipv4_addresses - 100::1 is NOT a valid IPv4 address.
❌ipv4_addresses - 100::1/128 is NOT a plain IPv4 address.
✅ipv4_addresses - 8.8.8.8 - Validated successfully
❌ipv4_addresses_wplen - 10.0.0.1 is a plain IPv4 address. An IPv4 address with prefix length was expected.
✅ipv4_addresses_wplen - 10.0.0.1/32 - Validated successfully
❌ipv4_addresses_wplen - 100::1 is a plain IPv4 address. An IPv4 address with prefix length was expected.
❌ipv4_addresses_wplen - 100::1/128 is NOT a valid IPv4 address with prefix length.
❌ipv4_addresses_wplen - 8.8.8.8 is a plain IPv4 address. An IPv4 address with prefix length was expected.
❌ipv4_multicast_addresses - 10.0.0.1 is NOT a multicast address.
❌ipv4_multicast_addresses - 10.0.0.1/32 is NOT a multicast address.
❌ipv4_multicast_addresses - 10.0.0.1/32 is NOT a plain IPv4 address.
❌ipv4_multicast_addresses - 100::1 is NOT a multicast address.
❌ipv4_multicast_addresses - 100::1 is NOT a valid IPv4 address.
❌ipv4_multicast_addresses - 100::1/128 is NOT a multicast address.
❌ipv4_multicast_addresses - 100::1/128 is NOT a plain IPv4 address.
❌ipv4_multicast_addresses - 8.8.8.8 is NOT a multicast address.
❌ipv4_multicast_addresses_wplen - 10.0.0.1 is NOT a multicast address.
❌ipv4_multicast_addresses_wplen - 10.0.0.1 is a plain IPv4 address. An IPv4 address with prefix length was expected.
❌ipv4_multicast_addresses_wplen - 10.0.0.1/32 is NOT a multicast address.
❌ipv4_multicast_addresses_wplen - 100::1 is NOT a multicast address.
❌ipv4_multicast_addresses_wplen - 100::1 is a plain IPv4 address. An IPv4 address with prefix length was expected.
❌ipv4_multicast_addresses_wplen - 100::1/128 is NOT a multicast address.
❌ipv4_multicast_addresses_wplen - 100::1/128 is NOT a valid IPv4 address with prefix length.
❌ipv4_multicast_addresses_wplen - 8.8.8.8 is NOT a multicast address.
❌ipv4_multicast_addresses_wplen - 8.8.8.8 is a plain IPv4 address. An IPv4 address with prefix length was expected.
✅ipv4_private_addresses - 10.0.0.1 - Validated successfully
❌ipv4_private_addresses - 10.0.0.1/32 is NOT a plain IPv4 address.
❌ipv4_private_addresses - 100::1 is NOT a private address.
❌ipv4_private_addresses - 100::1 is NOT a valid IPv4 address.
❌ipv4_private_addresses - 100::1/128 is NOT a plain IPv4 address.
❌ipv4_private_addresses - 100::1/128 is NOT a private address.
❌ipv4_private_addresses - 8.8.8.8 is NOT a private address.
❌ipv4_private_addresses_wplen - 10.0.0.1 is a plain IPv4 address. An IPv4 address with prefix length was expected.
✅ipv4_private_addresses_wplen - 10.0.0.1/32 - Validated successfully
❌ipv4_private_addresses_wplen - 100::1 is NOT a private address.
❌ipv4_private_addresses_wplen - 100::1 is a plain IPv4 address. An IPv4 address with prefix length was expected.
❌ipv4_private_addresses_wplen - 100::1/128 is NOT a private address.
❌ipv4_private_addresses_wplen - 100::1/128 is NOT a valid IPv4 address with prefix length.
❌ipv4_private_addresses_wplen - 8.8.8.8 is NOT a private address.
❌ipv4_private_addresses_wplen - 8.8.8.8 is a plain IPv4 address. An IPv4 address with prefix length was expected.
❌ipv4_public_addresses - 10.0.0.1 is NOT a public address.
❌ipv4_public_addresses - 10.0.0.1/32 is NOT a plain IPv4 address.
❌ipv4_public_addresses - 10.0.0.1/32 is NOT a public address.
❌ipv4_public_addresses - 100::1 is NOT a valid IPv4 address.
❌ipv4_public_addresses - 100::1/128 is NOT a plain IPv4 address.
✅ipv4_public_addresses - 8.8.8.8 - Validated successfully
❌ipv4_public_addresses_wplen - 10.0.0.1 is NOT a public address.
❌ipv4_public_addresses_wplen - 10.0.0.1 is a plain IPv4 address. An IPv4 address with prefix length was expected.
❌ipv4_public_addresses_wplen - 10.0.0.1/32 is NOT a public address.
❌ipv4_public_addresses_wplen - 100::1 is a plain IPv4 address. An IPv4 address with prefix length was expected.
❌ipv4_public_addresses_wplen - 100::1/128 is NOT a valid IPv4 address with prefix length.
❌ipv4_public_addresses_wplen - 8.8.8.8 is a plain IPv4 address. An IPv4 address with prefix length was expected.
```
