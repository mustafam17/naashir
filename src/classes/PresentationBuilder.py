from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.util import Pt
from pptx.enum.text import PP_ALIGN


class PresentationBuilder:
    def __init__(
        self,
        title: str,
        speaker_name_ar: str,
        speaker_name_en: str,
        text_ar: str,
        text_en: str,
    ):
        self.title = title
        self.speaker_name_ar = speaker_name_ar
        self.speaker_name_en = speaker_name_en
        self.text_ar = text_ar
        self.text_en = text_en
