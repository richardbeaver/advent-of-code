From the Modular Install Guide at [https://docs.modular.com/max/packages]:

- "You can install all the Modular APIs and tools (including MAX and Mojo) as a
  single package called `modular`, using any Python or Conda package manager. On
  this page, we show how to install using pip, uv, conda, and pixi."

On the "Get Started with Mojo" page at
[https://docs.modular.com/mojo/manual/get-started/] (as of 05/30/2025):

- "...for Mojo developers, we currently recommend using pixi."

Commands used to create this directory as a Modular environment using `pixi`:

````
# Install pixi if not already installed
curl -fsSL https://pixi.sh/install.sh | sh

# Create project directory and `cd` into it
pixi init <project-name> \
  -c https://conda.modular.com/max-nightly/ -c conda-forge \
  && cd <project-name>```

# Install `modular` conda package
pixi add modular

# Start virtual environment
pixi shell

# Run `mojo` commands with:
pixi run mojo <...>
# Or just:
mojo <...>

# To deactivate virtual environment:
exit
````
