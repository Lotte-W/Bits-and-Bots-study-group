# Content

[How to start the command prompt? [2]][2]

[Changing the title and color [2][1]][1]

[Echo [4]][4]

[Knowing where you are [4][3]][3]

[dir command [4][5]][5]

[dir [5]][5]

[dir /B [6]][6]

[dir /S [7]][7]

[dir /Q [7][8]][8]

[Tree command [8]][8]

[Change directories [8][9]][9]

[Renaming a file [9]][9]

[Making a new directory [9][10]][10]

[Copy a file [10]][10]

[Deleting a file [10][11]][11]

[Executing a batch script [11]][11]

[Executing a Python or HTML script [11][12]][12]

[Stopping a task [12]][12]

[Start Wordpad [12][13]][13]

[Start Word [12][14]][14]

[Calculating a checksum [12][15]][15]

[Cleaning the window [13]][13]

[Closing the command prompt [14]][14]

[Overview commands [14][16]][16]

[Overview Windows/Linux/macOS [15]][15]

Disclaimer: for the guide and demo I have used the Windows Command Prompt. I have added a table at the end with each command in Windows/Linux/Mac.

<span id="_Toc164795561" class="anchor"></span>*How to start the command prompt?  
To start the command prompt on Windows, you open the start menu on the left of your taskbar.

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image1.png" style="width:4.50943in;height:2.54354in" />

Once opened, you type ‘cmd’. The result is the command prompt which you can then click on to open. Once opened, it looks like this:

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image2.png" style="width:6.64995in;height:3.46718in" />

# Changing the title and color

To start, you can try and change the title of the window to give it a more meaningful name. You do this using the title command. To know what a command does, you can type in: title /?

By doing this, you get an explanation of the command. Furthermore, you also get an example of how to use it. In the case of *title*, you get: TITLE \[string\]. The string specifies the title for the command prompt window.

To change the title of the window to Demo you type in the following: title Demo.

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image3.png" style="width:5.60417in;height:2.59375in" />

Next, we can change the color of the window and the letters by using the color command. We start again with using /? so we can get more guidance on how to use this command.

The color command sets the default console foreground and background colors. The use of it is: COLOR \[attr\]. \[attr\] is what specifies the color attribute of console output. These attributes are specified by two hex digits: the first corresponds to the background, the second to the foreground. Then a list is given with options.

To get a bright white background with red letters: color fc

To go back to a black background with white letters: color 07

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image4.png" style="width:5.5252in;height:4.58888in" />

# Echo

As the people following the Python track are familiar with, the first step is always to print the message “Hello World”. Instead of using the print function, we need to use the echo command in the command prompt.

To get Hello World, type: echo Hello World

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image5.png" style="width:5.625in;height:1.82292in" />

# Knowing where you are

## dir command

In the command prompt, you can go into different folders (also called directories) and navigate your way around. As you can see in the previous screenshots, I am currently in my H drive (H:\\. I want to go into a directory, but I am not sure which directories there are in my H drive. To find out, I use the dir command. This command can be used to display a list of files and subdirectories. When you type in dir /? you get an overview of all the different options available to use with this command. The following are useful:

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Command</strong></th>
<th><strong>Explanation</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>dir</td>
<td>Displays the list of files and subdirectories in a directory.</td>
</tr>
<tr class="even">
<td>dir /B</td>
<td>Uses bare format (no heading information or summary).</td>
</tr>
<tr class="odd">
<td>dir /S</td>
<td>Displays files in specified directory and all subdirectories.</td>
</tr>
<tr class="even">
<td>dir /Q</td>
<td>Display the owner of the file.</td>
</tr>
</tbody>
</table>

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image6.png" style="width:6.3in;height:7.20139in" />

Lets see how they all work. For this demo, I have created a directory with several subdirectories in it: demo\_cmd. Lets try some options of the dir command here.

### dir 

We start by just using the dir command.

<img src="image7.png" style="width:4.66667in;height:2.78125in" />

### dir /B

dir /B gives you the bare format without heading information or summary.

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image8.png" style="width:1.875in;height:1.33333in" />

### dir /S

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image9.png" style="width:5.40625in;height:4.95833in" />

Note that this is not the entire result, just a part of it. As you can see, you get an overview of the subdirectories and the files in it, but it also checks those subdirectories and gives you an overview of that.

### dir /Q

dir /Q also gives you the owner. In my case, this is not very interesting because I created everything. But as archivists, we receive collections from others all the time, so this command could be handy.

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image10.png" style="width:6.10417in;height:2.84375in" />

## Tree command

You could also want a more visual view of the subdirectories and files. Then you can use the tree command.

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image11.png" style="width:3.44792in;height:2.25in" />

However, this does not show the files. It just shows the directories and subdirectories.

# Change directories

As you can see in the previous screenshot I am currently in my H drive in the subdirectory Demo\_cmd. How did I get here? By using the change directories command: cd \[directory you want to go in\]. Cd stands for changing directories.

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image12.png" style="width:1.41667in;height:0.63542in" />

I can also go back by using the cd command, but with the addition of two dots: cd..

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image13.png" style="width:1.44792in;height:0.96875in" />

You can also change drives. I am currently in my H drive, but I also have a C drive. To change drive, you simple type in \[DRIVE\]:. For me, this is: C:

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image14.png" style="width:0.60417in;height:0.6875in" />

# Renaming a file 

In H:\Demo\_cmd\Test I have a file named B.txt.

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image15.png" style="width:4.83333in;height:2.70833in" />

I want to change B.txt to A.txt. I need to rename it. I can do this using the ren command.

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image16.png" style="width:6.3in;height:1.28056in" />

I can change the name by typing in the following: ren \[old name file\] \[new name file\]

In this case: ren B.txt A.txt

I do not need to specify the file path here because it is all happening where I currently am: H:\Demo\_cmd\Test

However, here it is with the file paths included: ren H:\Demo\_cmd\Test\B.txt H:\Demo\_cmd\Test\A.txt

# Making a new directory

If I want to create a new directory in my demo\_cmd I can do this using the mkdir command. To create a new directory I type: mkdir demo\_test

To see if it worked, you can use the dir or tree command again.

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image17.png" style="width:3.5in;height:2.39583in" />

# Copy a file

If I want to copy A.txt (which is in my Test directory) to the new demo\_test directory, I can use the copy command. This leads to the following: copy A.txt H:\Demo\_cmd\demo\_test.

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image18.png" style="width:4.73958in;height:3.1875in" />

# Deleting a file

To delete a file, you can use the del command. However, it is recommended to also add /P to your command. /P gives you a prompt for confirmation before deleting each file. This is useful so you have an extra check built in.

To delete the file I just copied: del /P A.txt

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image19.png" style="width:3.84375in;height:0.83333in" />

In the screenshot you can see the prompt, where I need to type in Y or N for it to do it, or stop it.

# Executing a batch script

A batch script is a series of command to be executed by the command-line interpreter, stored in a plain text file. This is useful if you have a workflow for example. If I want to change the title, change the color, copy a file, and delete a file all in one go without typing these in all the time.

To create a batch script, you simply open your notepad and type in the command (one on each line). Then you save it as a .bat file.

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image20.png" style="width:3.4375in;height:2.57292in" />

After creating this script, I go into the directory where the bat script resides and type in the name of the file: example.bat

This leads to the command prompt doing these command one after the other without me having to type them in individually.

# Executing a Python or HTML script

Executing a Python script is almost the same. You simply go to where the file is and type in the name of the file.

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image21.png" style="width:3.36458in;height:0.8125in" />

You can also execute the file from somewhere else, just do not forget to type in the complete path.

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image22.png" style="width:3.19792in;height:0.47917in" />

For HTML this all works the same. Just type in the file (example: DuckArchive.HTML). With HTML files, this will start up in your browser which automatically gets booted up for you after entering the command.

# Stopping a task

When starting the Jokes.py program or when executing the tree command on your complete H drive (may take it a while), you might want to stop the task. You can of course close the window, but this is of course not the proper way. The proper way is to use ctrl + C.

# Start Wordpad

To start up Wordpad using your command prompt, you simple type write.

# Start Word

For Word, I had to go into my C drive since that is where the program is. To change

I need to access the file Winword.exe. However, just typing this in like we did with Python and HTML files will not suffice. You also need to write start.

To start windows: start winword.exe

# Calculating a checksum

Checksums are values that are generated from transmitted data before and after transmission. They are a sort of fingerprint for your file. If the checksum stays the same, you know the file is the same. If anything has changed, the checksum too will have changed. This can indicate bit rot or an error that happened during migration.

The command to calculate a checksum is certutil -hashfile

Calculate an MD5 checksum: certutil -hashfile \[file name\] MD5

Calculate a SHA512 checksum: certutil -hashfile \[file name\] MD5

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image23.png" style="width:4.51042in;height:0.9375in" />

You can also calculate a checksum on an entire folder using a batch script:

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image24.png" style="width:5.98958in;height:1.72917in" />

Here is a breakdown of the script:

-   **@echo off**

This line turns off the command echoing in the batch script, meaning that commands themselves won’t be printed to the console when they are executed.

-   **for %%f in (H:\Demo\_cmd\literature\\) do (…)**

This line sets up a loop that iterates over each file (%%f) in the directory specified (H:\Demo\_cmd\literature\\. The \* is a wildcard character that matches any file in that directory.

-   **certutil -hashfile "%%f" SHA256**

Within the loop, this command calculates the SHA256 hash value for each file (%%f) found in the directory specified. certutil is a command-line utility that performs various cryptographic operations, including hashing files. -hashfile is an option that tells certutil to hash a specified file. "%%f" is the file being hashed, and SHA256 specifies that the hash algorithm used should be SHA256.

In short, this script goes through each file in the specified directory and calculates its SHA256 hash value using the certutil command.

Note that the certutil command can do a lot more. To see all the options, type certutil /?

# Cleaning the window

If you enter multiple commands, your window can get full and a bit cluttered. To get a clean state, you can use the clean screen command: cls

<img src="https://github.com/Lotte-W/Bits-and-Bots-study-group/blob/main/media/command_prompt_guide/image25.png" style="width:4.78125in;height:2.14583in" />

# Closing the command prompt

To close the command prompt, you can close the window by clicking the x on the top right. But the more correct way is to use the exit command. Simply type exit and the window will close.

# Overview commands

Here are the commands in order of usage in this document.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Command</strong></th>
<th><strong>Explanation</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>title</td>
<td>Sets the window title for the command prompt window.</td>
</tr>
<tr class="even">
<td>color</td>
<td>The color command sets the default console foreground and background colors.</td>
</tr>
<tr class="odd">
<td>echo</td>
<td>Displays messages.</td>
</tr>
<tr class="even">
<td>dir</td>
<td>Displays the list of files and subdirectories in a directory.</td>
</tr>
<tr class="odd">
<td>dir /B</td>
<td>Uses bare format (no heading information or summary).</td>
</tr>
<tr class="even">
<td>dir /S</td>
<td>Displays files in specified directory and all subdirectories.</td>
</tr>
<tr class="odd">
<td>dir /Q</td>
<td>Display the owner of the file.</td>
</tr>
<tr class="even">
<td>tree</td>
<td>Graphically displays the folder structure of a drive or path.</td>
</tr>
<tr class="odd">
<td>ren</td>
<td>Renames a file or files.</td>
</tr>
<tr class="even">
<td>mkdir</td>
<td>Creates a directory.</td>
</tr>
<tr class="odd">
<td>copy</td>
<td>Copies one or more files to another location.</td>
</tr>
<tr class="even">
<td>del</td>
<td>Deletes one or more files.</td>
</tr>
<tr class="odd">
<td>write</td>
<td>Open Wordpad</td>
</tr>
<tr class="even">
<td>cls</td>
<td>Clears the screen.</td>
</tr>
<tr class="odd">
<td>exit</td>
<td></td>
</tr>
</tbody>
</table>

# Overview Windows/Linux/macOS

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 44%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Windows</strong></th>
<th><strong>Linux</strong></th>
<th><strong>macOS</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>title</td>
<td colspan="2">There isn't a direct equivalent, but you can use terminal titles by changing the PS1 variable in your shell configuration file (like .bashrc or .zshrc). For example, you can set export PS1="\[\033]0;Your Title Here\007\]\u@\h:\w\$ " in your .bashrc for Bash.</td>
</tr>
<tr class="even">
<td>color</td>
<td colspan="2">The terminal colors are typically controlled by the terminal emulator rather than by shell commands. You can change terminal colors within the settings of your terminal emulator.</td>
</tr>
<tr class="odd">
<td>echo</td>
<td>echo</td>
<td>echo</td>
</tr>
<tr class="even">
<td>dir</td>
<td>ls</td>
<td>ls</td>
</tr>
<tr class="odd">
<td>dir /B</td>
<td colspan="2">Use ls with the -1 (dash one) option to list files and directories in bare format, each on a new line.</td>
</tr>
<tr class="even">
<td>dir /S</td>
<td colspan="2">Use ls with the -1 (dash one) option to list files and directories in bare format, each on a new line.</td>
</tr>
<tr class="odd">
<td>dir /Q</td>
<td colspan="2">There isn't a direct equivalent for displaying ownership information with ls alone. You can use ls -l to display permissions and ownership details.</td>
</tr>
<tr class="even">
<td>tree</td>
<td colspan="2">You need to install the tree command if it's not already available. On macOS, you can use Homebrew to install it (brew install tree). Once installed, you can use tree to display directory trees.</td>
</tr>
<tr class="odd">
<td>ren</td>
<td colspan="2">Use the mv command to rename files and directories</td>
</tr>
<tr class="even">
<td>mkdir</td>
<td>mkdir</td>
<td>mkdir</td>
</tr>
<tr class="odd">
<td>copy</td>
<td colspan="2">Use the cp command to copy files and directories.</td>
</tr>
<tr class="even">
<td>del</td>
<td colspan="2">Use the rm command to delete files and directories.</td>
</tr>
<tr class="odd">
<td>write</td>
<td colspan="2"><p>In Windows, the write command is used to write directly to a serial port. If you're looking for a similar functionality in macOS/Linux, you can use the echo command in combination with the appropriate device file representing the serial port.</p>
<p>For example, if you want to write to the serial port /dev/ttyS0 (COM1 in Windows), you can use echo like this:</p>
<p>echo "Your message here" &gt; /dev/ttyS0</p>
<p>Replace /dev/ttyS0 with the appropriate device file for your serial port. You might need appropriate permissions to write to the serial port device file, so you may need to use sudo or adjust the permissions accordingly.</p></td>
</tr>
<tr class="even">
<td>cls</td>
<td>clear</td>
<td>clear</td>
</tr>
<tr class="odd">
<td>exit</td>
<td>exit</td>
<td>exit</td>
</tr>
</tbody>
</table>

  [2]: #_Toc164795561
  [1]: #changing-the-title-and-color
  [4]: #echo
  [3]: #knowing-where-you-are
  [5]: #dir-command
  [5]: #dir
  [6]: #dir-b
  [7]: #dir-s
  [8]: #dir-q
  [8]: #tree-command
  [9]: #change-directories
  [9]: #renaming-a-file
  [10]: #making-a-new-directory
  [10]: #copy-a-file
  [11]: #deleting-a-file
  [11]: #executing-a-batch-script
  [12]: #executing-a-python-or-html-script
  [12]: #stopping-a-task
  [13]: #start-wordpad
  [14]: #start-word
  [15]: #calculating-a-checksum
  [13]: #cleaning-the-window
  [14]: #closing-the-command-prompt
  [16]: #overview-commands
  [15]: #overview-windowslinuxmacos
