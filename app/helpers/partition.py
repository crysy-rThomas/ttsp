import tiktoken
from langchain.text_splitter import RecursiveCharacterTextSplitter
import csv

def partition(file):
    file_extension = file.filename.split(".")[-1]
    if file_extension == "txt":
        # openfile
        with file.file as f:
            data = f.read().decode("utf-8")
        splits = split_content(data)
    elif file_extension == "csv":
        # open file
        splits = []
        with file.file as f:
            content = f.read().decode("utf-8")
            csv_reader = csv.reader(content.splitlines())
            for row in csv_reader:
                splits.append(row[0])
    
    return splits


def split_content(content):
    tokenizer = tiktoken.get_encoding("cl100k_base")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=20,
        length_function=lambda x: len(tokenizer.encode(x)),
        is_separator_regex=False,
    )

    chunks = text_splitter.split_text(content)

    return chunks
