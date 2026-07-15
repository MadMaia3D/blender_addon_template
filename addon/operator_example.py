import bpy

# class name general pattern = ADDONPREFIX_TYPE_name
# class name panel pattern = ADDONPREFIX_OT_operator_name
# operator bl_idname = addonprefix.operator_name
class EXAMPLE_OT_operator(bpy.types.Operator):
    bl_idname = "example.operator"  # Unique operator identifier (category.name)
    bl_label = "Operator Name"  # Name displayed in the interface
    bl_description = "Description of what the operator does"  # Tooltip when hovering
    bl_options = {'REGISTER', 'UNDO'}  # Operator options (show in log, allow undo)

    @classmethod
    def poll(cls, context) -> bool:  # Optional, used to check if the operator can run
        return True

    def execute(self, context):
        # Main code executed when the operator is called
        self.report({'INFO'}, "Operator executed")  # Message shown in Blender's status
        return {'FINISHED'}  # Indicates the operator finished successfully


# ---------------------------- REGISTRATION ----------------------------
classes_to_register = [EXAMPLE_OT_operator]


def register() -> None:
    for cls in classes_to_register:
        bpy.utils.register_class(cls)


def unregister() -> None:
    for cls in reversed(classes_to_register):
        bpy.utils.unregister_class(cls)
