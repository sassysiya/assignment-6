def student_data(info_needed):
    directory = {"student_id":"22106021",
    "student_name" : "Sanyam Mahajan",
    "student_stream": "cseds"}
    print(directory.get(f'{info_needed}'))


student_data(str(input('What do you want to know?')))
