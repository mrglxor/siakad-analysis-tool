import os

def create_output_directory():
    output_directory = './data/'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    return output_directory