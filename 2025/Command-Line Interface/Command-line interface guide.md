# Working With The Command-Line Interface 

This guide on the Command-line interface is based on the Demo of the Command Prompt in Windows, during the third Bits and Bots expert meeting. 
However, commands for other Operating Systems have been included. Feel free to add to this guide if useful information is missing.

## Table of Contents
1. [Windows](#Windows)
2. [Mac](#Mac)
3. [Linux](#Linux)
4. [Batch Scripts](#Batch)
<br/>

## Windows <a name="Windows"></a>
The command-line interface for Windows is the command prompt. With the command prompt you can execute commands to do different tasks. 

  ### How to start the Command Prompt? 
To start the Command Prompt on Windows, you open the start menu on the left of you taskbar. 

![open cmd](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/open_cmd.png)

Once opened, you type 'cmd'. The result is the command prompt which you can then click on to open. Once opened, it looks like this: 
![cmd opened](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/cmd_opened.png)

If you want to know which commands there are and what they do, use the following commands:
|Command | Explanation |
|:----|:----------|
|help||
|[command] /?|| 

### Knowing where you are
|Command | Explanation |
|:---|:-----------|
|cd|Using cd and then added the directory name moves you into that directory. So if I am in C: and there is a subdirectory called Documents where you want to go to, just type cd Documents and you will move into that subdirectory.|
|cd..|When you want to go up into a parent directory, you use cd.. . Example: If you are in C:/Documents and you want to go back to just C:.| 
|C:|If you want to change to another drive, just type C:, H:, or whichever works for you.|
|dir|List files and folders in the current directory.|
|tree|Display a folder structure graphically as a tree.|
|start .|Open the current directory in File Explorer.|

### Creating folders and files
|Command | Explanation |
|:---|:-----------|
|mkdir newfolder|Creates a new directory called newfolder.|
|copy nul newfile.text|Creates a new empty text file called newfile.| 
|copy file.txt D:\Backup\|Copies the file called file.txt to another location.|
|move file.txt D:\Archives\|Moves the file called file.txt to a new folder.|
|del file.txt|Delete a file. Warning: this is a permananet delete, this will not even appear in your bin after deletion. To control deletion and add a prompt, use del /p.|
|rmdir /s oldfolder|Deletes the oldfolder and its contents.|
|echo Archived on %date% > note.txt|Write the current date to a text file.|

### Other useful commands to know
|Command | Explanation |
|:---|:-----------|
|find /c /v "" file.txt|Count the number of lines in a file.|
|findstr /S /I "keyword" *.txt|Search for a keyword in all .txt files.| 
|fc file1.txt file2.txt|Compare two text files line by line.|
|attrib +R file.txt|Make a file read-only.|
|xcopy source\ destination\ /E /I /H|Copy folders with all files and subfolders.|
|robocopy C:\Source D:\Backup /MIR|Mirror folders with robust options.|
|compact /s|Check or compress files using NTFS compression.|

  ### Changing the title and color
To start, you can try and change the title of the window to give it a more meaningful name. You do this using the title command. To know what a command does, you can type in: title /?. Do not forget to press ENTER after each command.

By doing this, you get an explanation of the command. Furthermore, you also get an example of how to use it. In the case of title, you get: TITLE [string]. The string specifies the title for the command prompt window.

To change the title of the window to Demo you type in the following: title Demo.
![Title demo](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/demo.png)

Next, we can change the color of the window and the letters by using the color command. We start again with using /? so we can get more guidance on how to use this command.

The color command sets the default console foreground and background colors. The use of it is: COLOR [attr]. [attr] is what specifies the color attribute of console output. These attributes are specified by two hex digits: the first corresponds to the background, the second to the foreground. Then a list is given with options.

To get a bright white background with red letters: color fc

To go back to a black background with white letters: color 07
![Colours](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/color_attributes.png)


  #### Dir command
In the command prompt, you can go into different folders (also called directories) and navigate your way around. As you can see in the previous screenshots, I am currently in my H drive (H:\). I want to go into a directory, but I am not sure which directories there are in my H drive. To find out, I use the dir command. This command can be used to display a list of files and subdirectories. When you type in dir /? you get an overview of all the different options available to use with this command. Every option can be useful for a different purpose, so do not forget to check out this command to see which option would work best for your purposes. Here are some useful examples:

|Command | Explanation |
|:---|:-----------|
|dir|Displays the list of files and subdirectories in a directory.|
|dir /B|Uses bare format (no heading information or summary).| 
|dir /S|Displays files in specified directory and all subdirectories.|
|dir /Q|Display the owner of the file.|

![Dir](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/dir_explained.png)

Lets see how they all work. For this demo, I have created a directory with several subdirectories in it: demo_cmd. Lets try some options of the dir command here. 

   #### dir
We start by just using the dir command

![Dir overview](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/dir.png)

  ##### dir /B
The command **dir /B** gives you the bare format, without heading information or summary. 

![Dir bare format](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/dir_bare_format.png)

   ##### dir /S
![Dir subdirectories](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/dir_subdirectories.png)

Note that this is not the entire result, just a part of it. As you can see, you get an overview of the subdirectories and the files in it, but it also checks those subdirectories and gives you an overview of that.

   ##### dir /Q
dir /Q also gives you the owner. In my case, this is not very interesting because I created everything. But as archivists, we receive collections from others all the time, so this command could be handy.
![Dir show owner](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/dir_show_owner.png)

  #### Tree command
You could also want a more visual view of the subdirectories and files. 
In this case, you can use the tree command 

![Tree command](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/tree_command.png)

  ### Change directories
As you can see in the previous screenshot I am currently in my H drive in the subdirectory Demo_cmd. How did I get here? By using the change directories command: cd [directory you want to go in]. Cd stands for changing directories.

![cd](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/change_directories.png)

I can also go back by using the cd command, but with the addition of two dots: cd..

![cd go back](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/cd_go_back.png)

You can also change drives. I am currently in my H drive, but I also have a C drive. To change drive, you simple type in [DRIVE]:. For me, this is: C:

![cd change drive](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/change_drive.png)

  ### Echo <br/>
You can use the echo command in different ways:
* Show basic output
* Using variables
* Blank lines
* Creating a simple text file

**Show basic output** <br/>
As the people following the Python track are familiar with, the first step is always to print the message “Hello World”. Instead of using the print function, we need to use the echo command in the command prompt. Especially in a [batch script](#Batch) it can be useful to add this, to provide feedback or display information during the running of that script.

To get Hello World, type: echo Hello World

![Echo](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/echo.png)

**Using variables** <br/>
You can also create a temporary enviroment variable. 
```
set MYNAME=Lotte
echo Hello, %MYNAME%
```
This will give you the result: Hello, Lotte. Using echo this way can help you in scripts you write and automation. 

**Blank lines** <br/>
When you are typing *echo.* you are printing a blank line. This is not the most useful when you are just using it on your one. But you can also add this in a [batch script](#Batch) to improve readability of the output.

**Creating a simple text file** <br/>
You can also use the echo command to send output to a file. You can then use *type* to see what is in that file:
```
echo This is a test > test.txt

type test.txt
```

If you want to add to a file, you have to do it in another way. If you try to first method, you will overwrite your file. To append the test file:
```
echo Adding another line >> test.txt
```

  ### Renaming a file
In H:\Demo_cmd\Test I have a file named B.txt. 

![B.txt](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/Example_file.png)

I want to change B.txt to A.txt. I need to rename it. I can do this using the ren command.

![A.txt](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/Rename_example_file.png)


I can change the name by typing in the following: ren [old name file] [new name file] 
In this case: ren B.txt A.txt 

I do not need to specify the file path here because it is all happening where I currently am: H:\Demo_cmd\Test 

However, here it is with the file paths included: ren H:\Demo_cmd\Test\B.txt H:\Demo_cmd\Test\A.txt

  ### Making a new directory
  If I want to create a new directory in my demo_cmd I can do this using the mkdir command. To create a new directory I type: mkdir demo_test

  To see if it worked, you can use the dir or tree command again.
  
  ![Tree view](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/tree_command.png)

  ### Copy a file
  If I want to copy A.txt (which is in my Test directory) to the new demo_test directory, I  can use the copy command. This leads to the following: copy A.txt  H:\Demo_cmd\demo_test.

   ![Copy file](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/copy_file.png)
   
  ### Deleting a file
To delete a file, you can use the del command. However, it is recommended to also add  /P to your command. /P gives you a prompt for confirmation before deleting each file.  This is useful so you have an extra check built in.

To delete the file I just copied: del /P A.txt

![Delete file](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/delete_file.png)


In the screenshot you can see the prompt, where I need to type in Y or N for it to do it, or stop it.

  ### Executing a batch script
A batch script is a series of command to be executed by the command-line interpreter,  stored in a plain text file. This is useful if you have a workflow for example. If I want to  change the title, change the color, copy a file, and delete a file all in one go without typing these in all the time.

To create a batch script, you simply open your notepad and type in the command (one on  each line). Then you save it as a .bat file.

![Create Batch Script](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/create_batch_script.png)

After creating this script, I go into the directory where the bat script resides and type in  the name of the file: example.bat

This leads to the command prompt doing these command one after the other without  me having to type them in individually.

  ### Executing a Python or HTML script
  Executing a Python script is almost the same. You simply go to where the file is and type in the name of the file.

![Execute file 1](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/Execute_.pyfile.png)

You can also execute the file from somewhere else, just do not forget to type in the complete path.

![Execute file 2](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/Execute_.pyfile_2.png)

For HTML this all works the same. Just type in the file (example: DuckArchive.HTML). With HTML files, this will start up in your browser which automatically gets booted up  for you after entering the command.
  
  ### Stopping a task
  When starting the Jokes.py program or when executing the tree command on your complete H drive (may take it a while), you might want to stop the task. You can of course  close the window, but this is of course not the proper way. The proper way is to use ctrl  + C.
 
  ### Start Wordpad
To start up Wordpad using your command prompt, you simple type write

### Start Word
For Word, I had to go into my C drive since that is where the program is. To change Drives, just type in the Drive you want to go to and it works. For example, I want to go  from the H: Drive to the C: Drive:

![Change drive](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/change_drive.png)

I need to access the file Winword.exe. However, just typing this in like we did with  Python and HTML files will not suffice. You also need to write start.

To start windows: start winword.exe
  
  ### Calculating a checksum
  Checksums are values that are generated from transmitted data before and after transmission. They are a sort of fingerprint for your file. If the checksum stays the same,  you know the file is the same. If anything has changed, the checksum too will have  changed. This can indicate bit rot or an error that happened during migration.

The command to calculate a checksum is certutil -hashfile

Calculate an MD5 checksum: certutil -hashfile [file name] MD5

Calculate a SHA512 checksum: certutil -hashfile [file name] MD5

![Calculate checksum](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/calculate_checksum.png)

You can also calculate a checksum on an entire folder using a batch script:

![Calculate checksum Batch Script](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/calculate_checksum_batch_script.png)

Here is a breakdown of the script:
* **@echo off**: This line turns off the command echoing in the batch script, meaning that  commands themselves won’t be printed to the console when they are executed.
* **for %%f in (H:\Demo_cmd\literature\*) do (…)**: This line sets up a loop that iterates over each file (%%f) in the directory  specified (H:\Demo_cmd\literature\). The * is a wildcard character that matches  any file in that directory.
* **certutil -hashfile "%%f" SHA256**: Within the loop, this command calculates the SHA256 hash value for each file  (%%f) found in the directory specified. certutil is a command-line utility that  performs various cryptographic operations, including hashing files. -hashfile is  an option that tells certutil to hash a specified file. "%%f" is the file being hashed, and SHA256 specifies that the hash algorithm used should be SHA256.

In short, this script goes through each file in the specified directory and calculates its  SHA256 hash value using the certutil command.

Note that the certutil command can do a lot more. To see all the options, type certutil /?

  ### Cleaning the Window
If you enter multiple commands, your window can get full and a bit cluttered. To get a clean state, you can use the clean screen command: cls

![Clear screen](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/cleaning_the_window.png)

  ### Closing the command prompt
  To close the command prompt, you can close the window by clicking the x on the top  right. But the more correct way is to use the exit command. Simply type exit, press  ENTER, and the window will close.

  ### Rescources 
[The Complete List of Command Prompt Commands](https://www.lifewire.com/list-of-command-prompt-commands-4092302) 

## Mac <a name="Mac"></a>

  ### How to start the Terminal? 

  ### Knowing where you are
  |Command | Explanation |
|:---|:-----------|
|pwd|Print Working Directory — shows where you are.|
|ls|List files and directories in the current folder.| 
|ls -l|Long listing format with details like size and date.|
|ls -a|Include hidden files (those starting with .).|
|cd foldername|Change directory to a folder.|
|cd..|Go up one level in the directory tree.|
|open .|Open the current directory in Finder.|

  ### Creating folders and files
  |Command | Explanation |
|:---|:-----------|
|mkdir newfolder|Make a new directory called newfolder.|
|touch newfile.text|Create a new, empty file.| 
|cp file.txt ../backup/|Copy file to another location.|
|mv file.txt ../archives/|Move (or rename) a file.|
|rm file.txt|	Delete a file (Warning: this is irreversible!).|
|rm -r oldfolder/|Delete a folder and all its contents.|
|echo "Archived on $(date)" > log.txt|Write the current date to a text file.|

  ### Other useful commands to know
  |Command | Explanation |
|:---|:-----------|
|find . -type f -name "*.tif"|Find all .tif files in current and subfolders.|
|grep -Ri "keyword" .|	Search for a keyword in all text files.| 
|diff file1.txt file2.txt|Compare two text files.|
|chmod 444 file.txt|Make file read-only for all users.|
|du -sh *|	Show size of folders/files in current directory.|
|rsync -avh source/ destination/|Copy files/directories with metadata preserved.|
|zip -r archive.zip folder/|Compress a folder into a .zip archive.|

  ### Resources

## Linux <a name="Linux"></a>
The command-line interface for Linux is the Terminal. With the terminal you can execute commands to do different tasks. 

  ### How to start the Terminal? 
In the search bar in your OS, you can type either "terminal", "command", "prompt", or "shell". 

![open terminal](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/open_terminal.png)

Once opened, it looks like this: <br/>
![terminal_openl](https://github.com/Susanne404/B-B-test/blob/main/cmd_guide/guide_resources/terminal_open.png)

  ### Knowing where you are

|Command | Explanation |
|:---|:-----------|
|cd|Using cd and then added the directory name moves you into that directory. So if I am in C: and there is a subdirectory called Documents where you want to go to, just type cd Documents and you will move into that subdirectory.|
|cd..|When you want to go up into a parent directory, you use cd.. . Example: If you are in C:/Documents and you want to go back to just C:.| 
|C:|If you want to change to another drive, just type C:, H:, or whichever works for you.|

### Creating folders and files

  ### Resources
* [The Linux command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)

  
## Batch scripts <a name="Batch"></a>
A batch script is a text file that contains a series of commands to be executed in sequence. You can make one by simply opening your notepad, typing some commands, and saving the file as a .bat file. Make sure each command is on its own line.

Here are some useful commands to use in your batch script:
|Command | Explanation |
|:---|:-----------|
|ECHO OFF|This command cleans up your output by hiding the commands executed from being shown.|
|PAUSE|If you are running a batch script straight from the file explorer instead of your command-line interface, you can add PAUSE to your batch filem to make sure the command-line interface does not shut off after executing the commands. This way you can see the output.| 
|ECHO.|This adds a blank line. When executing multiple commands the output can look very cluttered. To clean it up a bit you can add a blank line for readability.|

  ### Resources
  * [Batch Script Tutorial](https://www.tutorialspoint.com/batch_script/index.htm)
  * [Basics of Batch Scripting](https://www.geeksforgeeks.org/linux-unix/basics-of-batch-scripting/)
  * [How to Write a Batch Script on Windows](https://www.howtogeek.com/263177/how-to-write-a-batch-script-on-windows/)
