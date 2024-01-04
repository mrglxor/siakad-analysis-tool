import inquirer
from modules.scraper import scrape_data
from modules.display import wait_for_enter
from modules.display import intro
from modules.utility import create_output_directory

if __name__ == "__main__":
    intro()
    wait_for_enter()

    valid_data_types = ['url', 'img', 'text', 'title', 'meta_description', 'specific_links', 'table_data']

    questions = [
        inquirer.List('data_type',
                      message="Pilih jenis data yang ingin diambil:",
                      choices=valid_data_types,
                      ),
    ]

    answers = inquirer.prompt(questions)

    url = "https://edlink.id"  # analisis ke edlink
    output_directory = create_output_directory()

    scrape_data(answers['data_type'], url, output_directory)
