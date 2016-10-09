# Google Analytics superProxy BPI

This project is a web app that runs on Google App Engine and built on top of the Google Analytics superProxy web app. It publicly shares our Google Analytics reporting data regarding Daily Active User. And handles authentication, caching, and automatic refreshing.

To view the Public Charts:
- dev:  http://localhost:8080/charts/line_chart
- prod: https://ganalyticsproxy.appspot.com/charts/line_chart

**Quick Links**
- [Video demo](http://www.youtube.com/watch?v=8Or8KIhpsqg) of the
  Google Analytics superProxy
- [Google Analytics superProxy](https://developers.google.com/analytics/solutions/google-analytics-super-proxy)
  on the Google Analytics Developers site.
  - [Managing Users](https://developers.google.com/analytics/solutions/google-analytics-super-proxy#manage-users)
  - [Domain Restrictions](https://developers.google.com/analytics/solutions/google-analytics-super-proxy#domain)
- [Quota Considerations](https://developers.google.com/analytics/solutions/google-analytics-super-proxy#quota)
- [Google Analytics superProxy Forum](https://groups.google.com/forum/#!forum/google-analytics-super-proxy) (Ask questions, share Ideas, and get feedback)

## Feature Highlights
- Public access to your Google Analytics data
- Use the proxy to power your own custom dashboards
- Convert to CSV, Data Table, TSV
- Relative dates are supported (e.g. last 7 days)
- Automatically refreshes report data
- Caching - fast responses and efficient quota usage