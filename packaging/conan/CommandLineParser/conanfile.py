from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake
from conan.errors import ConanInvalidConfiguration
# The new class Git seems not to provide similar method like get_tag()
#from conan.tools.scm import Git
from conans import tools
import os

class MdtCommandLineParserConan(ConanFile):
  name = "MdtCommandLineParser"
  license = "BSD 3-Clause"
  url = "https://gitlab.com/scandyna/mdtcommandlineparser"
  description = "Library to help to create a command-line parser in a C++ application"
  settings = "os", "compiler", "build_type", "arch"
  options = {"shared": [True, False]}
  default_options = {"shared": True}
  generators = "CMakeDeps", "VirtualBuildEnv"
  # If no_copy_source is False, conan copies sources to build directory and does in-source build,
  # resulting having build files installed in the package
  # See also: https://github.com/conan-io/conan/issues/350
  no_copy_source = True

  # See: https://docs.conan.io/en/latest/reference/conanfile/attributes.html#short-paths
  short_paths = True

  # The version can be set on the command line:
  # conan create . x.y.z@scandyna/testing ...
  # It can also be set by a git tag (case of deploy in the CI/CD)
  def set_version(self):
    if not self.version:
      if os.path.exists(".git"):
        git = tools.Git()
        self.version = "%s" % (git.get_tag())
    if self.version == "None":
      msg = ("{}: no version provided. "
             "Either give a version at the conan create command, "
             "or call conan create from the root of the repository with a git tag set").format(self.name)
      raise ConanInvalidConfiguration(msg)
    self.output.info( "%s: version is %s" % (self.name, self.version) )


  def requirements(self):
    self.requires("MdtCMakeConfig/0.0.5@scandyna/testing")
    self.requires("qt/5.15.6")
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
    self.tool_requires("MdtCMakeModules/0.18.3@scandyna/testing", force_host_context=True)


  # The export exports_sources attributes does not work if the conanfile.py is in a sub-folder.
  # See https://github.com/conan-io/conan/issues/3635
  # and https://github.com/conan-io/conan/pull/2676
  def export_sources(self):
    self.copy("CMakeLists.txt", src="../../../", dst=".")
    self.copy("COPYING", src="../../../", dst=".")
    self.copy("COPYING.LESSER", src="../../../", dst=".")
    self.copy("libs/CommandLineParser/*", src="../../../", dst=".")

  def generate(self):
    tc = CMakeToolchain(self)
    #tc.variables["INSTALL_CONAN_PACKAGE_FILES"] = "ON"
    tc.generate()

  def build(self):
    cmake = CMake(self)
    cmake.configure()
    cmake.build()

  def package(self):
    cmake = CMake(self)
    cmake.install()

  # Use the default package_id()
  # https://docs.conan.io/en/latest/creating_packages/define_abi_compatibility.html#define-abi-compatibility

  def package_info(self):
    self.cpp_info.set_property("cmake_file_name", "Mdt0CommandLineParser")
    self.cpp_info.set_property("cmake_target_name", "Mdt0::CommandLineParser")
    self.cpp_info.libs = ["Mdt0CommandLineParser"]
