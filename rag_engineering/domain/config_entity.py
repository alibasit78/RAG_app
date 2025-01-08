import os
from dataclasses import dataclass

from .constants import *


class LinkedinDataIngestionConfig:
    linkedin_post_dir: str = os.path.join(LINKEDIN_POST_DIR)
    linkedin_post_file: str = LINKEDIN_POST_FILE_NAME