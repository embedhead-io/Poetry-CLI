import click
import subprocess
import os


def run_cmd(cmd):
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        click.echo(f"Command '{cmd}' failed with error: {str(e)}", err=True)


@click.command()
@click.option(
    "--project-name", prompt="Enter your project name", help="The name of the project"
)
@click.option(
    "--dependencies",
    prompt="Enter your dependencies, space separated",
    help="The dependencies of the project",
    default="",
)
@click.option("--create-env", is_flag=True, help="Whether or not to create a .env file")
@click.option(
    "--create-gitignore",
    is_flag=True,
    help="Whether or not to create a .gitignore file",
)
@click.option(
    "--create-main",
    is_flag=True,
    help="Whether or not to create a main.py file in the project directory",
)
@click.option(
    "--create-test",
    is_flag=True,
    help="Whether or not to create a test_main.py file in the tests directory",
)
def create_project(
    project_name, dependencies, create_env, create_gitignore, create_main, create_test
):
    """This is an interactive CLI for creating a new Poetry project"""
    click.echo(f"Creating a new Poetry project: {project_name}...")
    run_cmd(f"poetry new {project_name}")

    # Change into the project directory
    os.chdir(project_name)

    # Add dependencies
    if dependencies:
        click.echo(f"Adding necessary dependencies...")
        run_cmd(f"poetry add {dependencies}")

    # Create a .env file if requested
    if create_env:
        click.echo("Creating a .env file...")
        with open(".env", "w") as f:
            pass

    # Create a .gitignore file if requested
    if create_gitignore:
        click.echo("Creating a .gitignore file...")
        with open(".gitignore", "w") as f:
            pass

    # Create a main.py file if requested
    if create_main:
        click.echo("Creating a main.py file in the src directory...")
        with open(f"{project_name.replace('-', '_').lower()}/main.py", "w") as f:
            pass

    # Create a test_main.py file if requested
    if create_test:
        click.echo("Creating a test_main.py file in the tests directory...")
        with open("tests/test_main.py", "w") as f:
            pass

    # Inform the user
    click.echo(f"Project {project_name} has been successfully created!")


if __name__ == "__main__":
    create_project()
