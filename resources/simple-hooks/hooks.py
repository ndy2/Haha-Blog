import os
import frontmatter
from datetime import date
from dateutil.rrule import rrule, DAILY

def create_til_csv(*args, **kwargs):
    create_til_csv_of(2022)
    create_til_csv_of(2023)


def create_til_csv_of(year):
    f = open(f"docs/posting/til/resources/{year}.csv", "w")
    f.write("date,til\n")

    new_year_date = date(year, 1, 1)
    last_year_date = date(year, 12, 31)

    til_dates = set()
    for file in os.listdir("docs/posting/til"):
        if(file.startswith(str(year))):
            til_date = file[:10].split('-')
            til_month = int(til_date[1])
            til_day = int(til_date[2])
            til_dates.add(date(year, til_month, til_day))

    for d in rrule(DAILY, dtstart = new_year_date, until = last_year_date):
        if d.date() in til_dates:
            til_doc = frontmatter.load(f"docs/posting/til/{d.date()}.md")
            til_value = til_doc['til']
            f.write(f"{d.date()},{til_value}\n")
        else:
            f.write(f"{d.date()},0\n")
    f.close()
