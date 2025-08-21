from logger import setup_logger
from utils.data_loader import load_data
from utils.slide_generator import load_template, duplicate_slide, replace_placeholders
from utils.icon_logic import add_icons
from config import OUTPUT_PATH

logger = setup_logger()

def main():
    logger.info("Starting deck generation...")
    df = load_data()
    prs = load_template()
    template_slide = prs.slides[0]

    for _, row in df.iterrows():
        slide = duplicate_slide(prs, template_slide)
        replace_placeholders(slide, row)
        add_icons(slide, row)

    prs.save(OUTPUT_PATH)
    logger.info(f"Deck saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    main()
