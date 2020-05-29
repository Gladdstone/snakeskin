from snakeskin import __version__
import pkg_resources
pkg_resources.declare_namespace(__name__)
version = pkg_resources.require("snakeskin_cli")[0].version
