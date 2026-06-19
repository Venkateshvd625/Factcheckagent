from google.colab import files

print("Upload your PDF files now:")
uploaded = files.upload()

for filename in uploaded.keys():
    print(f'Uploaded file "{filename}" with length {len(uploaded[filename])} bytes')
