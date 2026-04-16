import sys
import logging
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="error occurred in python script name [{0}] line number[{1}] error message[{2}]".format(
    file_name,exc_tb.tb_lineno,str(error))
    return error_message




class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)


    def __str__(self):
        return self.error_message
    


# to check the working of the file
# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("divde by zero error")
#         raise CustomException(e,sys)


# Instead of just getting: ValueError: invalid literal for int()

#common fro all code


# You get something like: error occurred in python script name [main.py] line number [42] error message [invalid literal for int()]

# So it adds:
# 📄 File name
# 📍 Line number
# 💬 Original error message

# Why this is useful:
# Easier debugging
# Cleaner logs
# Standardized error handling

# This pattern is useful when:

# --You’re building a production system
# --You need structured logging
# --You want to hide internal details from users but log them internally
# --You're working in frameworks (ML pipelines, APIs, etc.)