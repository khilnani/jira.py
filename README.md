## jira.py

A python script to parse clipboard or shared text for jira ids
and then output key info for that jira ticket instantly.

While designed for the iOS [Pythonista](http://omz-software.com/pythonista/) application, the script runs on any linux/mac os environment.

### Configuration

- Rename `jira.sample.conf` to `jira.conf` and update values

### Usage

iOS / Pythonista
- In any app, use App Share, Run in Pythonista and then select this script.
- Copy text with a Jira ID in it, and run this script in Pythonista.

Linux/Mac OS
- Run this script in a linux/os x terminal with the JIRA ID as a command line arg
    - eg. `python jira.py ST-1222`

## Installation

- Download or clone the github repo, or:
  - Pythonista console: `import urllib2; exec urllib2.urlopen('http://khl.io/jira-py').read()`
  - Linux/Mac OS Terminal: `python -c "import urllib2; exec urllib2.urlopen('http://khl.io/jira-py').read()"`
