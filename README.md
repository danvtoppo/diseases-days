# Clinical Trial Gap Analyzer

A monitoring tool that parses **ClinicalTrials.gov** RSS feeds to detect periods of research inactivity. This script identifies if there are gaps in medical publications that exceed a user-defined number of days.

## Stack
* **Language:** Python
* **Libraries:** * `BeautifulSoup4`: XML parsing and data extraction.
    * `requests`: Handling HTTP requests to the ClinicalTrials.gov API.
    * `datetime`: Calculating time deltas between publication dates.

## Logic
The script performs a Gap Analysis on time-series data:
1. **Fetch:** Retrieves a live XML feed of clinical trials based on a specific condition.
2. **Parse:** Extracts all `<pubDate>` tags and converts them into Python `datetime` objects.
3. **Sort:** Organizes all publications chronologically.
4. **Calculate:** Iterates through the timeline to find the difference between consecutive dates:
   $$\Delta t = Date_{n+1} - Date_{n}$$
5. **Evaluate:** Returns `True` if any $\Delta t$ is greater than the specified `num_days` threshold.
