# Phi Data Multi-Model Diet Agent

This project implements a nutrition agent using the PhiData framework. The agent has knowledge of products, uses an LLM model to process data and respond, and has storage memory to remember conversations.

## Features

- **Knowledge Base Creation**: The knowledge data is passed as a CSV file within the project. This data is stored in a PostgreSQL database running in a Docker container. The data is stored in an embedded format, and queries are also embedded before the search by the LLM. The Gemini model is used as both the embedding system and the LLM model. The search type is hybrid, allowing for flexible response generation.
- **Model**: The model takes the knowledge and provides responses based on the input queries.
- **User Interaction**: The agent can generate personalized diet plans based on user input, incorporating products from the knowledge base.

## Setup

1. **Clone the repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a [.env](http://_vscodecontentref_/1) file in the root directory.
    - Add the following environment variables:
        ```
        GOOGLE_API_KEY=<your-google-api-key>
        ```

5. **Set up PostgreSQL database**:
    - Create a PostgreSQL database and user with the necessary permissions.
    - Update the [db_url](http://_vscodecontentref_/2) in the code with your PostgreSQL credentials.

## Running the Application

1. **Run the CSV UI Agent**:
    ```sh
    python csv_uiagent.py
    ```

2. **Run the FreshApp**:
    ```sh
    python freshapp.py
    ```

3. **Run the Main Application**:
    ```sh
    python app.py
    ```

## Files

- [csv_uiagent.py](http://_vscodecontentref_/3): Sets up the CSV UI agent.
- [freshapp.py](http://_vscodecontentref_/4): Collects user details and generates a diet plan.
- [app.py](http://_vscodecontentref_/5): Main application script.
- [train.py](http://_vscodecontentref_/6): Contains system prompts and instructions for the agent.
- [product.csv](http://_vscodecontentref_/7): List of products used in the knowledge base.
- [requirements.txt](http://_vscodecontentref_/8): List of dependencies.
- [.gitignore](http://_vscodecontentref_/9): Specifies files and directories to be ignored by Git.

## Notes

- Ensure that the PostgreSQL database is running and accessible.
- Run `phi auth` in the terminal for authentication before accessing the PhiData UI.

## License

This project is licensed under the MIT License.