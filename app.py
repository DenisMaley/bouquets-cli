import click

from src.controller import Controller


@click.command()
@click.option(
    '--input_file',
    type=click.File('r'),
    help='File in which there is the set of designs and the sequence of the details.'
         'If not provided, a prompt will allow you to type the input text.',
)
@click.option(
    '--output_file',
    type=click.File('w'),
    help='File in which the ready sets will be written.'
         'If not provided, the output text will just be printed.',
)
@click.option(
    '--capacity',
    type=int,
    help='Storage capacity',
)
def main(input_file, output_file, capacity):
    if input_file:
        input = input_file.read()
    else:
        input = click.prompt('Enter an input stream', type=str)

    controller = Controller(capacity)
    result = controller.run(input.replace('\\n', '\n'))

    if output_file:
        output_file.write(result)
    else:
        click.echo(result)


if __name__ == '__main__':
    main()
