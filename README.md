## jira.py

Python scripts to help improve Jira interactions

While designed for the iOS [Pythonista](http://omz-software.com/pythonista/) application, the scripts runs on any linux/mac os environment.

### `jira.py`

Extract Jira ID from clipboard or shared text or command line arg,
and then output summary info for that jira ticket instantly.

### `jira-id.py`

Extract Jira ID from clipboard or shared text or command line arg,
and launch a browser with the URL to the Jira issue.

#### Mac OS Equivalent

- Launch `/Applications/Automator`
- Create a new document of type *Service*
    - Save as something indicator, eg `jira-id` (be a bit more creative)
        - The script will be saved to `/Users/USERNAME/Library/Services/jira-id.workflow`
    - Configure (top ot the screen) to be: Service recieves selected `text` in `any application`
- Add the following workflow actions
    - *Text - Ask for Test* - Optional
        - Customize the prompt to something like 'Text with Jira id'
    - *Utilities - Run JavaScript*
        - Use the JavScript below to extracxt a Jira ID from text
	```
function run(input, parameters) {
	var re = new RegExp('([a-zA-Z]+-[0-9]+)');
	var items = re.exec(input);
	if (!items) {
		return input;
	} else {
		return 'https://jira.com/browse/' + items[0];
	}
	return input;
}
	```
    - *Internet - Display Webpages*
- Launch `System Preferences` and navigate to `Keyboard` / `Shortcuts`
- Under `Services` locate your Service in the `Text` category
- Assign a keyboard shortcut.


## Configuration

- Rename `jira.sample.conf` to `jira.conf` and update values

## Instructions

iOS / Pythonista
- In any app, use App Share, Run in Pythonista and then select this script.
- Copy text with a Jira ID in it, and run this script in Pythonista.

Linux/Mac OS
- Run this script in a linux/os x terminal with the JIRA ID as a command line arg
    - eg. `python jira.py ST-1222`

Installation

- Download or clone the github repo, or:
  - Pythonista console: `import urllib2; exec urllib2.urlopen('http://khl.io/jira-py').read()`
  - Linux/Mac OS Terminal: `python -c "import urllib2; exec urllib2.urlopen('http://khl.io/jira-py').read()"`

### `jira-id.py`

https://github.com/khilnani/jira.py
