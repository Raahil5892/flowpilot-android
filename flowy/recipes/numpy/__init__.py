from pythonforandroid.recipes.numpy import NumpyRecipe as _UpstreamNumpyRecipe


class NumpyRecipe(_UpstreamNumpyRecipe):
    """Local override.

    Upstream builds numpy with `python -m build --wheel`, which spawns an
    isolated venv. On this toolchain that venv installs meson-python but then
    fails to import it:

        pyproject_hooks._impl.BackendUnavailable: Cannot import 'mesonpy'

    Disabling isolation makes the build use hostpython's already-installed
    meson-python / Cython instead.
    """

    extra_build_args = _UpstreamNumpyRecipe.extra_build_args + [
        "--no-isolation",
        "--skip-dependency-check",
    ]

    hostpython_prerequisites = _UpstreamNumpyRecipe.hostpython_prerequisites + [
        "meson-python>=0.15.0",
        "meson",
        "ninja",
        "wheel",
        "pyproject-metadata",
        "packaging",
    ]


recipe = NumpyRecipe()
