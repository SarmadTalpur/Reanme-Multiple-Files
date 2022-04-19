# Python 3 code to rename multiple files in a directory or folder

# importing os module
import os

# Function to rename multiple files
def main():
    i = 00
    folder = "F:\\test\\Pair"
    
    # loop through all the files in the directory
    for count, filename in enumerate(os.listdir(folder)):
        # if the file name contains "COLOR_L" rename should be i_left i.e., 00_left
        if "COLOR_L" in filename:
            dst = f"{i}_left.jpg"
            # foldername/filename, if .py file is outside folder
            src =f"{folder}/{filename}"
            dst =f"{folder}/{dst}"
        # else rename should be i_right i.e., 00_right
        else:
            dst = f"{i}_right.jpg"
            # foldername/filename, if .py file is outside folder
            src =f"{folder}/{filename}"
            dst =f"{folder}/{dst}"
		
		# rename all the files
        os.rename(src, dst)
        
        # always increment i after 2 files renamed
        if count%2 != 0:
            i+=1
        

# Driver Code
if __name__ == '__main__':
	
	# Calling main() function
	main()
