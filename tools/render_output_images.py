import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(__file__))
ASSETS_DIR = os.path.join(ROOT, "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# Simulated terminal-like output text
outputs = {
    "task1_output.png": [
        "$ php task1_largest.php",
        "Input numbers: 12, 25, 7",
        "Largest number is: 25",
    ],
    "task2_output.png": [
        "$ php task2_reverse.php",
        "Input string: Hello, World!",
        "Reversed string: dlroW ,olleH",
    ],
}

# Choose a monospace font; fall back to default if not found
font = None
for candidate in [
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/usr/share/fonts/TTF/DejaVuSansMono.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",
    "/System/Library/Fonts/Menlo.ttc",
    "/Library/Fonts/Menlo.ttf",
]:
    if os.path.exists(candidate):
        try:
            font = ImageFont.truetype(candidate, 20)
            break
        except Exception:
            continue

if font is None:
    font = ImageFont.load_default()

for filename, lines in outputs.items():
    # Determine image size based on text
    padding = 20
    line_spacing = 8
    dummy_img = Image.new("RGB", (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    widths = []
    heights = []
    for line in lines:
        w, h = draw.textbbox((0, 0), line, font=font)[2:]
        widths.append(w)
        heights.append(h)
    width = max(widths) + padding * 2
    height = sum(heights) + line_spacing * (len(lines) - 1) + padding * 2

    # Create image
    img = Image.new("RGB", (width, height), color=(248, 250, 252))  # light gray
    draw = ImageDraw.Draw(img)

    # Draw border and text
    border_color = (30, 41, 59)
    draw.rectangle([(0, 0), (width - 1, height - 1)], outline=border_color, width=2)

    y = padding
    text_color = (15, 23, 42)
    for line in lines:
        draw.text((padding, y), line, fill=text_color, font=font)
        y += draw.textbbox((0, 0), line, font=font)[3] + line_spacing

    out_path = os.path.join(ASSETS_DIR, filename)
    img.save(out_path)
    print(f"Wrote {out_path}")
