import bpy

# class name general pattern = ADDONPREFIX_TYPE_name
# class name operator pattern = MYADDON_PT_main_panel
# operator bl_idname = MYADDON_PT_main_panel (preferably the same name as the class)
class EXAMPLE_PT_panel(bpy.types.Panel):
    bl_label = "Panel Name"  # Name shown at the top of the panel
    bl_idname = "EXAMPLE_PT_panel"  # Unique identifier for the panel
    bl_space_type = 'VIEW_3D'  # Editor where the panel appears
    bl_region_type = 'UI'  # UI region (UI = sidebar)
    bl_category = "Example"  # Sidebar tab name
    bl_context = ""  # Optional context where the panel is visible
    bl_options = {'DEFAULT_CLOSED'}  # Panel options (ex: start collapsed)
    bl_parent_id = "parent_idname" # Optional the parent panel id_name
    bl_order = 0 # Optional the priority order of the panel

    @classmethod
    def poll(cls, context) -> bool:  # Optional, used to check if the panel should be drawn
        return True

    def draw(self, context):
        layout = self.layout  # Layout used to draw UI elements
        layout.label(text="Text in the panel")  # Example label
        layout.operator("example.operator")  # Button that calls an operator
        