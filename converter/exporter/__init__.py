from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty
from bpy.types import Operator
import bpy


def register():
    bpy.utils.register_class(ExportPrusa)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportPrusa)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


class ExportPrusa(Operator, ExportHelper):
    # important since its how bpy.ops.import_test.some_data is constructed
    bl_idname = "export_prusa.subdiv_data"
    bl_label = "Export STL"

    # ExportHelper mixin class uses this
    filename_ext = ".stl"

    filter_glob: StringProperty(
        default="*.stl",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )  # type: ignore

    def execute(self, context):
        return export_data(context,
                           self.filepath)  # type: ignore


def menu_func_export(self, context):
    self.layout.operator(ExportPrusa.bl_idname,
                         text="Prusa Slicer (.stl)")


def export_data(context, filepath: str):
    if not bpy.context.active_object.mode == "OBJECT":
        bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

    export_format = "STL"

    bpy.ops.object.select_all(action='DESELECT')
    print("exporting")
    for o in bpy.data.objects:  # type: ignore
        if not o.visible_get(view_layer=bpy.context.view_layer):
            continue
        col = o.instance_collection
        if col is not None and col.name == "Cutter":
            print("found cutter, skipping")
            continue
        if not o.type == "MESH":
            continue
        bpy.context.view_layer.objects.active = o  # type: ignore
        for mod in o.modifiers:
            if not mod.is_active:
                continue
            print("applying modifier " + mod.name + " for " + o.name)
            bpy.ops.object.modifier_apply(modifier=mod.name)
        o.select_set(True)
    bpy.ops.export_mesh.stl(filepath=filepath, check_existing=False,
                            use_selection=True, use_mesh_modifiers=True, use_scene_unit=True, ascii=True, global_scale=1.0, batch_mode='OFF', axis_forward='Y', axis_up='Z')
    return {'FINISHED'}
