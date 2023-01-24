# is_non_negative_num = lambda x: x.replace('.', '', 1).isnumeric()

is_non_negative_num = lambda x: x.replace(".", "", 1).isdigit() if "." in x else x.isdigit()