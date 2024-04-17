# Sentiment Analysis and Text Metrics Extraction

This repository contains a Python script for performing sentiment analysis and extracting text metrics from a set of URLs using Python's `newspaper`, `pandas`, and `numpy` libraries.

## Installation

To run the script, you'll need to have Python installed on your system along with the required libraries. You can install the necessary libraries using pip:

```
pip install pandas newspaper3k numpy
```


## Usage

1. Make sure you have your input data prepared in an Excel file (`Input.xlsx`). The Excel file should contain a column named `URL` containing the URLs to analyze.

2. Create three text files:
   - `stopwords.txt`: containing a list of stopwords
   - `positive-words.txt`: containing a list of positive words
   - `negative-words.txt`: containing a list of negative words

3. Run the Python script `sentiment_analysis.py`. This script will:
   - Download articles from the provided URLs.
   - Perform sentiment analysis on the articles.
   - Extract various text metrics.

4. The output will be saved to an Excel file named `output.xlsx`.

## Files

- `sentiment_analysis.py`: Python script for sentiment analysis and text metrics extraction.
- `Input.xlsx`: Sample input data.
- `stopwords.txt`: List of stopwords.
- `positive-words.txt`: List of positive words.
- `negative-words.txt`: List of negative words.
- `output.xlsx`: Output Excel file containing sentiment analysis results and text metrics.

## Example

Here's how to use the script:

```python
python sentiment_analysis.py
```

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
