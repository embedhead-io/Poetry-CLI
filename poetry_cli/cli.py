import click
import subprocess
import os


@click.command()
@click.option(
    "--project-name", prompt="Enter your project name", help="The name of the project"
)
@click.option(
    "--dependencies",
    prompt="Enter your dependencies, space separated",
    help="The dependencies of the project",
)
@click.option(
    "--create-env",
    prompt="Would you like to create a .env file?",
    help="Whether or not to create a .env file",
    type=click.Choice(["yes", "no"], case_sensitive=False),
    default="no",
)
@click.option(
    "--create-gitignore",
    prompt="Would you like to create a .gitignore file?",
    help="Whether or not to create a .gitignore file",
    type=click.Choice(["yes", "no"], case_sensitive=False),
    default="no",
)
@click.option(
    "--create-main",
    prompt="Would you like to create a main.py file in the project directory?",
    help="Whether or not to create a main.py file in the project directory",
    type=click.Choice(["yes", "no"], case_sensitive=False),
    default="no",
)
@click.option(
    "--create-test",
    prompt="Would you like to create a test_main.py file in the tests directory?",
    help="Whether or not to create a test_main.py file in the tests directory",
    type=click.Choice(["yes", "no"], case_sensitive=False),
    default="no",
)
def create_project(
    project_name,
    dependencies,
    create_env,
    create_gitignore,
    create_main,
    create_test,
):
    """This is an interactive CLI for creating a new Poetry project"""

    # Initialize the Poetry project
    click.echo(f"Creating a new Poetry project: {project_name}...")
    subprocess.run(f"poetry new {project_name}", shell=True, check=True)

    # Change into the project directory
    os.chdir(project_name)

    # Add dependencies
    if dependencies:
        click.echo(f"Adding necessary dependencies...")
        subprocess.run(f"poetry add {dependencies}", shell=True, check=True)

    # Create a .env file if requested
    if create_env.lower() == "yes":
        click.echo("Creating a .env file...")
        with open(".env", "w") as f:
            pass

    # Create a .gitignore file if requested
    if create_gitignore.lower() == "yes":
        click.echo("Creating a .gitignore file...")
        with open(".gitignore", "w") as f:
            pass

    # Create a main.py file if requested
    if create_main.lower() == "yes":
        click.echo("Creating a main.py file in the src directory...")
        with open(f"{project_name.replace('-', '_').lower()}/main.py", "w") as f:
            pass

    # Create a test_main.py file if requested
    if create_test.lower() == "yes":
        click.echo("Creating a test_main.py file in the tests directory...")
        with open("tests/test_main.py", "w") as f:
            pass

    # Inform the user
    click.echo(f"Project {project_name} has been successfully created!")


if __name__ == "__main__":
    create_project()
