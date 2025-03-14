import requests
import json
import re
from typing import Optional

# API Keys (replace these with your actual keys)
SEARCHAPI_KEY = ""
OPENAI_API_KEY = ""

def extract_video_id(url: str) -> Optional[str]:
    """Extract the video ID from a YouTube URL."""
    # Regular expressions to match various YouTube URL formats
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11}).*',  # Standard YouTube URLs
        r'(?:embed\/)([0-9A-Za-z_-]{11})',  # Embedded URLs
        r'(?:youtu\.be\/)([0-9A-Za-z_-]{11})'  # Shortened youtu.be URLs
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    # If the input is already just a video ID (11 characters)
    if re.match(r'^[0-9A-Za-z_-]{11}$', url):
        return url
    
    return None

def get_transcript(video_id: str) -> Optional[str]:
    """Get the transcript of a YouTube video using SearchAPI.io."""
    url = "https://www.searchapi.io/api/v1/search"
    
    params = {
        "engine": "youtube_transcripts",
        "video_id": video_id,
        "api_key": SEARCHAPI_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        # Check for errors
        if "error" in data:
            print(f"Error: {data['error']}")
            if "available_languages" in data:
                print("Available languages:")
                for lang in data["available_languages"]:
                    print(f"- {lang['name']} ({lang['lang']})")
            return None
        
        # Extract transcript
        transcript = ""
        for item in data.get("transcript", []):
            transcript += item.get("text", "") + " "
        
        return transcript.strip()
    
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def summarize_with_openai(transcript: str) -> Optional[str]:
    """Summarize the transcript using OpenAI's GPT-4o model."""
    import openai
    
    openai.api_key = OPENAI_API_KEY
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes YouTube video transcripts into concise bullet points. Focus on the main ideas and key takeaways."},
                {"role": "user", "content": f"Please summarize the following YouTube video transcript into bullet points:\n\n{transcript}"}
            ],
            max_tokens=1000
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error summarizing transcript: {e}")
        return None

def main():
    # Get video URL or ID from user
    video_input = input("Enter YouTube video URL or ID (default: 0e3GPea1Tyg): ").strip() or "0e3GPea1Tyg"
    
    # Extract video ID
    video_id = extract_video_id(video_input)
    if not video_id:
        print("Invalid YouTube URL or video ID.")
        return
    
    print(f"Fetching transcript for video ID: {video_id}")
    
    # Get transcript
    transcript = get_transcript(video_id)
    if not transcript:
        print("Failed to get transcript.")
        return
    
    print("\nTranscript fetched successfully!")
    print(f"Transcript length: {len(transcript)} characters")
    
    # Summarize transcript
    print("\nSummarizing transcript with OpenAI GPT-4o...")
    summary = summarize_with_openai(transcript)
    
    if not summary:
        print("Failed to summarize transcript.")
        return
    
    # Print summary
    print("\n--- BULLET POINT SUMMARY ---\n")
    print(summary)
    print("\n---------------------------")

if __name__ == "__main__":
    main()
