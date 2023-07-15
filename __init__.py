from . import converter
from . import auto_load

auto_load.init()

bl_info = {
    "name": "Prusa Export",
    "author": "xackery",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "File > Export, File > Import",
    "category": "Import-Export",
    "description": "Helper for Prusa Slicer Exporting",
}


def register():
    converter.register()
    auto_load.register()


def unregister():
    converter.unregister()
    auto_load.unregister()


if __name__ == "__main__":
    register()
