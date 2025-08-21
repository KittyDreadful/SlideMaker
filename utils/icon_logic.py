import os
from pptx.util import Inches
from config import ICON_DIR, ICON_MAP

def add_icons(slide, row):
    icon_left = Inches(8.5)
    icon_top = Inches(1.0)
    spacing = Inches(0.6)
    icons = []

    if str(row.get("oe", "")).lower() == "yes":
        icons.append(ICON_MAP["oe"])
    if str(row.get("pd", "")).lower() == "yes":
        icons.append(ICON_MAP["pd"])
    if str(row.get("tspv", "")).lower() == "yes":
        icons.append(ICON_MAP["tspv"])

    cred_type = str(row.get("credential_type", "")).lower()
    if cred_type == "cert":
        icons.append(ICON_MAP["cert"])
    elif cred_type == "apl":
        icons.append(ICON_MAP["APL"])

    for i, icon_name in enumerate(icons):
        icon_path = os.path.join(ICON_DIR, icon_name)
        if os.path.exists(icon_path):
            slide.shapes.add_picture(icon_path, icon_left, icon_top + i * spacing, width=Inches(0.5))
