# tmdb-cli-tool
 A simple command line interface (CLI) to fetch data from The Movie Database (TMDB) and display it in the terminal, such as "Now Playing Movies", "Popular Movies, "Top Rated Movies", "Upcoming Movies".

https://roadmap.sh/projects/tmdb-cli

# TMDB Command Line Interface (CLI) Application

This project implements a simple Command Line Interface (CLI) application that fetches and displays movie data from The Movie Database (TMDB). The user can query the application to fetch popular, top-rated, upcoming, or now playing movies by specifying the movie type via command-line arguments.

## Features

- Fetch data for **Now Playing**, **Popular**, **Top Rated**, and **Upcoming** movies from the TMDB API.
- Display movie information such as the title, release date, and overview in the terminal.
- Handle potential errors such as API failures or network issues.

## Requirements

- Python 3.6 or higher
- Internet connection (for API requests)
- TMDB API Key (you can get your key [here](https://www.themoviedb.org/settings/api))

## Installation

1. **Clone the repository:**

    ```
    git clone https://github.com/yourusername/tmdb-cli.git
    cd tmdb-cli
    ```

2. **Install the required dependencies:**

    Ensure you have Python 3.6 or higher installed, and then install the necessary Python packages:

    ```
    pip install requests
    ```

3. **Set up your TMDB API key:**

    To interact with the TMDB API, you need to add your API key. You can do this by setting an environment variable or by directly modifying the code.

    - **Option 1:** Set the API key as an environment variable:

        ```
        export TMDB_API_KEY="your_tmdb_api_key"   # On Windows use: set TMDB_API_KEY=your_tmdb_api_key
        ```

    - **Option 2:** Modify the code (not recommended for security reasons) to hardcode the API key directly into the script.

## Usage

Once you have set up the project and installed the dependencies, you can run the CLI tool to fetch movie data by specifying the movie type.

### Available Commands:

- `playing`: Fetches currently playing movies.
- `popular`: Fetches popular movies.
- `top`: Fetches top-rated movies.
- `upcoming`: Fetches upcoming movies.

### Example Commands:

1. **To view now playing movies:**

    ```
    python tmdb-app.py --type "playing"
    ```

2. **To view popular movies:**

    ```
    python tmdb-app.py --type "popular"
    ```

3. **To view top-rated movies:**

    ```
    python tmdb-app.py --type "top"
    ```

4. **To view upcoming movies:**

    ```
    python tmdb-app.py --type "upcoming"
    ```
