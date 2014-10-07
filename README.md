pieTrader
=========

Python Stock Analyzer using Quandl

<h5>pieTrader.config</h5>
<p>
There is an example config located in the project directory.  Rename that file to pieTrader.config.  To get the most out of this you can sign up for a Quandl API key at http://www.quandl.com/users/sign_up
</p>
<p>
The config file also lets you set favorites to analyze.  Enter the symbols separated by commas.
</p>

<h5>pieTrader.py</h5>
<p>
The pieTrader.py file is a command line script for analyzing stocks and any favorites that are setup. To get the most out of this make sure you have a Quandl API Key and favorites setup in the pieTrader.config file.
</p>

<hr>
<h5>Files</h5>
  <ul>
    <li>analyze.py - functions to help analyze stocks and favorites</li>
    <li>dataHandler.py - DataHandler class to handle getting symbols from Quandl</li>
    <li>quandl.py - Quandl class that handles getting JSON data from Quandl and parsing it</li>
    <li>stock.py - Stock class that contains general stock information</li>
    <li>user.py - User class that handles user specific data like favorites</li>
  </ul>

