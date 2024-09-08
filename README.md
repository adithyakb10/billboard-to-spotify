# Billboard-To-Spotify

This project scrapes the Billboard Top 100 songs for a given year and creates a Spotify playlist containing all those songs using Python. It leverages BeautifulSoup for web scraping and Spotipy for interacting with the Spotify API.

## Features

- Scrapes the Billboard Top 100 chart for a specified year.
- Creates a Spotify playlist with all the scraped songs.
- Utilizes BeautifulSoup for web scraping.
- Uses Spotipy to interact with the Spotify API.

## Requirements

- Python 3.6+
- `beautifulsoup4` library
- `requests` library
- `spotipy` library

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/adithyakb10/billboard-to-spotify.git
   cd billboard-to-spotify
   ```

2. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the root directory of the project with the following environment variables:

   ```
   SPOTIPY_CLIENT_ID=your_spotify_client_id
   SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
   SPOTIPY_REDIRECT_URI=your_spotify_redirect_uri
   ```

   Replace `your_spotify_client_id`, `your_spotify_client_secret`, and `your_spotify_redirect_uri` with your actual Spotify API credentials.

   For obtaining the CLIENT_ID and CLIENT_SECRET, create an app in https://developer.spotify.com/

   The REDIRECT_URI can be localhost for development. Ex: http://localhost:8888/callback

5. **Run the script:**

   ```bash
   python main.py
   ```

   The script will prompt you to enter the year for which you want to scrape the Billboard Top 100 chart and create a Spotify playlist.

## How It Works

1. **Scraping Billboard Top 100:**

   The script uses BeautifulSoup to scrape the Billboard Top 100 chart from a specific year. It extracts the song titles and artist names from the Billboard website.

2. **Creating a Spotify Playlist:**

   Using Spotipy, the script creates a new playlist on Spotify and adds the scraped songs to it. You'll need to authenticate with Spotify to allow the script to access your Spotify account.

## Contributing

Feel free to open issues or submit pull requests if you find bugs or want to add new features. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for web scraping.
- [Spotipy](https://spotipy.readthedocs.io/en/2.20.0/) for Spotify API integration.
- [Billboard](https://www.billboard.com/charts/) for the charts data.

---

Let me know if you need any more details or adjustments!
