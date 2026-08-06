from os.path import dirname

import pythonforandroid.recipes.android as _upstream_module
from pythonforandroid.recipes.android import AndroidRecipe as _UpstreamAndroidRecipe


class AndroidRecipe(_UpstreamAndroidRecipe):
    """Local override of p4a's `android` recipe.

    Two things going on:

    1. Build isolation is broken on this toolchain - the isolated venv
       installs setuptools but then cannot import it:
           BackendUnavailable: Cannot import 'setuptools.build_meta'
       So we build with --no-isolation, using hostpython's packages.

    2. This recipe uses IncludedFilesBehaviour, which copies `src/` from
       the *recipe directory*. Because this local recipe shadows the
       upstream one, get_recipe_dir() would point here (no src/). We
       redirect it back to the upstream recipe directory so the bundled
       sources are still found.
    """

    extra_build_args = list(
        getattr(_UpstreamAndroidRecipe, "extra_build_args", [])
    ) + ["--no-isolation", "--skip-dependency-check"]

    hostpython_prerequisites = list(
        getattr(_UpstreamAndroidRecipe, "hostpython_prerequisites", [])
    ) + ["setuptools>=40.8.0", "wheel"]

    def get_recipe_dir(self):
        return dirname(_upstream_module.__file__)


recipe = AndroidRecipe()
