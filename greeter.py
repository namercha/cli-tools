import click

@click.command()
@click.argument('name')
@click.option('--lang',
              help='Specify a language English (en) or Spanish (es)',
              default='en',
              type=click.Choice(['es', 'en']))
def greet(name, lang):
    """Displays a greeting to the user."""
    greeting = 'Hello' if lang =='en' else 'Hola'
    click.echo(f"{greeting}! {name}")
