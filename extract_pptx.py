import sys
from pathlib import Path

from pptx import Presentation

pptx_path = Path(sys.argv[1])
presentation = Presentation(pptx_path)

lines = []
for slide in presentation.slides:
    for shape in slide.shapes:
        if shape.has_text_frame:
            lines.append(shape.text_frame.text)

out_path = Path("notes") / (pptx_path.stem + ".txt")
out_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {out_path}")
