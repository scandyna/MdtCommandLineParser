# Install MdtCommandLineParser

Get MdtCommandLineParser:
```bash
git clone git@gitlab.com:scandyna/mdtcommandlineparser.git
```

Create a build directory and cd to it:
```bash
mkdir build
cd build
```

## Requirements

Some tools and libraries are required to build MdtCommandLineParser:
 - Git
 - CMake
 - A compiler (Gcc or Clang or MSVC)
 - Make (optional)
 - Qt5

For a overview how to install them, see https://gitlab.com/scandyna/build-and-install-cpp

Some Mdt tools and libraries are also required:
 - [MdtCMakeConfig](https://gitlab.com/scandyna/mdtcmakeconfig)
 - [MdtCMakeModules](https://gitlab.com/scandyna/mdt-cmake-modules)

See the project repository for each of them to install those.

## Note about install prefix

Some note on the `CMAKE_INSTALL_PREFIX`:
 - To target a system wide installation on Linux, set it to `/usr` (`-DCMAKE_INSTALL_PREFIX=/usr`) .
 - For other locations, spcecify also the `<package-name>`, (for example `-DCMAKE_INSTALL_PREFIX=~/opt/MdtCommandLineParser`).

For details about that, see:
 - https://scandyna.gitlab.io/mdt-cmake-modules/Modules/MdtInstallDirs.html
 - https://cmake.org/cmake/help/latest/variable/CMAKE_INSTALL_PREFIX.html
 - https://scandyna.gitlab.io/mdt-cmake-modules/Modules/MdtInstallLibrary.html

## Configure MdtCommandLineParser

Configure MdtCommandLineParser:
```bash
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/some/path/MdtCommandLineParser -DCMAKE_PREFIX_PATH="/some/path/MdtCMakeConfig;/some/path/MdtCMakeModules;/some/path/qt/Qt5/5.15.2/gcc_64" ..
cmake-gui .
```

Choose different options, like the components to build.
Once done, run "Generate", then quit cmake-gui.

## Build and install MdtCommandLineParser

To build and install, run:
```cmd
cmake --build . --target INSTALL --config Release
```

Note that the `--config Release` is only mandatory
for multi configuration build systems, like MSVC.
