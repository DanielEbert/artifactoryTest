from conans import ConanFile, CMake, tools


class Ci4ciConan(ConanFile):
    name = "ci4ci"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False], 'fuzzing': [True, False]}
    default_options = {"shared": False, "fPIC": True, 'fuzzing': False}
    generators = "cmake"

    def build_requirements(self):
        if self.options.fuzzing:
            self.build_requires('libafl/0.1@daniel/testing')

    def build(self):
        cmake = CMake(self)
        
        if self.options.fuzzing:
            cmake.definitions['CMAKE_CXX_COMPILER'] = self.deps_env_info['libafl'].FUZZER_LIBAFL_CXX_PATH

        cmake.configure()
        cmake.build()
