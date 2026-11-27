from enum import Enum
class ResponseSignal(Enum):
    FILE_TYPE_NOT_ALLOWED = "file type not allowed"
    FILE_SIZE_NOT_SPECIFIED = "File size is not specified"
    FILE_SIZE_EXCEEDS_LIMIT = "File size exceeds the limit"
    File_IS_VALID = "File is valid"
    file_uploaded_successfully = "File uploaded successfully"
    FILE_UPLOAD_FAILED = "File upload failed"