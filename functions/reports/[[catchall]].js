export async function onRequest(context) {
  const url = new URL(context.request.url);
  const assetResponse = await context.env.ASSETS.fetch(context.request);
  
  if (url.pathname.endsWith('.pdf')) {
    const newHeaders = new Headers(assetResponse.headers);
    newHeaders.set('Content-Type', 'application/pdf');
    newHeaders.set('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0');
    return new Response(assetResponse.body, {
      status: assetResponse.status,
      headers: newHeaders
    });
  }
  
  return assetResponse;
}
