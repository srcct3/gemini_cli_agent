from functions.get_files_info import get_files_info, get_file_content, write_file


feedback1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
feedback2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
feedback3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

print(feedback1)
print(feedback2)
print(feedback3)

# res1 = get_files_info("calculator", ".")
# res2 = get_files_info("calculator", "pkg")
# res3 = get_files_info("calculator", "/bin")
# res4 = get_files_info("calculator", "../")

# print(res1)
# print("\n")
# print(res2)
# print("\n")
# print(res3)
# print("\n")
# print(res4)
# print("\n")

# main = get_file_content("calculator", "main.py")
# calc = get_file_content("calculator", "pkg/calculator.py")
# err1 = get_file_content("calculator", "/bin/cat")
# err2 = get_file_content("calculator", "pkg/does_not_exist.py")

# print(main)
# print("-------------------------------------")
# print(calc)
# print("-------------------------------------")
# print(err1)
# print("-------------------------------------")
# print(err2)
# print("-------------------------------------")
