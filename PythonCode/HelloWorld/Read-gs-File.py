# pip install google-cloud-storage

# python code to read file from public cloud storage bucket
# https://storage.googleapis.com/pub/shakespeare/rose.txt (Public URL to view file)
# gs://pub/shakespeare/rose.txt (gsUtil uri to view file)

# input_file = 'gs://pub/shakespeare/rose.txt'

# gs://public-rk/file1.json
# https://storage.googleapis.com/public-rk/file1.json

from google.cloud import storage

# Initialize a client to interact with the Google Cloud Storage service
client = storage.Client()

# Specify the name of your Google Cloud Storage bucket and the path to the file
bucket_name = 'public-rk'
file_path = 'file1.json'

# Get a reference to the bucket and file
bucket = client.bucket(bucket_name)
blob = bucket.blob(file_path)

# Download the contents of the file
file_contents = blob.download_as_text()

# Print the contents of the file
print(file_contents)


