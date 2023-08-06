========================================================================
                         KETER PORT SCANNER
========================================================================

DESCRIPTION:

Keter Port Scanner is a simple yet powerful tool that allows you to scan a range of ports on a given target host to identify which ports are open. Additionally, it provides the WhoIs details of the target host. The tool uses multi-threading to enhance the scanning speed.

FEATURES:

1. Fast multi-threaded port scanning.
2. Fetches and displays WhoIs details of the target.
3. Interactive user input for selecting target and port range.
4. Neatly formatted output with progress bar.
5. ASCII art header for aesthetics.

USAGE:

1. Run the script.
2. Enter the target host address when prompted.
3. Enter the starting port for scanning.
4. Enter the ending port for scanning.
5. Wait for the scanner to complete the scan and display results.

SYSTEM REQUIREMENTS:

1. Python 3.6 or above.
2. Internet connection (for fetching WhoIs details).
3. Only tested on Windows (may work on other OS, but not officially supported).

DEPENDENCIES:

1. socket module (built-in with Python).
2. datetime module (built-in with Python).
3. os module (built-in with Python).
4. whois module (external) - Install via pip:
   pip install python-whois
5. concurrent.futures module (built-in with Python).

CREDITS:

Developed by Noah Vesenjak-Dolinsek / KETER-Software
For feedback and bug reports, please contact: noah.vesenjak@gmail.com 

LICENSE:

This software is provided "as is" without warranty of any kind. You are free to modify and distribute it as long as credit is given to the original author.

========================================================================
