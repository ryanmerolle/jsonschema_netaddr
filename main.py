#!/usr/bin/env python3
import json

import netaddr
from jsonschema import Draft7Validator, FormatChecker, exceptions
from rich import print as rprint


def get_ip_object(instance):
    if "/" in instance:  # Check if instance has CIDR notation
        return netaddr.IPNetwork(instance)
    else:
        return netaddr.IPAddress(instance)


# Define the custom validators
def validate_ipv4_address(validator, ipv4, instance, schema):
    if "/" in instance:  # Check if instance has CIDR notation
        yield exceptions.ValidationError(
            f"{instance} is [red]NOT[/red] a plain IPv4 address."
        )
        return  # Exit the function early
    try:
        netaddr.IPAddress(instance, version=4)
        if "ipv4WithPrefix" in schema and schema["ipv4WithPrefix"]:
            raise exceptions.ValidationError(
                f"{instance} should [red]NOT[/red] be a plain IPv4 address when prefix length is expected."
            )
    except netaddr.AddrFormatError:
        yield exceptions.ValidationError(
            f"{instance} is [red]NOT[/red] a valid IPv4 address."
        )


def validate_ipv4_network(validator, ipv4_network, instance, schema):
    try:
        net = netaddr.IPNetwork(instance, version=4)
        if net.ip != net.network:
            raise exceptions.ValidationError(
                f"{instance} is [red]NOT[/red] a valid IPv4 network address."
            )
    except netaddr.AddrFormatError:
        yield exceptions.ValidationError(
            f"{instance} is [red]NOT[/red] a valid IPv4 network address."
        )


def validate_multicast(validator, multicast, instance, schema):
    ip = get_ip_object(instance)
    if not ip.is_multicast():
        yield exceptions.ValidationError(
            f"{instance} is [red]NOT[/red] a multicast address."
        )


def validate_public(validator, public, instance, schema):
    ip = get_ip_object(instance)
    if not ip.is_unicast() or ip.is_private():
        yield exceptions.ValidationError(
            f"{instance} is [red]NOT[/red] a public address."
        )


def validate_private(validator, private, instance, schema):
    ip = get_ip_object(instance)
    if not ip.is_private():
        yield exceptions.ValidationError(
            f"{instance} is [red]NOT[/red] a private address."
        )


def validate_ipv4_with_prefix(validator, ipv4_with_prefix, instance, schema):
    if "/" not in instance:  # Check if CIDR notation is missing
        yield exceptions.ValidationError(
            f"{instance} is a plain IPv4 address. An IPv4 address with prefix length was expected."
        )
        return  # Exit the function early

    try:
        netaddr.IPNetwork(instance, version=4)
    except netaddr.AddrFormatError:
        yield exceptions.ValidationError(
            f"{instance} is [red]NOT[/red] a valid IPv4 address with prefix length."
        )


# Add the custom validators to the meta-schema
Draft7Validator.VALIDATORS.update(
    {
        "ipv4": validate_ipv4_address,
        "ipv4Network": validate_ipv4_network,
        "multicast": validate_multicast,
        "public": validate_public,
        "private": validate_private,
        "ipv4WithPrefix": validate_ipv4_with_prefix,
    }
)

with open("test_schema.json", "r", encoding="utf-8") as f:
    schema = json.load(f)

validator = Draft7Validator(schema, format_checker=FormatChecker())

# Load the JSON file containing the expanded list
with open("test_data.json", "r", encoding="utf-8") as f:
    examples = json.load(f)

output = []


def get_parent_key(path):
    """Return the parent key based on the error path."""
    if len(path) < 2:
        return None
    return path[-2]


def mark_failed_paths(error, failed_items):
    path = list(error.absolute_path)
    for i in range(len(path)):
        failed_items.add(tuple(path[: i + 1]))


def check_and_print(item, path, failed_items):
    """Recursively check if any part of the path failed and print results."""
    if isinstance(item, dict):
        for key, value in item.items():
            new_path = path + [key]
            check_and_print(value, new_path, failed_items)
    elif isinstance(item, list):
        for idx, value in enumerate(item):
            new_path = path + [idx]
            check_and_print(value, new_path, failed_items)
    else:
        if tuple(path) in failed_items:
            # This means one of the validations failed, so we won't print success for this path
            return
        output.append(f"{path[0]} - {item} - [green]Validated successfully[/green]")


# 1. Collect paths that failed validation
failed_items = set()
for error in validator.iter_errors(examples):
    parent_key = get_parent_key(list(error.absolute_path))
    output.append(f"{parent_key} - {error.message}")
    # Mark all paths that had a failure
    mark_failed_paths(error, failed_items)

# 2. Recursively validate all keys/indexes in examples
check_and_print(examples, [], failed_items)

# 3. Print the results
for line in sorted(output):
    if "Validated successfully" in line:
        rprint(f":white_heavy_check_mark:{line}")
    else:
        rprint(f":cross_mark:{line}")
