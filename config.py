import os

BASE_DIR = os.path.dirname(__file__)

TEMPLATE_PATH = os.path.join(BASE_DIR, "template", "template_slide.pptx")
DATA_PATH = os.path.join(BASE_DIR, "data", "data.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "output", "generated_deck.pptx")

ICON_DIR = os.path.join(BASE_DIR, "icons")
ICON_MAP = {
    "oe": "oe_icon.png",
    "pd": "pd_icon.png",
    "tspv": "tspv_icon.png",
    "cert": "cert_icon.png",
    "APL": "apl_icon.png"
}
