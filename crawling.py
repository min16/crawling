import glob, os
from create import createExcel, createCompanyInfo
from getUrl import getUrl

files = []
for filename in glob.glob('templates/*.html'):
        files.append(filename)

link_list = []
for filename in files:
    new_link_list = getUrl(filename)

    link_list += getUrl(filename)

# print(link_list)
# print(len(link_list))
#
company_list = []
for link in link_list:
    company_list.append(list(createCompanyInfo(link).__dict__.values()))

createExcel(company_list)
