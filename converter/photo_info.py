class PhotoInfo:
    """Общий формат для фотографий после конвертации из api"""

    def __init__(self, file_name, height, width, url):
        self.file_name = file_name
        self.height = height
        self.width = width
        self.url = url

    def __str__(self):
        return str(self.__dict__)

    def to_dict(self):
        return self.__dict__

