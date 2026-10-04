export async function onRequest(context) {
  const url = new URL(context.request.url);
  const backendOrigin = "https://acp-plausible-tracking.acp-authentic-content-pilot.com";
  const targetUrl = backendOrigin + url.pathname + url.search;

  if (context.request.method === "OPTIONS") {
    return new Response(null, {
      status: 204,
      headers: {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Authorization",
        "Access-Control-Max-Age": "86400"
      }
    });
  }

  const reqInit = {
    method: context.request.method,
    headers: context.request.headers,
    redirect: "follow"
  };

  if (context.request.method !== "GET" && context.request.method !== "HEAD") {
    reqInit.body = context.request.body;
  }

  try {
    const upstreamResponse = await fetch(targetUrl, reqInit);
    const newHeaders = new Headers(upstreamResponse.headers);
    newHeaders.set("Access-Control-Allow-Origin", "*");
    newHeaders.set("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
    newHeaders.set("Access-Control-Allow-Headers", "Content-Type, Authorization");
    
    return new Response(upstreamResponse.body, {
      status: upstreamResponse.status,
      statusText: upstreamResponse.statusText,
      headers: newHeaders
    });
  } catch (err) {
    return new Response(JSON.stringify({ ok: false, error: err.message }), {
      status: 502,
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
      }
    });
  }
}
