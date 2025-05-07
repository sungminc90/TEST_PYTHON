import zipfile

with zipfile.ZipFile("result.zip", "w") as zipf:
    zipf.writestr("data.txt", "This is test content.")
