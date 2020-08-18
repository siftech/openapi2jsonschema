#!/usr/bin/env python

import json
import re
from copy import deepcopy
from typing import Any, Dict, Optional

import yaml
import urllib
import os
import sys

from jsonref import JsonRef  # type: ignore
import click

from openapi2jsonschema.log import info, error, debug_print
from openapi2jsonschema.log import debug as dbg
from openapi2jsonschema.util import (
    additional_properties,
    replace_int_or_string,
    allow_null_optional_fields,
    change_dict_values,
    append_no_duplicates,
)
from openapi2jsonschema.errors import UnsupportedError
import openapi2jsonschema.translator as translator


@click.command()
@click.option(
    "-o",
    "--output",
    default="schemas",
    metavar="PATH",
    help="Directory to store schema files",
)
@click.option(
    "-p",
    "--prefix",
    default="_definitions.json",
    help="Prefix for JSON references (only for OpenAPI versions before 3.0)",
)
@click.option(
    "-r",
    "--root",
    default=None,
    help="Root class to generate schema for.  Will generate a standalone JSON schema file for this class.",
)
@click.option(
    "--stand-alone", is_flag=True, help="Whether or not to de-reference JSON schemas"
)
@click.option(
    "--expanded", is_flag=True, help="Expand Kubernetes schemas by API version"
)
@click.option(
    "--kubernetes", is_flag=True, help="Enable Kubernetes specific processors"
)
@click.option(
    "--strict",
    is_flag=True,
    help="Prohibits properties not in the schema (additionalProperties: false)",
)
@click.argument("schema", metavar="SCHEMA_URL")
@click.option(
    "-d", "-v",
    "--debug", is_flag=True, default=False, help="Enable debug output."
)

def default(output, schema, prefix, stand_alone, expanded, kubernetes, strict, root: Optional[str], debug: bool):
    translator.translate(output, schema, prefix, stand_alone, expanded, kubernetes, strict, root, debug)

if __name__ == "__main__":
    default()
