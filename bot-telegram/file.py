import zipfile
file = "test.zip"
f = zipfile.zipFile(file)
f.extractall()