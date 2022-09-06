# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.15)

# CMAKE_PREFIX_PATH is empty before any call to project()
# Because set_project_version() does not exist,
# we call the project command twice (is there a cleaner solution?)
project(MdtCommandLineParser)

#######################################################
# Project definition with versionning got from git tag
#######################################################

find_package(Git REQUIRED)
find_package(MdtCMakeModules REQUIRED)

include(MdtVersionUtils)

set(INITIAL_PROJECT_VERSION)
if(FROM_CONAN_PROJECT_VERSION)
  set(INITIAL_PROJECT_VERSION ${FROM_CONAN_PROJECT_VERSION})
else()
  mdt_cmake_project_version_from_git_tag(INITIAL_PROJECT_VERSION DEFAULT_VERSION 0.0.0)
endif()

project(MdtCommandLineParser VERSION ${INITIAL_PROJECT_VERSION} LANGUAGES CXX)

unset(INITIAL_PROJECT_VERSION)

#######################
# Options
#######################

include(MdtBuildOptionsUtils)
include(MdtSanitizers)

set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN YES)

option(BUILD_TESTS "Build the tests" OFF)
option(BUILD_BENCHMARKS "Build the benchmarks" OFF)
option(BUILD_DOCS "Build the documentations" OFF)
mdt_set_available_build_types(Release Debug RelWithDebInfo MinSizeRel Instrumented)
option(WARNING_AS_ERROR "Treat warnings as errors" OFF)
option(BUILD_SHARED_LIBS "Build shared libraries" ON)

option(BUILD_USE_IPO_LTO_IF_AVAILABLE "Use link-time optimization if available on the platform" OFF)
mark_as_advanced(BUILD_USE_IPO_LTO_IF_AVAILABLE)
# Provide LPO/LTO option if supported
# Note: CMake before 3.9 does only support Intel compiler on Linux.
#       Check documentation of the CheckIPOSupported module,
#       and also CMP0069 policy.
include(CheckIPOSupported)
check_ipo_supported(RESULT HAVE_IPO_LTO)
if(HAVE_IPO_LTO)
  option(BUILD_USE_IPO_LTO "Use link-time optimization" ${BUILD_USE_IPO_LTO_IF_AVAILABLE})
endif()

mdt_add_address_sanitizer_option_if_available(SANITIZER_ENABLE_ADDRESS
  HELP_STRING "Enable address sanitizer"
  INITIAL_VALUE OFF
)
mdt_add_memory_sanitizer_option_if_available(SANITIZER_ENABLE_MEMORY
  HELP_STRING "Enable memory sanitizer"
  INITIAL_VALUE OFF
)
mdt_add_undefined_sanitizer_option_if_available(SANITIZER_ENABLE_UNDEFINED
  HELP_STRING "Enable undefined behaviour sanitizer"
  INITIAL_VALUE OFF
)
mdt_add_thread_sanitizer_option_if_available(SANITIZER_ENABLE_THREAD
  HELP_STRING "Enable thread sanitizer (can be incompatible with other sanitizers)"
  INITIAL_VALUE OFF
)

#######################
# Warnings
#######################

if(MSVC)
  add_compile_options(/W3)
  if(WARNING_AS_ERROR)
    add_compile_options(/WX)
  endif()
  # C4996: 'strcpy': This function or variable may be unsafe. Consider using strcpy_s instead (which not works with gcc/clang)
#   add_compile_options(/wd4996)
else()
  add_compile_options(-Wall -Wextra -Wpedantic -Wconversion -Wunused)
  if(WARNING_AS_ERROR)
    add_compile_options(-Werror)
  endif()
endif()

#######################
# Dependencies
#######################

# find_package(Threads REQUIRED)
find_package(Qt5 COMPONENTS Core REQUIRED)
find_package(Mdt0 COMPONENTS CommandLineArguments REQUIRED)

# CommandLineParser uses Boost optional
# For header only library,no component is defined.
# https://cmake.org/pipermail/cmake/2013-September/055941.html
find_package(Boost REQUIRED)


if(BUILD_TESTS)
  find_package(Catch2 REQUIRED)
  find_package(Qt5 COMPONENTS Test Gui REQUIRED)
endif()

if(BUILD_BENCHMARKS)
  find_package(Qt5 COMPONENTS Test REQUIRED)
endif()

if(BUILD_DOCS)
  include(FindDoxygen)
  find_package(Doxygen REQUIRED dot)
endif()

#######################
# Sanitizers
#######################

if(SANITIZER_ENABLE_ADDRESS)
  mdt_build_with_address_sanitizer()
endif()
if(SANITIZER_ENABLE_MEMORY)
  mdt_build_with_memory_sanitizer()
endif()
if(SANITIZER_ENABLE_UNDEFINED)
  mdt_build_with_undefined_sanitizer()
endif()
if(SANITIZER_ENABLE_THREAD)
  mdt_build_with_thread_sanitizer()
endif()

#######################
# Install
#######################

set(MDT_INSTALL_PACKAGE_NAME Mdt${PROJECT_VERSION_MAJOR})
include(GNUInstallDirs)
include(MdtInstallDirs)

#######################
# Qt
#######################

add_definitions(-DQT_NO_CAST_DEFINITIONS -DQT_NO_CAST_FROM_ASCII -DQT_NO_CAST_TO_ASCII -DQT_NO_CAST_FROM_BYTEARRAY)

set(CMAKE_AUTOMOC ON)

######################
# Tests and benchmarks
######################

if(BUILD_TESTS OR BUILD_BENCHMARKS)
  add_library(Mdt_Catch2Qt STATIC Catch2QString.cpp)
  target_include_directories(Mdt_Catch2Qt
    PUBLIC
      $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
      $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}>
  )
  target_link_libraries(Mdt_Catch2Qt PUBLIC Qt5::Core)
  add_library(Mdt::Catch2Qt ALIAS Mdt_Catch2Qt)

  add_library(Mdt_Catch2Main STATIC Catch2Main.cpp)
  target_link_libraries(Mdt_Catch2Main PUBLIC Catch2::Catch2)
  add_library(Mdt::Catch2Main ALIAS Mdt_Catch2Main)

  enable_testing()
endif()

if(BUILD_BENCHMARKS)
  target_compile_definitions(Mdt_Catch2Main
    PUBLIC
      CATCH_CONFIG_ENABLE_BENCHMARKING
  )
endif()

#######################
# Sources
#######################

add_subdirectory(libs/CommandLineParser)

if(BUILD_DOCS)
  add_subdirectory(doc)
endif()
