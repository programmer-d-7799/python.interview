from typing import Dict, List


RETRY_CODES = [500, 503]


class FileUploadService:

    def __init__(upload_attempts=3, upload_delay=0):
        self.upload_attempts = upload_attempts
        self.upload_delay = upload_delay

    def set_upload_attempts(attempts: int):
        self.upload_attempts = attempts

    def upload_file_part(
        self, file_name: str, part_number: int, total_parts: int, byte_stream: str
    ) -> int:
        pass

    def file_uploaded(self, file_name: str) -> bool:
        pass

    def split_file(self, file_name: str) -> List[str]:
        """returning list of byte_stream"""
        pass

    def extract_file_name(self, file_path: str) -> str:
        pass

        # returns file name

    def upload_file_batch(files: List[str]) -> Dict[str, bool]:
        """files is a list of of file paths"""
        for file in files:
            file_parts = self.split_file(file)
            file_name = self.extract_file_name(file)
            num_file_parts = len(file_parts)
            for file_part_index, file_part in enumerate(file_parts):
                current_upload_attempts = 0
                while current_upload_attempts < 3 and not upload_result in RETRY_CODES:

                    upload_result = self.upload_file_part(
                        file_name, file_part_index, num_file_parts, file_part
                    )
                    if upload_result == SERVICE_OVERLOAD_CODE:
                        pass
                        # sleep upload_delay ()
                        return output


INSTANCE = FileUploadService()
