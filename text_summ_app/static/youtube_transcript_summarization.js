// youtube_transcript_summarization.js

document.addEventListener('DOMContentLoaded', function () {
    const summarizeButton = document.getElementById('youtube-transcript-summarize-button');
    const inputTranscript = document.getElementById('input-transcript');
    const youtubeTranscriptSummaryResult = document.getElementById('youtube-transcript-summary-result');

    summarizeButton.addEventListener('click', () => {
        const transcriptText = inputTranscript.value;

        // Send the transcript text to the server for YouTube transcript summarization
        fetch('/summarize_youtube_transcript', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `input_transcript=${encodeURIComponent(transcriptText)}`,
        })
        .then(response => response.json())
        .then(data => {
            const summary = data.summary;
            youtubeTranscriptSummaryResult.textContent = summary;
            youtubeTranscriptSummaryResult.style.display = 'block';
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
