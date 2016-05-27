# Usage-plan

terminal input:

draid +
- bu [<options>] <location> <location-backup>
	- __options__
	- -c - make change backup, else: overwrite
	- -f - dont keep deleted files
	- -t [n] - keep deleted files for n days (default 30)
	- -l [<path>] - write log to file (append)
	- -d - dry-run
- mv <source> <bu-path> <target>
- rm <target> <bu-path>
- ls-del <bu-path>
- find-missing-bu <dir1> <dir2>
- revive <bu-path> <original>
- keep <n> <bu-path> - keep deleted file in backup for n days from now on
- cleanup <bu-path> - finally delete all deleted files and folders

