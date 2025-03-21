# scraping-linkdin-package

Description. 
The package scraping-linkdin-package is used to:
	
	The scraping-linkdin-package package is used to scrape jobs from LinkedIn. It allows you to provide information such as job title, country, state, and city to search for job openings and save them to a CSV file. The main function is run(), which receives parameters positionally.
	

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install scraping-linkdin-package

```bash
pip install scraping-linkdin-package
```

## Usage

```python
from scraping_linkdin.scraping.linkdin_scraping import run

# Call the run() function with the parameters: vacancy, country, state and city
run("Desenvolvedor Python", "Brasil", "São Paulo", "São Paulo")
```

## Author
Luan Lopes de Siqueira

## License
[MIT](https://choosealicense.com/licenses/mit/)