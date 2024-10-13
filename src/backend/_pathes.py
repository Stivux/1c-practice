import os
from pathlib import Path
from _constants import APP_ID

local_share_dir = Path.home() / '.local' / 'share' / APP_ID

local_share_dir.mkdir(parents=True, exist_ok=True)