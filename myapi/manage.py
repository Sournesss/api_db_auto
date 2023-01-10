import click
from flask.cli import with_appcontext
import random

@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from myapi.extensions import db
    from myapi.models import User,FilterCar

    click.echo("create user")
    user = User(id=random.randint(1,9999))
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")
