from google_play_scraper import app, reviews
# Define the package name (e.g., for the Google Maps app)
package_name = "com.google.android.apps.maps"
app_info = app(package_name)
app_title = app_info['title']
app_url = app_info['url']

print(f"App Title: {app_title}")
print(f"App URL: {app_url}")

review_count = input()
app_reviews = reviews(package_name, lang='en', count=review_count)

for review in app_reviews:
    print(f"Review ID: {review['reviewId']}")
    print(f"User: {review['userName']}")
    print(f"Rating: {review['score']}")
    print(f"Review: {review['content']}")
    print()

