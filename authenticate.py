import click

# Method 1:
# @click.command()
# @click.option('--username', prompt=True)
# @click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
# def auth(username, password):
#     """Provides user authentication."""
#     click.echo(f'Logging in {username}')

# Method 2
@click.command()
def auth():
    """Provides user authentication."""
    username = click.prompt('username')
    password = click.prompt('password', hide_input=True, confirmation_prompt=True)

    if click.confirm('Are you an Admin?'):
        admin_id = click.prompt('Admin ID', type=int, prompt_suffix='>')
        click.echo(f'Logging in admin {username} ID = {admin_id}')
    else:
        click.echo(f'Logging in {username}')
