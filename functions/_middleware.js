export async function onRequest(context) {
  const url = new URL(context.request.url);
  const hostname = url.hostname.toLowerCase();

  // 1. Hostname: webpilot.magnet-xs.ch
  if (hostname.startsWith('webpilot.')) {
    // If not already accessing /webpilot path internally
    if (!url.pathname.startsWith('/webpilot')) {
      let targetPath = url.pathname;
      if (targetPath === '/' || targetPath === '') {
        targetPath = '/webpilot/index.html';
      } else if (!targetPath.includes('.')) {
        // e.g. /ueber-uns -> /webpilot/ueber-uns.html
        targetPath = `/webpilot${targetPath}.html`;
      } else {
        targetPath = `/webpilot${targetPath}`;
      }

      const rewriteUrl = new URL(targetPath, url.origin);
      rewriteUrl.search = url.search;
      return context.env.ASSETS.fetch(new Request(rewriteUrl, context.request));
    }
  }

  // 2. Hostname: vorschau.magnet-xs.ch
  if (hostname.startsWith('vorschau.')) {
    // Match /hiltbrand or /hiltbrand/...
    if (url.pathname.startsWith('/hiltbrand')) {
      let rest = url.pathname.replace(/^\/hiltbrand\/?/, '');
      if (rest === '' || rest === '/') {
        rest = 'index.html';
      } else if (!rest.includes('.')) {
        rest = `${rest}.html`;
      }
      const targetPath = `/preview-hiltbrand/${rest}`;
      const rewriteUrl = new URL(targetPath, url.origin);
      rewriteUrl.search = url.search;
      return context.env.ASSETS.fetch(new Request(rewriteUrl, context.request));
    }

    // Match /birchmeier or /birchmeier/...
    if (url.pathname.startsWith('/birchmeier')) {
      let rest = url.pathname.replace(/^\/birchmeier\/?/, '');
      if (rest === '' || rest === '/') {
        rest = 'index.html';
      } else if (!rest.includes('.')) {
        rest = `${rest}.html`;
      }
      const targetPath = `/preview-birchmeier/${rest}`;
      const rewriteUrl = new URL(targetPath, url.origin);
      rewriteUrl.search = url.search;
      return context.env.ASSETS.fetch(new Request(rewriteUrl, context.request));
    }
  }

  return context.next();
}
