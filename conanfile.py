from conans import ConanFile, tools
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake
import os

# This recipe is only to install dependencies to build MdtCommandLineParser
# The recipes to create packages are in packaging/conan/ subfolder
class MdtCommandLineParserConan(ConanFile):
  name = "MdtCommandLineParser"
  license = "BSD 3-Clause"
  url = "https://gitlab.com/scandyna/mdtcommandlineparser"
  description = "Library to help to create a command-line parser in a C++ application."
  settings = "os", "compiler", "build_type", "arch"
  options = {"shared": [True, False]}
  default_options = {"shared": True}
  generators = "CMakeDeps", "CMakeToolchain", "VirtualBuildEnv"

  # If no_copy_source is False, conan copies sources to build directory and does in-source build,
  # resulting having build files installed in the package
  # See also: https://github.com/conan-io/conan/issues/350
  no_copy_source = True

  def requirements(self):
    self.requires("qt/5.15.2")
    self.requires("boost/1.72.0")
    self.requires("MdtCommandLineArguments/0.4.1@scandyna/testing")


  # When using --profile:build xx and --profile:host xx ,
  # the dependencies declared in build_requires and tool_requires
  # will not generate the required files.
  # see:
  # - https://github.com/conan-io/conan/issues/10272
  # - https://github.com/conan-io/conan/issues/9951
  def build_requirements(self):
    # TODO fix once issue solved
    # Due to a issue using GitLab Conan repository,
    # version ranges are not possible.
    # See https://gitlab.com/gitlab-org/gitlab/-/issues/333638
    self.tool_requires("catch2/2.13.9", force_host_context=True)
    self.tool_requires("MdtCMakeModules/0.19.0@scandyna/testing", force_host_context=True)
