export async function onRequest(context) {
  const url = new URL(context.request.url);
  const hostname = url.hostname.toLowerCase();

  // 0. Kontaktformular-Edge-Relay (/api/contact -> GCF_contact_form)
  if (url.pathname === '/api/contact') {
    if (context.request.method === 'OPTIONS') {
      return new Response(null, {
        status: 204,
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'POST, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type'
        }
      });
    }
    if (context.request.method === 'POST') {
      try {
        const bodyText = await context.request.text();
        const gcfRes = await fetch('https://contact-form-5pzvo6eena-oa.a.run.app', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Origin': 'https://acp-authentic-content-pilot.com',
            'Referer': 'https://acp-authentic-content-pilot.com/'
          },
          body: bodyText
        });
        const resBody = await gcfRes.text();
        return new Response(resBody, {
          status: gcfRes.status,
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          }
        });
      } catch (err) {
        return new Response(JSON.stringify({ error: err.message }), {
          status: 502,
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          }
        });
      }
    }
  }

  // 1a. Hostname: mxs-talent-solutions.com (Custom Domain Routing -> /mxs-talent/)
  if (hostname.includes('mxs-talent-solutions.com')) {
    if (url.pathname.includes('/cockpit')) {
      return Response.redirect(`https://embed.magnet-xs.ch/mxs-talent/cockpit${url.search}`, 302);
    }
    let targetPath = url.pathname;
    if (targetPath === '/' || targetPath === '') {
      targetPath = '/mxs-talent/';
    } else if (!targetPath.startsWith('/mxs-talent')) {
      targetPath = `/mxs-talent${targetPath}`;
    }

    const rewriteUrl = new URL(targetPath, url.origin);
    rewriteUrl.search = url.search;
    const response = await context.env.ASSETS.fetch(new Request(rewriteUrl, context.request));

    if ([301, 302, 307, 308].includes(response.status)) {
      const loc = response.headers.get('location');
      if (loc && loc.startsWith('/mxs-talent')) {
        const cleanLoc = loc.replace(/^\/mxs-talent/, '') || '/';
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

  // 1b. Hostname: webpilot.magnet-xs.ch
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

  // Pfad-Analyse für Mandanten
  const pathParts = url.pathname.split('/').filter(Boolean);
  const rootSegment = pathParts[0] || '';

  // API-Routen direkt an functions/api/[[catchall]].js durchlassen (Bypass für Schutzwall & Client-Routing)
  if (rootSegment === 'api') {
    return context.next();
  }

  const isReservedRoot = ['api', 'webpilot', 'boardroom', 'partner', 'images', 'css', 'js', 'fonts', 'favicon.ico', 'robots.txt'].includes(rootSegment);

  // 2. Token-Guard & Multi-Tenant Isolation für Mandanten-Pfade
  if (rootSegment && !isReservedRoot) {
    const clientSlug = rootSegment.replace(/^preview-/, '');
    const isCockpit = url.pathname.includes('/cockpit') || url.pathname.endsWith('/cockpit.html');
    const isOnboarding = url.pathname.includes('/onboarding') || url.pathname.endsWith('/onboarding.html');
    const isPublicMxsBrand = (clientSlug === 'mxs-talent') && !isCockpit;

    // Statische Medien und Styles dürfen frei passieren
    const isAsset = url.pathname.includes('/images/') ||
                    url.pathname.endsWith('.pdf') ||
                    url.pathname.endsWith('.png') ||
                    url.pathname.endsWith('.jpg') ||
                    url.pathname.endsWith('.jpeg') ||
                    url.pathname.endsWith('.webp') ||
                    url.pathname.endsWith('.mp4') ||
                    url.pathname.endsWith('.svg') ||
                    url.pathname.endsWith('.css') ||
                    url.pathname.endsWith('.js') ||
                    url.pathname.endsWith('.ico');

    // Mandanten-spezifische Tokens (Krypto-Secrets)
    const clientTokens = {
      'hiltbrand': ['hb_sec_9e2f48b7c0d3a5a81e9', 'hb2026'],
      'preview-hiltbrand': ['hb_sec_9e2f48b7c0d3a5a81e9', 'hb2026'],
      'birchmeier': ['bm_sec_7a1c8f3e2d9b4a5f', 'bi_live_ea3776_a1ef'],
      'preview-birchmeier': ['bm_sec_7a1c8f3e2d9b4a5f', 'bi_live_ea3776_a1ef'],
      'mxs-talent': ['mxs-talent_sec_master', 'mxs-talent2026'],
      'cotra': ['cotra_sec_master', 'cotra2026'],
      'preview-cotra': ['cotra_sec_master', 'cotra2026'],
      'hochuli': ['hochuli_sec_master', 'hochuli2026'],
      'preview-hochuli': ['hochuli_sec_master', 'hochuli2026'],
      'her11': ['her11_sec_master', 'her112026'],
      'preview-her11': ['her11_sec_master', 'her112026'],
      'default': [clientSlug + '_sec_master', clientSlug + '2026']
    };
    const validTokens = clientTokens[rootSegment] || clientTokens[clientSlug] || clientTokens['default'];

    const tokenParam = url.searchParams.get('token');
    const cookieHeader = context.request.headers.get('Cookie') || '';

    // Mandanten-isoliertes Cookie prüfen: mxs_auth_[slug]= + Legacy-Support für Hiltbrand
    const tenantCookieKey = 'mxs_auth_' + clientSlug + '=';
    const legacyCockpitKey = 'hb_cockpit_token=';
    const legacyPreviewKey = 'hb_preview_token=';

    const hasValidCookie = validTokens.some(t =>
      cookieHeader.includes(tenantCookieKey + t) ||
      (clientSlug === 'hiltbrand' && (cookieHeader.includes(legacyCockpitKey + t) || cookieHeader.includes(legacyPreviewKey + t)))
    );

    const hasValidToken = tokenParam && validTokens.includes(tokenParam);

    const isPreview = rootSegment.startsWith('preview-');
    const isEmbed = url.searchParams.get('embed') === 'true';
    const isVorschauHost = hostname.startsWith('vorschau.');

    // Schutzwall:
    // A) COCKPITS (/cockpit): Verlangen zwingend einen gültigen Token oder Cookie!
    if (isCockpit) {
      if (!hasValidToken && !hasValidCookie) {
        if (clientSlug === 'birchmeier' || rootSegment.includes('birchmeier')) {
          return Response.redirect('https://vorschau.magnet-xs.ch/webpilot/', 302);
        }
        return new Response('Zugriff geschützt. Bitte Cockpit mit gültigem Mandanten-Token öffnen.', {
          status: 403,
          headers: { 'Content-Type': 'text/plain; charset=utf-8' }
        });
      }
    }
    // B) VORSCHAU-HOST (vorschau.magnet-xs.ch) oder PREVIEWS (preview-*):
    // Verlangen Token oder Cookie, AUSSER bei Assets, Iframe-Embeds, Onboarding und öffentlichen Eigenmarken (mxs-talent)
    else if ((isVorschauHost || isPreview) && !isPublicMxsBrand && !isEmbed && !hasValidToken && !hasValidCookie && !isAsset && !isOnboarding) {
      if (clientSlug === 'birchmeier' || rootSegment.includes('birchmeier')) {
        return Response.redirect('https://vorschau.magnet-xs.ch/webpilot/', 302);
      }
      return new Response('Vorschau geschützt. Bitte über das Mandanten-Cockpit mit Token aufrufen.', {
        status: 403,
        headers: { 'Content-Type': 'text/plain; charset=utf-8' }
      });
    }
  }

  // 3. Hostname: vorschau.magnet-xs.ch (Dynamisches Mandanten-Routing)
  if (hostname.startsWith('vorschau.')) {
    if (url.pathname === '/' || url.pathname === '') {
      return Response.redirect('https://magnet-xs.com', 302);
    }

    // Direkte /preview-[slug] Aufrufe auf saubere /[slug] URL umleiten
    if (url.pathname.startsWith('/preview-')) {
      const cleanPath = url.pathname.replace(/^\/preview-/, '/');
      const redirectUrl = new URL(cleanPath, url.origin);
      redirectUrl.search = url.search;
      return Response.redirect(redirectUrl.toString(), 302);
    }

    let targetPath = url.pathname;
    let isClientPath = false;
    let activeClientSlug = '';

    const match = url.pathname.match(/^\/([a-zA-Z0-9_-]+)(\/.*)?$/);
    if (match && !['api', 'webpilot', 'boardroom', 'partner', 'mxs-talent', 'images', 'css', 'js', 'fonts'].includes(match[1])) {
      isClientPath = true;
      activeClientSlug = match[1];
      const rest = match[2] || '';
      if (rest === '/onboarding' || rest === '/onboarding.html') {
        targetPath = `/preview-${activeClientSlug}/onboarding`;
      } else {
        targetPath = `/preview-${activeClientSlug}${rest === '' ? '/' : rest}`;
      }
    }

    const rewriteUrl = new URL(targetPath, url.origin);
    rewriteUrl.search = url.search;
    const response = await context.env.ASSETS.fetch(new Request(rewriteUrl, context.request));

    let newHeaders = new Headers(response.headers);
    if (isClientPath) {
      const tokenParam = url.searchParams.get('token');
      if (tokenParam) {
        newHeaders.append('Set-Cookie', `mxs_auth_${activeClientSlug}=${tokenParam}; Path=/${activeClientSlug}/; Max-Age=86400; SameSite=Lax`);
        if (activeClientSlug === 'hiltbrand') {
          newHeaders.append('Set-Cookie', `hb_preview_token=${tokenParam}; Path=/hiltbrand/; Max-Age=86400; SameSite=Lax`);
        }
      }
    }

    if ([301, 302, 307, 308].includes(response.status)) {
      const loc = response.headers.get('location');
      if (loc) {
        let cleanLoc = loc.replace(/^\/preview-([a-zA-Z0-9_-]+)/, '/$1');
        if (cleanLoc === url.pathname) {
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

  // 4. Default: embed.magnet-xs.ch (Tenant-Scoped Cookie setzen)
  if (rootSegment && !isReservedRoot) {
    const clientSlug = rootSegment.replace(/^preview-/, '');
    const tokenParam = url.searchParams.get('token');
    const response = await context.next();
    if (tokenParam) {
      const clientTokens = {
        'hiltbrand': ['hb_sec_9e2f48b7c0d3a5a81e9', 'hb2026'],
        'preview-hiltbrand': ['hb_sec_9e2f48b7c0d3a5a81e9', 'hb2026'],
        'birchmeier': ['bm_sec_7a1c8f3e2d9b4a5f', 'bi_live_ea3776_a1ef'],
        'preview-birchmeier': ['bm_sec_7a1c8f3e2d9b4a5f', 'bi_live_ea3776_a1ef'],
        'mxs-talent': ['mxs-talent_sec_master', 'mxs-talent2026'],
      'cotra': ['cotra_sec_master', 'cotra2026'],
      'preview-cotra': ['cotra_sec_master', 'cotra2026'],
      'hochuli': ['hochuli_sec_master', 'hochuli2026'],
      'preview-hochuli': ['hochuli_sec_master', 'hochuli2026'],
      'her11': ['her11_sec_master', 'her112026'],
      'preview-her11': ['her11_sec_master', 'her112026'],
        'default': [clientSlug + '_sec_master', clientSlug + '2026']
      };
      const validTokens = clientTokens[rootSegment] || clientTokens[clientSlug] || clientTokens['default'];
      if (validTokens.includes(tokenParam)) {
        const newHeaders = new Headers(response.headers);
        const cookiePath = '/' + rootSegment + '/';
        newHeaders.append('Set-Cookie', 'mxs_auth_' + clientSlug + '=' + tokenParam + '; Path=' + cookiePath + '; Max-Age=2592000; SameSite=Lax');
        if (clientSlug === 'hiltbrand') {
          newHeaders.append('Set-Cookie', 'hb_cockpit_token=' + tokenParam + '; Path=' + cookiePath + '; Max-Age=2592000; SameSite=Lax');
          newHeaders.append('Set-Cookie', 'hb_preview_token=' + tokenParam + '; Path=' + cookiePath + '; Max-Age=2592000; SameSite=Lax');
        }
        return new Response(response.body, {
          status: response.status,
          headers: newHeaders
        });
      }
    }
    return response;
  }

  return context.next();
}
