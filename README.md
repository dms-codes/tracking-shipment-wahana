# Wahana Tracking Script

This Python script allows you to track a Wahana shipment by providing its tracking number. It scrapes the tracking information from the Wahana website and displays the sender's and recipient's details, as well as the shipment's current status.

## Features

- Tracks Wahana shipments using a tracking number.
- Retrieves sender and recipient information.
- Displays the current status of the shipment.
- Provides a simple command-line interface for tracking.

## Prerequisites

Before running the script, make sure you have the following Python libraries installed:

- `requests`: To make HTTP requests.
- `BeautifulSoup`: For web scraping.

You can install these libraries using `pip`:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Modify the script to specify the `NORESI` variable with your Wahana tracking number.

2. Run the script by executing the following command in your terminal:

```bash
python your_script_name.py
```

3. The script will fetch the tracking information from the Wahana website for the provided tracking number.

4. It will then display the sender's and recipient's details, as well as the current status of the shipment.

## Configuration

- `URL`: The base URL of the Wahana tracking page.
- `NORESI`: The Wahana tracking number you want to track.
- `NUMCHR`: The number of characters to print as separators.
- `CHAR`: The character used for separators.
- Other settings in the script can be customized as needed.

## Example

Suppose you want to track a Wahana shipment with the tracking number '187TNBLM.' After running the script, you will see the tracking details displayed in the terminal.

## License

This script is provided under the [MIT License](LICENSE).
```

Replace `"your_script_name.py"` with the actual name of your script. You can also add more details to the README.md file, such as installation instructions and additional usage examples, based on your project's specific needs.
