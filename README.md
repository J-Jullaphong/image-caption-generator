# Image Caption Generator

This is an AI-generated application made for learning the use of AI in development.

## How to Run
1. Clone the repository from GitHub.
    ```
    git clone https://github.com/J-Jullaphong/image-caption-generator.git
    ```
2. Change directory to image-caption-generator.
    ```
    cd image-caption-generator
    ```
3. Create a virtual environment.
   ```
   python -m venv venv
   ```
4. Activate the virtual environment.
   - Linux and macOS
   ```
   source venv/bin/activate 
   ```
   - Windows
   ```
   .\venv\Scripts\activate
   ```
5. Install Dependencies for required python modules.
   ```
   pip install -r requirements.txt
   ```
6. Create a .env file for externalized variables.
   - Linux and macOS
   ```
   cp sample.env .env 
   ```
   - Windows
   ```
   copy sample.env .env
   ```
7. Use a text editor to edit the .env file according to your needs.
   ```
   - HUGGINGFACE_API_KEY
   - UPLOAD_FOLDER
   ```
8. Run the application.
    ```
    python app.py
    ```