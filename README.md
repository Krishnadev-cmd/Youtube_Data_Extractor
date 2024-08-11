# YouTube Summary Generator

This is a Streamlit-based web application that extracts the transcript of a YouTube video and generates a concise summary using Google's generative AI.

## Features

- **YouTube URL Input**: Enter a YouTube URL to fetch the video transcript.
- **Automatic Transcript Extraction**: The transcript is automatically extracted using the `youtube_transcript_api`.
- **AI-Powered Summary**: The extracted transcript is summarized into key points within 250 words using Google's generative AI.
- **Thumbnail Display**: The video thumbnail is displayed based on the YouTube video ID.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/youtube-summary-generator.git
    cd youtube-summary-generator
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment variables:**
    - Create a `.env` file in the root directory.
    - Add your Google API key to the `.env` file:
        ```
        GOOGLE_API_KEY=your_google_api_key_here
        ```

## Usage

1. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```
    ![Screenshot (1)](https://github.com/user-attachments/assets/42d119bb-336a-41e4-b58d-2c59cd67a1ff)

2. **Open the app in your web browser.**
    - Enter a YouTube URL and click the "Get Details" button to generate the summary.

## Code Explanation

- **`extract_video_id(url)`**: Extracts the YouTube video ID from different YouTube URL formats.
- **`get_text(video_id)`**: Retrieves the video transcript using the `youtube_transcript_api`.
- **`generate_summary(transcript, prompt)`**: Generates a summary of the transcript using the Google Generative AI model.
- **Streamlit App**:
    - Displays an input box for the YouTube URL.
    - Displays the video thumbnail.
    - Generates and displays the video summary when the "Get Details" button is clicked.
 
      ![Screenshot (2)](https://github.com/user-attachments/assets/47d592ae-e29b-43b1-8abf-db32d3686b3c)

      

## Requirements

- `streamlit`
- `google-generativeai`
- `youtube-transcript-api`
- `python-dotenv`
