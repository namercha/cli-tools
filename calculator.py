import click

@click.command()
@click.argument('xs', type=int, nargs=-1)
@click.option('-v', '--verbose', help='Show additional output.', count=True)
def add(xs, verbose):
    """Adds a list of numbers."""
    if verbose > 1:
        steps = []
        results = 0
        for x in xs:
            steps.append(x)
            results += x
            click.echo(f"{' + '.join(str(x) for x in steps)} = {sum(steps)}")
    elif verbose == 1:
        click.echo(f"{' + '.join(str(x) for x in xs)} = {sum(xs)}")
    else:
        click.echo(sum(xs))


@click.command()
@click.argument('xs', type=int, nargs=-1)
@click.option('-v', '--verbose', help='Show additional output.', count=True)
def subtract(xs, verbose):
    """Subtracts a list of numbers."""
    if verbose > 1:
        z = xs[0]
        steps = [z]
        for x in xs[1:]:
            steps.append(x)
            z -= x
            click.echo(f"{' - '.join(str(s) for s in steps)} = {z}")
    else:
        results = xs[0]
        for x in xs[1:]:
            results -= x
        if verbose == 1:
            click.echo(f"{' - '.join(str(x) for x in xs)} = {results}")
        else:
            click.echo(results)
