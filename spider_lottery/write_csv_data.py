import csv

# print(dir(csv.writer))

returns_path = "/Users/pizi/Documents/git_flie/code_file/names.csv"
files = open(returns_path, 'w')
writer = csv.writer(files)
writer.writerow(['data', 'name'])
writer.writerow(['123', 'wwww'])
files.close()