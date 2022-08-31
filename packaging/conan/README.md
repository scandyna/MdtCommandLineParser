[[_TOC_]]

# Create Conan packages for MdtCommandLineParser

The package version is picked up from git tag.
If working on MdtCommandLineParser, go to the root of the source tree:
```bash
git tag x.y.z
conan create packaging/conan/CommandLineParser scandyna/testing --profile:build $CONAN_PROFILE_BUILD --profile:host $CONAN_PROFILE_HOST -s build_type=$BUILD_TYPE
```

To create a package without having a git tag:
```bash
conan create packaging/conan/CommandLineParser x.y.z@scandyna/testing --profile:build $CONAN_PROFILE_BUILD --profile:host $CONAN_PROFILE_HOST -s build_type=$BUILD_TYPE
```

