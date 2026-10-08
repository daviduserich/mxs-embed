export async function onRequest(context) {
  const url = new URL(context.request.url);
  const hostname = url.hostname.toLowerCase();

  // 1. Hostname: webpilot.magnet-xs.ch
  if (hostname.startsWith('webpilot.')) {
    let targetPath = url.pathname;
    if (targetPath === '/' || targetPath === '') {
      targetPath = '/webpilot/';
    } else if (!targetPath.startsWith('/webpilot')) {
      targetPath = `/webpilot${targetPath}`;
    }

    const rewriteUrl = new URL(targetPath, url.origin);
    rewriteUrl.search = url.search;
    const response = await context.env.ASSETS.fetch(new Request(rewriteUrl, context.request));

    if ([301, 302, 307, 308].includes(response.status)) {
      const loc = response.headers.get('location');
      if (loc && loc.startsWith('/webpilot')) {
        const cleanLoc = loc.replace(/^\/webpilot/, '') || '/';
        const newHeaders = new Headers(response.headers);
        newHeaders.set('location', cleanLoc);
        return new Response(response.body, {
          status: response.status,
          headers: newHeaders
        });
      }
    }
    return response;
  }

  // 2. Token-Guard for Hiltbrand & Cockpits (Edge Shield & Video Leak Protection)
  const isHiltbrand = url.pathname.startsWith('/hiltbrand') || url.pathname.startsWith('/preview-hiltbrand');
  if (isHiltbrand) {
    const validTokens = ['hb_sec_9e2f48b7c0d3a5a81e9', 'hb2026', 'hb-preview', 'hiltbrand', 'preview-hiltbrand-token'];
    const tokenParam = url.searchParams.get('token');
    const cookieHeader = context.request.headers.get('Cookie') || '';
    const hasValidCookie = validTokens.some(t => cookieHeader.includes('hb_cockpit_token=' + t) || cookieHeader.includes('hb_preview_token=' + t));
    const hasValidToken = validTokens.includes(tokenParam);

    // Static assets (CSS, JS, images) pass through
    const isAsset = url.pathname.includes('/images/') || 
                    url.pathname.endsWith('.png') || 
                    url.pathname.endsWith('.jpg') || 
                    url.pathname.endsWith('.jpeg') || 
                    url.pathname.endsWith('.webp') || 
                    url.pathname.endsWith('.svg') || 
                    url.pathname.endsWith('.css') || 
                    url.pathname.endsWith('.js');

    const isCockpit = url.pathname.includes('cockpit');
    const isOnboarding = url.pathname.includes('onboarding');

    // Cockpit & Preview require valid token or valid cookie!
    if (isCockpit) {
      if (!hasValidToken && !hasValidCookie) {
        return Response.redirect('https://webpilot.magnet-xs.ch/', 302);
      }
    } else if (!hasValidToken && !hasValidCookie && !isAsset && !isOnboarding) {
      return Response.redirect('https://webpilot.magnet-xs.ch/', 302);
    }
  }

  // 3. Hostname: vorschau.magnet-xs.ch
  if (hostname.startsWith('vorschau.')) {
    if (url.pathname === '/' || url.pathname === '') {
      return Response.redirect('https://magnet-xs.com', 302);
    }

    // Direct /preview-hiltbrand requests redirect to /hiltbrand
    if (url.pathname.startsWith('/preview-hiltbrand')) {
      const rest = url.pathname.replace(/^\/preview-hiltbrand/, '');
      const redirectUrl = new URL(`/hiltbrand${rest}`, url.origin);
      redirectUrl.search = url.search;
      return Response.redirect(redirectUrl.toString(), 302);
    }

    let targetPath = url.pathname;
    let isHiltbrandPath = false;
    if (url.pathname.startsWith('/hiltbrand')) {
      isHiltbrandPath = true;
      const rest = url.pathname.replace(/^\/hiltbrand/, '');
      if (rest === '/onboarding' || rest === '/onboarding.html') {
        targetPath = '/preview-hiltbrand/onboarding';
      } else {
        targetPath = `/preview-hiltbrand${rest === '' ? '/' : rest}`;
      }
    } else if (url.pathname.startsWith('/birchmeier')) {
      const rest = url.pathname.replace(/^\/birchmeier/, '');
      targetPath = `/preview-birchmeier${rest === '' ? '/' : rest}`;
    }

    const rewriteUrl = new URL(targetPath, url.origin);
    rewriteUrl.search = url.search;
    const response = await context.env.ASSETS.fetch(new Request(rewriteUrl, context.request));

    let newHeaders = new Headers(response.headers);
    if (isHiltbrandPath) {
      const tokenParam = url.searchParams.get('token');
      if (tokenParam) {
        newHeaders.append('Set-Cookie', `hb_preview_token=${tokenParam}; Path=/; Max-Age=86400; SameSite=Lax`);
      }
    }

    if ([301, 302, 307, 308].includes(response.status)) {
      const loc = response.headers.get('location');
      if (loc) {
        let cleanLoc = loc
          .replace(/^\/preview-hiltbrand/, '/hiltbrand')
          .replace(/^\/preview-birchmeier/, '/birchmeier');
        if (cleanLoc === url.pathname) {
          // Verhindert Endlosschleife bei Cloudflare Clean URLs!
          const directUrl = new URL(loc, url.origin);
          return await context.env.ASSETS.fetch(new Request(directUrl, context.request));
        }
        newHeaders.set('location', cleanLoc);
        return new Response(response.body, {
          status: response.status,
          headers: newHeaders
        });
      }
    }
    return new Response(response.body, {
      status: response.status,
      headers: newHeaders
    });
  }

  // 4. Default: embed.magnet-xs.ch token cookie setting
  if (url.pathname.startsWith('/preview-hiltbrand') || url.pathname.startsWith('/hiltbrand')) {
    const tokenParam = url.searchParams.get('token');
    const response = await context.next();
    if (tokenParam) {
      const newHeaders = new Headers(response.headers);
      newHeaders.append('Set-Cookie', 'hb_cockpit_token=' + tokenParam + '; Path=/; Max-Age=2592000; SameSite=Lax');
      newHeaders.append('Set-Cookie', 'hb_preview_token=' + tokenParam + '; Path=/; Max-Age=2592000; SameSite=Lax');
      return new Response(response.body, {
        status: response.status,
        headers: newHeaders
      });
    }
    return response;
  }

  return context.next();
}
