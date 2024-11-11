# Star Wars Characters Fetcher

This script fetches and displays all characters from a specific Star Wars movie using the Star Wars API (SWAPI).

## Requirements

- **Node.js** (version 10.14.x or above)
- **request module**: Install using `npm install request`

## Usage

To run the script, pass the Movie ID as a command-line argument. For example, to get characters from "Return of the Jedi" (Movie ID 3):

```bash
$ ./0-starwars_characters.js 3
```
## How It Works
    The script takes the movie ID as an argument (e.g., 3 for "Return of the Jedi").
    It fetches the movie data from the SWAPI using the movie ID.
    It extracts the URLs of characters from the movie data.
    It makes another request for each character to fetch and print their names

