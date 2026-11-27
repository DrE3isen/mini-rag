from .BaseController import BaseController
from fastapi import UploadFile
from src.models import ResponseSignal

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale=1048576  # 1 MB in bytes
    def validate_uploaded_file(self,file:UploadFile):
        print(f"file.content_type: {file.content_type}")
        print(f"file.size: {file.size}")
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False,ResponseSignal.FILE_TYPE_NOT_ALLOWED.value
        if file.size is None:
            return False,ResponseSignal.FILE_SIZE_NOT_SPECIFIED.value
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:  # Convert MB to bytes
            return False,ResponseSignal.FILE_SIZE_EXCEEDS_LIMIT.value
        return True,ResponseSignal.File_IS_VALID.value