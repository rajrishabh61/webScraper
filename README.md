<h1 align="center">📚 Web Scraper for Books to Scrape</h1>

<p align="center">
  <em>A beginner-friendly project to practice web scraping with Python</em>
</p>

<hr>

<h2>✨ Features</h2>
<ul>
  <li>Scrapes book <b>titles</b>, <b>prices</b>, <b>availability</b>, and product <b>links</b></li>
  <li>Saves extracted data into a <code>CSV</code> file</li>
  <li>Handles duplicate entries to keep data clean</li>
  <li>Can be extended to scrape multiple pages</li>
</ul>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li><b>Python</b></li>
  <li><b>Requests</b> → For fetching web pages</li>
  <li><b>BeautifulSoup</b> → For parsing HTML</li>
  <li><b>CSV</b> → For storing results</li>
</ul>

<h2>🚀 How to Run</h2>
<ol>
  <li>Clone the repository:
    <pre><code>git clone https://github.com/rajrishabh61/webScraper.git</code></pre>
  </li>
  <li>Navigate into the folder:
    <pre><code>cd webScraper</code></pre>
  </li>
  <li>Run the scraper:
    <pre><code>python scraper.py</code></pre>
  </li>
  <li>Check <code>books.csv</code> for your data 🎉</li>
</ol>

<h2>📊 Example Output</h2>
<pre>
Title: A Light in the Attic  
Price: £51.77  
Availability: In stock  
URL: https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html
</pre>

<h2>💡 Future Improvements</h2>
<ul>
  <li>Scrape multiple pages (pagination)</li>
  <li>Export data into Excel or JSON</li>
  <li>Integrate with pandas for data analysis</li>
  <li>Add charts & visualizations for insights</li>
</ul>

<hr>

<p align="center">
  Made with ❤️ using Python | Happy Scraping! 🐍
</p>
