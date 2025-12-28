import os
import re
import wikipedia


def sanitize_filename(input_string):
    return re.sub(r'^[a-zA-Z0-9]', '_', input_string)


def generate_corpus(search_term="human rights", num_articles=1000, output_dir="all_articles"):
    os.makedirs(output_dir, exist_ok=True)

    articles = []
    search_results = wikipedia.search(search_term, results=num_articles)

    for i, title in enumerate(search_results, 1):
        try:
            page = wikipedia.page(title)
            content = page.content
            articles.append((title, content))

            sanitized = sanitize_filename(title)
            filename = f'{sanitized}.txt'
            filepath = os.path.join(output_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

        except Exception as e:
            print(f"Error processing '{title}': {str(e)}")
            continue
    print(f"\nCompleted! Saved {len(articles)} articles!")


if __name__ == "__main__":
    generate_corpus()