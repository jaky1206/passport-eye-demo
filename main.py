# https://ourcodeworld.com/articles/read/656/how-to-retrieve-machine-readable-zones-from-a-passport-image-with-python-using-the-passporteye-library
# https://pypi.org/project/PassportEye/

# Import PassportEye
from passporteye import read_mrz

# Process image
mrz = read_mrz(r"E:\CodeRepository\Tourista\passportEyeDemo\uploads\passport_wania.jpg")


# Obtain image
mrz_data = mrz.to_dict()

import pprint

pprint.pprint(mrz_data)

"""
print(mrz_data['country'])
print(mrz_data['names'])
print(mrz_data['surname'])
print(mrz_data['type'])
"""

# And so on with the rest of shown properties in the previous JSON string