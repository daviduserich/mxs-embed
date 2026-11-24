const ALLOWED_ORIGIN_RE = /^https:\/\/([a-z0-9-]+\.)?(magnet-xs\.ch|magnet-xs\.com|pages\.dev|acp-authentic-content-pilot\.com)$|^http:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/i;

function applyCorsHeaders(headers, reqOrigin) {
  if (reqOrigin && ALLOWED_ORIGIN_RE.test(reqOrigin)) {
    headers.set("Access-Control-Allow-Origin", reqOrigin);
    headers.set("Access-Control-Allow-Credentials", "true");
    headers.append("Vary", "Origin");
  } else {
    headers.set("Access-Control-Allow-Origin", "*");
  }
  headers.set("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS");
  headers.set("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Partner-Token, X-WebPilot-Relay-Key, X-Boardroom-Key");
}

export async function onRequest(context) {
  const url = new URL(context.request.url);
  const reqOrigin = (context.request.headers.get("Origin") || "").trim();
  const backendOrigin = "https://acp-plausible-tracking.acp-authentic-content-pilot.com";
  let forwardPath = url.pathname;
  if (
    forwardPath.startsWith("/api/auth/") ||
    forwardPath.startsWith("/api/lead-") ||
    forwardPath.startsWith("/api/webpilot/") ||
    forwardPath.startsWith("/api/team-") ||
    forwardPath.startsWith("/api/cockpit/")
  ) {
    forwardPath = forwardPath.replace(/^\/api\//, "/api/publish-career/");
  }
  const targetUrl = backendOrigin + forwardPath + url.search;

  if (context.request.method === "OPTIONS") {
    const optHeaders = new Headers({ "Access-Control-Max-Age": "86400" });
    applyCorsHeaders(optHeaders, reqOrigin);
    return new Response(null, { status: 204, headers: optHeaders });
  }

  const forwardHeaders = new Headers(context.request.headers);
  forwardHeaders.set("X-Forwarded-Host", url.hostname);
  forwardHeaders.set("X-Forwarded-Proto", url.protocol.replace(":", ""));

  const reqInit = {
    method: context.request.method,
    headers: forwardHeaders,
    redirect: "follow"
  };

  if (context.request.method !== "GET" && context.request.method !== "HEAD") {
    reqInit.body = context.request.body;
  }

  try {
    const upstreamResponse = await fetch(targetUrl, reqInit);
    const newHeaders = new Headers(upstreamResponse.headers);
    applyCorsHeaders(newHeaders, reqOrigin);

    return new Response(upstreamResponse.body, {
      status: upstreamResponse.status,
      statusText: upstreamResponse.statusText,
      headers: newHeaders
    });
  } catch (err) {
    const errHeaders = new Headers({ "Content-Type": "application/json" });
    applyCorsHeaders(errHeaders, reqOrigin);
    return new Response(JSON.stringify({ ok: false, error: err.message }), {
      status: 502,
      headers: errHeaders
    });
  }
}
