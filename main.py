from flask import Flask, jsonify, request
from controller import *
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)
base_url = 'https://courtingthelaw.com/category/news-events'


@app.route('/get_news', methods=['GET'])
def scrape():
    try:
        num_pages = request.args.get('num_pages', default=1, type=int)
        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=10, type=int)

        with ThreadPoolExecutor(max_workers=5) as executor:
            urls = [f'{base_url}/page/{page_num}/' for page_num in range(1, num_pages + 1)]
            results = executor.map(scrape_page, urls)
            all_articles = []

            for result in results:
                all_articles.extend(result)

        total_count = len(all_articles)
        start_index = (page - 1) * per_page
        end_index = start_index + per_page
        paginated_articles = all_articles[start_index:end_index]

        return jsonify({
            'total_pages': len(all_articles) // per_page + 1,
            'total_count': total_count,
            'current_page': page,
            'per_page': per_page,
            'articles': paginated_articles
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
