#!/usr/bin/env python

import click

debug_print: bool = False


def info(message):
    click.echo(click.style(message, fg="green"))


def debug(message):
    if debug_print:
        click.echo(click.style(message, fg="yellow"))


def error(message):
    click.echo(click.style(message, fg="red"))
