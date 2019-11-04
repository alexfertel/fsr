import eel
from src import text_extractor, hooks
eel.init('web', allowed_extensions=['.js'])
eel.start('index.html')

