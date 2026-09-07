# Assignment 16: File Extension Analyzer
#
# Given:
# files = [
#     "resume.pdf",
#     "photo.jpg",
#     "report.pdf",
#     "data.csv",
#     "image.png",
#     "notes.txt"
# ]
#
# Create functions that return:
# {
#     "pdf": 2,
#     "jpg": 1,
#     "csv": 1,
#     "png": 1,
#     "txt": 1
# }
#
# Handle:
# - file
# - README
# - archive.tar.gz
#


files = [
    "resume.pdf",
    "photo.jpg",
    "report.pdf",
    "data.csv",
    "image.png",
    "notes.txt"
]

def get_extension(filename):
    if "." not in filename:
        return None

    parts = filename.split(".")

    if len(parts) < 2 or parts[-1] == "":
        return None

    return parts[-1].lower()

def count_extensions(files):
    result = {}

    for file in files:
        extension = get_extension(file)

        if extension is not None:
            if extension in result:
                result[extension] += 1
            else:
                result[extension] = 1

    return result

print(count_extensions(files))