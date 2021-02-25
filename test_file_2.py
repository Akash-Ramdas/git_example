import os

filename = "output.txt"
with open(filename, "w") as f:
    f.write("Output \n")

out_dir_name = "Output_dir"
curr_dir = os.getcwd()
out_dir = curr_dir + "/" + out_dir_name
os.chdir(out_dir)

filename = "output.txt"
with open(filename, "w") as f:
    f.write("Output \n")
