import bpy

if bpy.context.preferences.view.show_developer_ui:
    from .__refresh__ import reload_addon
    reload_addon(__name__)


from .addon import register_addon, unregister_addon

bl_info = {
    "name": "Addon Name",  # Name displayed in the Blender add-ons list
    "author": "Your Name",  # Author of the add-on
    "version": (1, 0, 0),  # Add-on version (major, minor, patch)
    "blender": (4, 0, 0),  # Minimum Blender version required
    "location": "View3D > Sidebar > Tab",  # Where the add-on appears in the UI
    "description": "Short description of what the add-on does",  # Brief explanation of functionality
    "warning": "",  # Warning shown to the user (ex: experimental, unstable)
    "doc_url": "",  # URL to the add-on documentation
    "tracker_url": "",  # URL for bug reports or issue tracking
    "category": "3D View",  # Category used in the Blender add-on preferences
}


def register() -> None:
    register_addon()


def unregister() -> None:
    unregister_addon()
