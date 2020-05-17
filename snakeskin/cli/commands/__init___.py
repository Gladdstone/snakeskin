from snakeskin import __version__
import pkg_resources
pkg_resources.declare_namespace(__name__)
pkg_resources.get_default_cache("snakeskin_cli").version