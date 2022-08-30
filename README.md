# MdtCommandLineParser

## Description

Library to help to create a command-line parser in a C++ application.

Key points:
* Parser based on a C++ definition
* Support for sub-command (1 level)
* Support for Bash TAB completion (generated from the definition)

C++ does not offer native command-line arguments parsing built-in.

A portable solution is to use [QCommandLineParser](https://doc.qt.io/qt-6/qcommandlineparser.html),
which does the job well, but has some missing features:
* No built-in support for the concept of sub-command
* Mixing the parser definition into the parser make the API a bit confusing
* No support for Bash TAB completion built-in

## Usage

A example of code is available in the [API documentaion](https://scandyna.gitlab.io/mdtcommandlineparser).

## CMake project description

Update your CMakeLists.txt to use the required libraries:
```cmake
cmake_minimum_required(VERSION 3.15)
project(MyApp)

find_package(Threads REQUIRED)
find_package(Qt5 REQUIRED COMPONENTS Core)
find_package(Mdt0 REQUIRED COMPONENTS CommandLineParser )

add_executable(myApp myApp.cpp)
target_link_libraries(myApp Mdt0::CommandLineParser)
```

## Project using Conan

If you use [Conan](https://conan.io/),
add MdtCommandLineParser as requirement in your `conanfile.txt`:
```conan
[requires]
MdtCommandLineParser/x.y.z@scandyna/testing

[generators]
CMakeDeps
CMakeToolchain
VirtualBuildEnv
```

Add the remote:
```bash
conan remote add gitlab https://gitlab.com/api/v4/projects/25668674/packages/conan
```

Install the dependencies:
```bash
mkdir build && cd build
conan install .. --profile your_profile -s build_type=Debug
```

If you don't use the native compiler,
and your Conan profile defines one
(or it defines some other environments),
bring the required environment to the current shell:
```bash
source conanbuild.sh
```
On Windows:
```bash
.\conanbuild.bat
```

Configure your project:
```bash
cmake -DCMAKE_TOOLCHAIN_FILE=conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Debug ..
```

Maybe adjust some settings:
```bash
cmake-gui .
```

Build:
```bash
cmake --build . --config Debug
```

To run the tests:
```bash
ctest --output-on-failure -C Debug
```

If applicable, restore the previous shell environment:
```bash
source deactivate_conanbuild.sh
```
On Windows:
```bash
.\deactivate_conanbuild.bat
```

For a list of available packages, and also some other details,
see [Conan packages README](packaging/conan/README.md).

## Manual install

It is also possible to install MdtCommandLineParser locally.
See [INSTALL](INSTALL.md).

Then, configure your project and specify
the path of the installed MdtCommandLineParser and the dependencies:
```bash
cmake -DCMAKE_PREFIX_PATH="/some/path/MdtCommandLineParser;/some/path/MdtCMakeConfig;/some/path/MdtCMakeModules;/some/path/qt/Qt5/5.15.2/gcc_64" ..
```

# Work on MdtCommandLineParser

## Build

See [BUILD](BUILD.md).

## Create Conan package

See [README](packaging/conan/README.md) in the conan packaging folder.

---

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!).  Thank you to [makeareadme.com](https://gitlab.com/-/experiment/new_project_readme_content:c2a8b3a5a9f4f6f4c812fa76506347b0?https://www.makeareadme.com/) for this template.

## Suggestions for a good README
Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.

