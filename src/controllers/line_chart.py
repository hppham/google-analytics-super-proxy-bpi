#!/usr/bin/python2.7


"""Display the public chart.

These handlers are for actions performed by external users that may or may not
be signed in. This is configured in app.yaml. Additional logic is provided by
utility functions.

  PublicQueryResponseHandler: Outputs the API response for the requested query.
  NotAuthorizedHandler: Handles unauthorized requests.
"""

__author__ = 'huy pham'

from controllers import base
from controllers.util import co
import webapp2


class DisplayChart(base.BaseHandler):
  """Redirect to the display_chart page."""

  def get(self):
    self.RenderHtmlTemplate('line_chart.html')


app = webapp2.WSGIApplication(
    [(co.LINKS['line_chart'], DisplayChart)],
    debug=True)
