import sys
from src.logger import logging

"""
this script creates a custom informative error messages, which are useful for
debugging.
"""
def error_message_detail(error, error_detail: sys):

    # this function builds the detailed error message
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message='Error occurred in python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message        

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)

        # it calls the helper func tp generate detailed message
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    # it returns detailed message when a exception is printed
    def __str__(self):
        return self.error_message
    