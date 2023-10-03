# Text Summarization

## Description

Text Summarization is a web application that provides an automated way to generate summaries of input text. It leverages natural language processing (NLP) techniques to extract essential information from lengthy documents, making it easier for users to grasp the main ideas and key points.

The application is built using Flask for the backend and HTML/CSS for the frontend. It uses the spaCy library for NLP processing to perform text summarization.

## Features

- Input a piece of text in a user-friendly interface.
- Click the "Submit" button to generate a summary.
- View the original text and its summary side by side.
- See the word count of the original text and summary.
- Customize the level of summarization by adjusting the percentage of sentences included.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/Text-Summarization.git
   cd Text-Summarization
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the application:

   ```bash
   python app.py
   ```

6. Open a web browser and go to [http://localhost:5000](http://localhost:5000) to use the application.

## Usage

1. Enter or paste your text into the input field on the home page.
2. Click the "Submit" button to generate a summary.
3. View the original text and summary on the summary page.
4. You can adjust the level of summarization by changing the percentage of sentences included in the summary. This can be done by modifying the `select_len` variable in `text_summary.py`.

## Credits

This project was created by MAJJIGA JASWANTH and is based on the Flask web framework and spaCy NLP library.

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Replace `[Your Name]` with your actual name, and make sure to create a `LICENSE` file in your repository with the appropriate license text.

Feel free to customize and expand this `README.md` to include any additional information about your project, such as troubleshooting tips or future enhancements. Once you've created your `README.md` file, you can commit and push it to your GitHub repository.
