from pathlib import Path
from datetime import datetime
import click

NOTES_DB = Path.home() / "code" / "cli-tools" / ".notes" / "notes.txt"
DISPLAY_FORMAT = "{:<3} {:16} {:16} {:40}"

def load_notes():
    notes = []
    with open(NOTES_DB) as fo:
        for line in fo:
            notes.append(line.strip())
    return notes


def print_note(index, note):
    created, updated, contents = note.split("\t")
    date_format = "%b-%d %I:%M %p"
    created = datetime.fromisoformat(created).strftime(date_format)
    updated = datetime.fromisoformat(updated).strftime(date_format)
    click.echo(DISPLAY_FORMAT.format(index, created, updated, contents))


def print_header():
    click.echo(DISPLAY_FORMAT.format("ID", "Created", "Updated", "Contents"))
    click.echo(DISPLAY_FORMAT.format("-"*3, "-"*16, "-"*16, "-"*40))


def save_notes(notes):
    with open(NOTES_DB, 'w')as fo:
        for note in notes:
            fo.write(f"{note}\n")
    return notes


@click.group()
@click.pass_context
def main(ctx):
    """Program for managing notes."""
    if not NOTES_DB.parent.exists():
        NOTES_DB.parent.mkdir()
        NOTES_DB.touch()

    ctx.ensure_object(dict)
    ctx.obj["notes"] = load_notes()


@main.command()
@click.pass_context
def show(ctx):
    """Shows notes in notes database."""

    notes = ctx.obj["notes"]

    print_header()
    for i, note in enumerate(notes, start=1):
        print_note(i, note)


@main.command()
@click.pass_context
def add(ctx):
    """Adds note to notes database."""

    notes = ctx.obj["notes"]


    created = datetime.now().isoformat()
    contents = click.prompt('Note context')
    notes.append(f"{created}\t{created}\t{contents}")
    save_notes(notes)


@main.command()
@click.pass_context
def update(ctx):
    """Updates note in notes database."""

    notes = ctx.obj["notes"]


    print_header()
    for i, note in enumerate(notes, start=1):
        print_note(i, note)
    
    index = click.prompt("Index of note to update or -1 to exit: ", type=int)
    if index == -1:
        return
    
    updated_content = click.prompt('Updated content >')
    index -= 1

    updated = datetime.now().isoformat()
    created = notes[index].split('\t')[0]

    notes[index] = f"{created}\t{updated}\t{updated_content}"

    save_notes(notes)


@main.command()
@click.pass_context
def delete(ctx):
    """Deletes note in notes database."""
    print_header()
    notes = ctx.obj["notes"]
    
    for i, note in enumerate(notes, start=1):
        print_note(i, note)
    
    index = click.prompt("Index of note to delete or -1 to exit: ", type=int)
    
    if index == -1:
        return
    
    index -= 1
    notes.remove(notes[index])
    save_notes(notes)
