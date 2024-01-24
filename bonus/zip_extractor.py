import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("C:/Users/Solidworks PC/PycharmProjects/To_do_App/bonus/05 compressed.zip",
                    "C:/Users/Solidworks PC/PycharmProjects/To_do_App/bonus/files")