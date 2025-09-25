from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

text1 = run_python_file("calculator", "main.py") # (should print the calculator's usage instructions)
print(text1)
text2 = run_python_file("calculator", "main.py", ["3 + 5"]) # (should run the calculator... which gives a kinda nasty rendered result)
print(text2)
text3 = run_python_file("calculator", "tests.py")
print(text3)
text4 = run_python_file("calculator", "../main.py") # (this should return an error)
print(text4)
text5 = run_python_file("calculator", "nonexistent.py") # (this should return an error)
print(text5)

# feedback1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# feedback2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# feedback3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
#
# print(feedback1)
# print(feedback2)
# print(feedback3)

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
