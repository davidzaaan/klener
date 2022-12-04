class FolderEmptyError(Exception):
    """
        Custom exception that will be raised when there is no files to delete
    """
    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)