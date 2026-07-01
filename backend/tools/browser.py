import webbrowser
import urllib.parse


class BrowserTool:

    @staticmethod
    def execute(parameters):

        action = parameters.get("action")

        if action == "open_url":

            url = parameters.get("url")

            if not url.startswith("http"):
                url = "https://" + url

            webbrowser.open(url)

            return f"Opening {url}"

        if action == "google_search":

            query = urllib.parse.quote(parameters.get("query"))

            webbrowser.open(
                f"https://www.google.com/search?q={query}"
            )

            return f"Searching Google for {parameters.get('query')}"

        if action == "youtube_search":

            query = urllib.parse.quote(parameters.get("query"))

            webbrowser.open(
                f"https://www.youtube.com/results?search_query={query}"
            )

            return f"Searching YouTube for {parameters.get('query')}"

        return "Unknown browser action."