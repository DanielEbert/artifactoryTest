from conans import ConanFile, CMake, tools
import os

class LibaflConan(ConanFile):
    name = "libafl"
    version = "0.1"

    def package(self):
        self.copy("libafl_cc", dst="bin", src="bin")
        self.copy("libafl_cxx", dst="bin", src="bin")
        self.copy("libfuzzbench.a", dst="bin", src="bin")

    def package_info(self):
        self.output.info(f'libafl_cc path: {os.path.join(self.package_folder, "bin/libafl_cc")}')
        self.output.info(f'libafl_cxx path: {os.path.join(self.package_folder, "bin/libafl_cxx")}')
        self.output.info(f'libfuzzbench.a path: {os.path.join(self.package_folder, "bin/libfuzzbench.a")}')
        self.env_info.FUZZER_LIBAFL_CC_PATH = os.path.join(self.package_folder, 'bin/libafl_cc')
        self.env_info.FUZZER_LIBAFL_CXX_PATH = os.path.join(self.package_folder, 'bin/libafl_cxx')
        self.env_info.FUZZER_LIBFUZZBENCH_PATH = os.path.join(self.package_folder, 'bin/libfuzzbench.a')

