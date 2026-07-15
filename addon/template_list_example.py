import bpy



# class name general pattern = ADDONPREFIX_TYPE_name
# class name for Property Groups pattern = MYADDON_PG_name
# Stores the data for each item in the collection.
# Every element displayed by the UIList is an instance of this PropertyGroup.
class MYADDON_PG_item(bpy.types.PropertyGroup):
    name: bpy.props.StringProperty(
        name="Name"  # Name displayed for the item
    )



# class name general pattern = ADDONPREFIX_TYPE_name
# class name for UILists pattern = MYADDON_UL_name
# Defines how each item in the collection is drawn inside the template list.
# This class is responsible only for the visual representation of list items.
class MYADDON_UL_items(bpy.types.UIList):
    # Draws a single item in the list.
    def draw_item(
        self,
        context,
        layout,
        data,
        item,
        icon,
        active_data,
        active_property,
        index,
    ):
        # item is an instance of MYADDON_PG_item

        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.prop(item, "name", text="", emboss=False)

        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="")



# class name general pattern = ADDONPREFIX_TYPE_name
# class name for Property Groups pattern = MYADDON_PG_name
# Stores the collection displayed by the UIList and
# keeps track of the currently selected item.
class MYADDON_PG_root(bpy.types.PropertyGroup):
    items: bpy.props.CollectionProperty(
        type=MYADDON_PG_item  # Type stored in the collection
    )

    active_item: bpy.props.IntProperty(
        default=0  # Index of the selected item
    )



# ---------------------------- OPTIONAL HELPER INTERFACE FUNCTIONS ----------------------------
# ---------------------------- FUNCTIONS TO INTERFACE WITH THE LIST ----------------------------
# You can use layout.template_list to draw the list directly in a panel, or you can use a function like this:
def draw_example_template(context: bpy.types.Context, layout: bpy.types.UILayout) -> None:
    props = context.scene.addon_template_props

    layout.template_list(
            listtype_name="MYADDON_UL_items",   # UIList class name
            list_id="",                         # Optional unique identifier
            dataptr=props,                      # Object that owns the collection
            propname="items",                   # CollectionProperty name
            active_dataptr=props,               # Object that owns the active index
            active_propname="active_item",      # IntProperty storing the active index
            rows=5,                             # Number of visible rows
            maxrows=10,                         # Maximum rows when expanding
            type='DEFAULT',                     # DEFAULT, COMPACT, or GRID
        )


# This operator adds a new item to the list
class EXAMPLE_OT_add_to_example_list(bpy.types.Operator):
    bl_idname = "example.add_to_example_list"
    bl_label = "Add"
    bl_description = "Adds a new item to the list"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context) -> bool:
        return True

    def execute(self, context) -> set[str]:
        props: MYADDON_PG_root = context.scene.addon_template_props
        current_index = len(props.items)
        item = props.items.add()
        item.name = "name_" + str(current_index)
        props.active_item = current_index
        return {'FINISHED'}


# This operator deletes the selected item from the list
class EXAMPLE_OT_delete_from_list(bpy.types.Operator):
    bl_idname = "example.delete_from_list"
    bl_label = "Delete"
    bl_description = "Delete selected item from the list"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context) -> bool:
        props: MYADDON_PG_root = context.scene.addon_template_props
        current_length = len(props.items)
        active_item = props.active_item
        if (current_length < 1):
            return False
        
        if (active_item < 0 or active_item >= current_length):
            return False
        
        return True

    def execute(self, context) -> set[str]:
        props: MYADDON_PG_root = context.scene.addon_template_props
        props.items.remove(props.active_item)
        return {'FINISHED'}


# ---------------------------- REGISTRATION ----------------------------
classes_to_register = [
    MYADDON_PG_item,
    MYADDON_UL_items,
    MYADDON_PG_root,
    EXAMPLE_OT_add_to_example_list,
    EXAMPLE_OT_delete_from_list,
]

# Properties instances should be created with the convention addonprefix_propertyname
def register() -> None:
    for cls in classes_to_register:
        bpy.utils.register_class(cls)

    bpy.types.Scene.addon_template_props = bpy.props.PointerProperty(type=MYADDON_PG_root)



def unregister() -> None:
    del bpy.types.Scene.addon_template_props
    
    for cls in reversed(classes_to_register):
        bpy.utils.unregister_class(cls)
