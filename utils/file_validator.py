import os
import time

class FileValidation:

    def validate_file(self, path, filename):
        time.sleep(5)
        files = os.listdir(path)
        return filename in files