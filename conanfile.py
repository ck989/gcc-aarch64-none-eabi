import os
from conan.tools.files import copy
from conan import ConanFile

class GCCAArch64NoneEabiRecipe(ConanFile):
    name = "gcc-aarch64-none-eabi"
    version = "14.2.1"
    package_type = "application"
    settings = "os", "arch"
    exports_sources = "gcc/*"

    def layout(self):
        self.folders.source = "."
        self.folders.build = "build"
        self.folders.generators = "build/generators"
        self.cpp.package.resdirs = []
        self.cpp.package.includedirs = []
        self.cpp.package.libdirs = []
        self.cpp.package.bindirs = ["bin"]

    def build(self):
        url = "https://github.com/ck989/gcc-aarch64-none-eabi.git"
        self.run(f"git clone --depth=1 {url} gcc")
        return
    
    def package(self):
        copy(self, pattern="*", dst=self.package_folder, src=os.path.join(self.source_folder, "gcc"))
        return
    
    def package_info(self):
        self.buildenv_info.append_path("PATH", os.path.join(self.package_folder, "bin"))
        return

