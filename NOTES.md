https://canva.zoom.us/j/92593347891?pwd=RzhlOFcxUVhVVWJUZFVtY1FiN0Qvdz09
https://docs.google.com/document/d/1mQa7DMs8R5tH3RBwOyHW_Yuysym9j8SnuM15WEn75rI/edit

Eric Fung, Or Straze

Use external storage,
Develop a module to use external storage?
Define subset of function

2 end points,
Multi part upload interface
Part number
Key
Total number of parts
Robust, could be flaky
Batch number of big files to upload 
Exist has file been uploaded

Define interface to start off. 

Upload a file in parts
upload_file_parts(key: file_name, part_number, total_parts, byte_stream: bytes) -> True, 
file_uploaded(file_name) -> True

Call that uploads batch of files
upload_file_batch(files: List[str]) -> Dict[file_name: bool]

