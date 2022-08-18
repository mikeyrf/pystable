import os
import pathlib
import shutil

from distutils.command.build_ext import build_ext
from distutils.core import Distribution
from distutils.core import Extension


libstable_module = Extension('libstable',
                             libraries=["blas", "gsl", "m", "gslcblas"],
                             sources=[
                                "./libstable/stable/src/mcculloch.c",
                                "./libstable/stable/src/methods.c",
                                "./libstable/stable/src/stable_cdf.c",
                                "./libstable/stable/src/stable_common.c",
                                "./libstable/stable/src/stable_dist.c",
                                "./libstable/stable/src/stable_fit.c",
                                "./libstable/stable/src/stable_integration.c",
                                "./libstable/stable/src/stable_koutrouvelis.c",
                                "./libstable/stable/src/stable_pdf.c",
                                "./libstable/stable/src/stable_q.c",
                                "./libstable/stable/src/stable_rnd.c"])


# SEE: https://github.com/python-poetry/poetry/issues/11
# SEE: https://github.com/sdispater/pendulum/blob/master/build.py
class ExtensionBuild(build_ext):
    def run(self):
        build_ext.run(self)

        # Copy built extensions back to project
        self.check_extensions_list(self.extensions)
        for ext in self.extensions:
            output = self.get_ext_fullpath(ext.name)
            if not os.path.exists(output):
                continue

            relative_extension = os.path.relpath(output, self.build_lib)
            file_extension = pathlib.Path(relative_extension).suffix
            dest = os.path.join(
                "./pystable/_extensions",  # TODO: remove hard code
                ext.name+file_extension
            )
            shutil.copyfile(output, dest)
            mode = os.stat(dest).st_mode
            mode |= (mode & 0o444) >> 2
            os.chmod(dest, mode)


def build(setup_kwargs):
    """
    This function is mandatory in order to build the extensions.
    """
    distribution = Distribution(
        {"name": "pystable", "ext_modules": [libstable_module]})
    distribution.package_dir = "pystable"

    cmd = ExtensionBuild(distribution)
    cmd.ensure_finalized()
    cmd.run()

    return setup_kwargs


if __name__ == "__main__":
    build({})
