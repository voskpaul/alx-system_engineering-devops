## 0x02-shell_redirections
Repository covering the basics in shell redirections and the various commands involved.  
Included are some scripts that demonstrate how they all work.

### 0-hello_world
> A script that prints “Hello, World”, followed by a new line to the standard output.

### 1-confused_smiley
> A script that displays a confused smiley "(Ôo)'.

### 2-hellofile
> A script that displays the content of the /etc/passwd file.

### 3-twofiles
> A script that displays the content of /etc/passwd and /etc/hosts

### 4-lastlines
> A script that displays the last 10 lines of /etc/passwd

### 5-firstlines
> A script that displays the first 10 lines of /etc/passwd

### 6-third_line
> A script that displays the third line of the file `iacta`.
> * The file `iacta` will be in the working directory
> * You’re not allowed to use `sed`

### 7-file
> A shell script that creates a file named exactly `\*\\'"Holberton School"\'\\*$\?\*\*\*\*\*:)`  
> containing the text `Holberton School` ending by a new line.

### 8-cwd_state
> A script that writes into the file `ls_cwd_content` the result of the command `ls -la`.  
> If the file `ls_cwd_content` already exists, it should be overwritten.  
> If the file `ls_cwd_content` does not exist, create it.

### 9-duplicate_last_line
> A script that duplicates the last line of the file `iacta`
> * The file `iacta` will be in the working directory

### 10-no_more_js
> A script that deletes all the regular files (not the directories) with a `.js` extension  
> that are present in the current directory and all its subfolders.

### 11-directories
> A script that counts the number of directories and sub-directories in the current directory.
> * The current and parent directories should not be taken into account
> * Hidden directories should be counted

### 12-newest_files
> A script that displays the 10 newest files in the current directory.
> * Requirements:
>   * One file per line
>   * Sorted from the newest to the oldest

### 13-unique
> A script that takes a list of words as input and prints only words that appear exactly once.
> * Input format: One line, one word
> * Output format: One line, one word
> * Words should be sorted

### 14-findthatword
> A script that displays lines containing the pattern “root” from the file `/etc/passwd`

### 15-countthatword
> A script displays the number of lines that contain the pattern “bin” in the file `/etc/passwd`

### 16-whatsnext
> A script that displays lines containing the pattern “root” and 3 lines after them in the file `/etc/passwd`.

### 17-hidethisword
> A script that displays all the lines in the file `/etc/passwd` that do not contain the pattern “bin”.

### 18-letteronly
> A script that displays all lines of the file `/etc/ssh/sshd_config` starting with a letter.
> * include capital letters as well

### 19-AZ
> A script that replaces all characters `A` and `c` from input to `Z` and `e` respectively.

### 20-hiago
> A script that removes all letters `c` and `C` from input.

### 21-reverse
> A script that reverse its input.

### 22-users_and_homes
> A script that displays all users and their home directories, sorted by users.
> * Based on the the `/etc/passwd` file
