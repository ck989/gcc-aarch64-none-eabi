import os
from pathlib import pathlib
from conans import ConanFile

class Package(ConanFile):
    name = "gcc-arm-none-eabi"
    version = "14.2.1"

    def build(self):
        url = "https://github.com/ck989/gcc-aarch64-none-eabi.git"
        self.run(f"git clone --depth=1 {url} gcc")

        return
    
    def package(self):
        self.copy("*", src="gcc", dst="")
        return
    
    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
        return

