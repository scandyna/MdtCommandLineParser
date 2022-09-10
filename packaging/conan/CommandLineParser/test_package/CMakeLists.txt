# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.15)

project(MdtCommandLineParser_Test LANGUAGES CXX)

find_package(MdtCMakeModules REQUIRED)

include(MdtAddTest)

enable_testing()

find_package(Qt5 COMPONENTS Core REQUIRED)
find_package(Boost REQUIRED)
find_package(Mdt0 COMPONENTS CommandLineParser REQUIRED)

mdt_add_test(
  NAME CommandLineParser_Test
  TARGET commandLineParser_Test
  DEPENDENCIES Mdt0::CommandLineParser Qt5::Core
  SOURCE_FILES
    main.cpp
)
