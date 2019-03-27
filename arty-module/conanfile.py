from conans import ConanFile, CMake, tools


class ArtyConan(ConanFile):
    name = "arty"
#    version = "0.1"
    license = "MIT"
    author = "yann chaysinh"
    url = "https://github.com/cyan21/conan-demo"
    description = "Artifactory wrapper"
    topics = ("Artifactory", "demo")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = "src/*"

    def source(self):
        self.run("git clone https://github.com/cyan21/conan-demo.git")
#        self.run("cd arty-module")

        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
#        tools.replace_in_file("src/CMakeLists.txt", "project(artifactory)",
#                              '''project(libart)
#include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
#conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

        # Explicit way:
        # self.run('cmake %s/hello %s'
        #          % (self.source_folder, cmake.command_line))
        # self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["artifactory"]

