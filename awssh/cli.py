# -*- coding: utf-8 -*-

"""Console script for awssh."""

import click
import awssh

@click.group()
def main(args=None):
    """Console script for awssh."""
    click.echo("Replace this message by putting your code into "
               "awssh.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


@main.command()
def testing():
    an = awssh.CliHelper.ask("Testing")
    click.echo('Answer: {0}'.format(an))

if __name__ == "__main__":
    main()
