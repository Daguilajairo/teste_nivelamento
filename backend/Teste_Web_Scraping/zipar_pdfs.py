import os;
import zipfile;

pdf_folder = os.path.join ("data","pdfs")
zip_filename = os.path.join("zips","anexos.zip")

with zipfile.ZipFile(zip_filename, "w") as zipf:
    for file in os.listdir(pdf_folder):
        if file.endswith(".pdf"):
            file_path = os.path.join(pdf_folder, file)
            zipf.write(file_path, arcname=file)
            print(f"adicionado ao zip: {file}")

            print(f"\n arquivo {zip_filename} criado!")
