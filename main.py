from google_form import FillForm
from scraping_data import ZillowScraper

scrap_data = ZillowScraper()
form_data = scrap_data.scrap_now()

form = FillForm()
form.fill_now(form_data)

