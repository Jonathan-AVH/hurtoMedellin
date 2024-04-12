import pandas as pd
from taipy.gui import Gui, Html
from taipy.gui import Gui 
import taipy.gui.builder as tgb 
from taipy.gui import Markdown
from src.pages.pagina1 import pagina_1
from src.pages.pagina2 import pagina_2
from src.pages.pagina3 import pagina_3

pages = {"PAGINA-1": pagina_1, "PAGINA-2": pagina_2, "PAGINA-3": pagina_3}

Gui(pages=pages).run()