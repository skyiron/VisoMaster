class ModelLoadWhilePlayingException(Exception):
    """Exception raised when an attempt is made to load a model while playback is active."""
    
    def __init__(self, message="Cannot load a model while playback is in progress."):
        super().__init__(message)