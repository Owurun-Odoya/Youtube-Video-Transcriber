# YouTube Video to Bullet Point Summary

This Python script extracts the transcript from a YouTube video and uses OpenAI's GPT-4o model to generate a concise bullet point summary.

## Prerequisites

- Python 3.6 or higher
- API keys for:
  - [SearchAPI.io](https://www.searchapi.io/) - For extracting YouTube transcripts
  - [OpenAI](https://platform.openai.com/) - For generating summaries with GPT-4o

## Installation

1. Install the required Python packages:

```bash
pip install requests openai
```

2. Open `youtube_summarizer.py` and replace the placeholder API keys with your actual keys:

```python
# Replace these with your actual keys
SEARCHAPI_KEY = "your_searchapi_key_here"
OPENAI_API_KEY = "your_openai_api_key_here"
```

## Usage

Run the script from the command line:

```bash
python youtube_summarizer.py
```

The script will:
1. Prompt you to enter a YouTube video URL or ID (defaults to "0e3GPea1Tyg" if none provided)
2. Extract the transcript using SearchAPI.io
3. Summarize the transcript using OpenAI's GPT-4o model
4. Print the bullet point summary to the terminal

## Example

```
Enter YouTube video URL or ID (default: 0e3GPea1Tyg): https://www.youtube.com/watch?v=dQw4w9WgXcQ
Fetching transcript for video ID: dQw4w9WgXcQ

Transcript fetched successfully!
Transcript length: 1234 characters

Summarizing transcript with OpenAI GPT-4o...

--- BULLET POINT SUMMARY ---

• Bullet point 1
• Bullet point 2
• Bullet point 3
...

---------------------------
```

## Troubleshooting

- If you get an error about missing transcripts, the video might not have captions available.
- If you encounter API rate limits, you may need to wait before making additional requests.
- Make sure your API keys are correctly entered in the script.
