import os
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
sys.path.append(str(project_root / "app"))

os.environ["DATABASE_HOST"] = "localhost"
