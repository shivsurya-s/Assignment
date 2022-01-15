from datetime import date
def age_to_years(dob):
    current_date=date.today()
    age = current_date.year - dob.year -((current_date.month, current_date.day) <
         (dob.month, dob.day))
    return age
age_to_years(date(1998, 9, 30))
