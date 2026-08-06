from pythonforandroid.recipes.pyjnius import PyjniusRecipe as _Upstream


class PyjniusRecipe(_Upstream):
    """Local override: build isolation is broken on this toolchain.

    The isolated venv installs setuptools but then cannot import it:
        BackendUnavailable: Cannot import 'setuptools.build_meta'
    Same root cause as the numpy override.
    """

    extra_build_args = list(getattr(_Upstream, "extra_build_args", [])) + [
        "--no-isolation",
        "--skip-dependency-check",
    ]

    hostpython_prerequisites = list(
        getattr(_Upstream, "hostpython_prerequisites", [])
    ) + ["setuptools>=58.0.0", "wheel", "Cython~=3.1.2"]


recipe = PyjniusRecipe()
