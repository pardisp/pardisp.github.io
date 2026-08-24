/* ==========================================================================
   analytics.js: privacy-friendly page counting via GoatCounter
   --------------------------------------------------------------------------
   Dashboard: https://pardisp.goatcounter.com  (log in to view stats)

   GoatCounter sets no cookies and stores no personal data, so this needs no
   cookie-consent banner. See https://www.goatcounter.com/help/privacy

   OPTIONAL. To show the "N views" line in the footer:
     In GoatCounter, go to Settings -> "Site settings" and enable
     "Allow adding visitor counts to your website". Without that setting the
     count endpoint is not public and the footer line just stays hidden.
   ========================================================================== */

(function () {
  "use strict";

  var GOATCOUNTER_CODE = "pardisp";

  if (!GOATCOUNTER_CODE) return;

  // Don't count local development traffic.
  var host = window.location.hostname;
  if (host === "localhost" || host === "127.0.0.1" || host === "") {
    return;
  }

  var endpoint = "https://" + GOATCOUNTER_CODE + ".goatcounter.com";

  // --- 1. Record the pageview -------------------------------------------
  var s = document.createElement("script");
  s.async = true;
  s.src = "//gc.zgo.at/count.js";
  s.setAttribute("data-goatcounter", endpoint + "/count");
  document.head.appendChild(s);

  // --- 2. Show the count in the footer, if the element exists -----------
  var el = document.querySelector(".view-count");
  if (!el || !window.fetch) return;

  var path = window.location.pathname || "/";
  var url =
    endpoint + "/counter/" + encodeURIComponent(path) + ".json";

  fetch(url)
    .then(function (r) {
      if (!r.ok) throw new Error("counter unavailable");
      return r.json();
    })
    .then(function (data) {
      if (!data || !data.count) return;
      el.textContent = data.count + " views";
      el.hidden = false;
    })
    .catch(function () {
      /* Counter not public or offline, so leave the footer line hidden. */
    });
})();
