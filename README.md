# bunny3

bunny3 is a Python3 rewrite of [bunny1](https://github.com/ccheever/bunny1), the smart bookmarks/search engine originally developed at Facebook. You might also consider checking out alternatives like [jack_bunny](https://github.com/jackyang127/jack_bunny) and [rusty-bunny](https://github.com/fbsamples/rusty-bunny).

This project is targetted for personal use to be ran locally, and may be expanded to a client-server model in the future.

## To install

1. `git clone https://github.com/mattwhatkins/bunny3.git`
2. `cd bunny3`
3. Optional (But recommended): Configure a virtualenv or similar and activate
4. `pip install -r requirements.txt`
5. `python3 -m bunny3.bunny`

## To do
*(Some rough notes capturing what's planned)*
* WWW
  * Cleanup/format help.html
  * Test for flask vulns
  * Migrate to production flask
* Python
  * Add typing
  * Expand unit tests for DB etc
  * Logging and error checking
  * Setup CI etc
* Commands
  * Build collection of different command sets