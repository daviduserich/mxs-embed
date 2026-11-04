const VORSCHAU_SLUG_TO_FOLDER = {
  // Free's: Zeigeversion (-v2, -v1, ohne Suffix) -> preview-frees-v2 | Vollversion (-vollversion, -vv) -> preview-frees
  'frees': 'preview-frees-v2',
  'frees-v1': 'preview-frees-v2',
  'frees-v2': 'preview-frees-v2',
  'frees-vollversion': 'preview-frees',
  'frees-vv': 'preview-frees',

  // Innere Stärke (Wüest + Paneduro): Zeigeversion (-v2, -v1, ohne Suffix) -> preview-innere-staerke-v2 | Vollversion (-vollversion, -vv) -> preview-innere-staerke
  'innere-staerke': 'preview-innere-staerke-v2',
  'innere-staerke-v1': 'preview-innere-staerke-v2',
  'innere-staerke-v2': 'preview-innere-staerke-v2',
  'innere-staerke-vollversion': 'preview-innere-staerke',
  'innere-staerke-vv': 'preview-innere-staerke',

  // FC Schlieren: Zeigeversion (-v2, -v1, ohne Suffix) -> preview-fcschlieren-v2 | Vollversion (-vollversion, -vv) -> preview-fcschlieren
  'fcschlieren': 'preview-fcschlieren-v2',
  'fcschlieren-v1': 'preview-fcschlieren-v2',
  'fcschlieren-v2': 'preview-fcschlieren-v2',
  'fcschlieren-vollversion': 'preview-fcschlieren',
  'fcschlieren-vv': 'preview-fcschlieren',

  // SC Fulenbach: Zeigeversion (-v2, -v1, ohne Suffix) -> preview-scfulenbach
  'scfulenbach': 'preview-scfulenbach',
  'scfulenbach-v1': 'preview-scfulenbach',
  'scfulenbach-v2': 'preview-scfulenbach',
  'scfulenbach-vollversion': 'preview-scfulenbach',
  'scfulenbach-vv': 'preview-scfulenbach',

  // FC Attiswil: Zeigeversion (-v2, -v1, ohne Suffix) -> preview-fcattiswil
  'fcattiswil': 'preview-fcattiswil',
  'fcattiswil-v1': 'preview-fcattiswil',
  'fcattiswil-v2': 'preview-fcattiswil',
  'fcattiswil-vollversion': 'preview-fcattiswil',
  'fcattiswil-vv': 'preview-fcattiswil',

  // Weitere Mandanten-Aliase
  'hochuli-v2': 'preview-hochuli',
  'hochuli-vollversion': 'preview-hochuli',
  'hochuli-vv': 'preview-hochuli',
  'her11-v2': 'preview-her11',
  'her11-vollversion': 'preview-her11',
  'her11-vv': 'preview-her11'
};

const CLIENT_TOKENS = {
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
  'fcschlieren': ['fcschlieren_sec_master', 'fcschlieren2026'],
  'preview-fcschlieren': ['fcschlieren_sec_master', 'fcschlieren2026'],
  'fcschlieren-v2': ['fcschlieren_sec_master', 'fcschlieren2026'],
  'preview-fcschlieren-v2': ['fcschlieren_sec_master', 'fcschlieren2026'],
  'fcschlieren-vollversion': ['fcschlieren_sec_master', 'fcschlieren2026'],
  'fcschlieren-vv': ['fcschlieren_sec_master', 'fcschlieren2026'],
  'fcattiswil': ['fcattiswil_sec_master', 'fcattiswil2026'],
  'preview-fcattiswil': ['fcattiswil_sec_master', 'fcattiswil2026'],
  'fcattiswil-v2': ['fcattiswil_sec_master', 'fcattiswil2026'],
  'scfulenbach': ['scfulenbach_sec_master', 'scfulenbach2026'],
  'preview-scfulenbach': ['scfulenbach_sec_master', 'scfulenbach2026'],
  'scfulenbach-v2': ['scfulenbach_sec_master', 'scfulenbach2026'],
  'innere-staerke': ['innerestaerke_sec_master', 'innerestaerke2026', 'innere-staerke2026'],
  'preview-innere-staerke': ['innerestaerke_sec_master', 'innerestaerke2026', 'innere-staerke2026'],
  'innere-staerke-v2': ['innerestaerke_sec_master', 'innerestaerke2026', 'innere-staerke2026'],
  'preview-innere-staerke-v2': ['innerestaerke_sec_master', 'innerestaerke2026', 'innere-staerke2026'],
  'innere-staerke-vollversion': ['innerestaerke_sec_master', 'innerestaerke2026', 'innere-staerke2026'],
  'innere-staerke-vv': ['innerestaerke_sec_master', 'innerestaerke2026', 'innere-staerke2026'],
  'frees': ['frees_sec_master', 'frees2026', 'frees-v22026'],
  'preview-frees': ['frees_sec_master', 'frees2026', 'frees-v22026'],
  'frees-v2': ['frees_sec_master', 'frees2026', 'frees-v22026'],
  'preview-frees-v2': ['frees_sec_master', 'frees2026', 'frees-v22026'],
  'frees-vollversion': ['frees_sec_master', 'frees2026', 'frees-v22026'],
  'frees-vv': ['frees_sec_master', 'frees2026', 'frees-v22026']
};

function getValidTokens(rootSegment, clientSlug) {
  const baseSlug = clientSlug.replace(/-(?:vollversion|vv|v1|v2)$/, '');
  return CLIENT_TOKENS[rootSegment] ||
         CLIENT_TOKENS[clientSlug] ||
         CLIENT_TOKENS[baseSlug] ||
         [baseSlug + '_sec_master', baseSlug + '2026', clientSlug + '2026'];
}

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
    const baseClientSlug = clientSlug.replace(/-(?:vollversion|vv|v1|v2)$/, '');
    const isCockpit = url.pathname.includes('/cockpit') || url.pathname.endsWith('/cockpit.html');
    const validTokens = getValidTokens(rootSegment, clientSlug);

    const tokenParam = url.searchParams.get('token');
    const cookieHeader = context.request.headers.get('Cookie') || '';

    const tenantCookieKey = 'mxs_auth_' + clientSlug + '=';
    const baseCookieKey = 'mxs_auth_' + baseClientSlug + '=';
    const legacyCockpitKey = 'hb_cockpit_token=';
    const legacyPreviewKey = 'hb_preview_token=';

    const hasValidCookie = validTokens.some(t =>
      cookieHeader.includes(tenantCookieKey + t) ||
      cookieHeader.includes(baseCookieKey + t) ||
      (clientSlug === 'hiltbrand' && (cookieHeader.includes(legacyCockpitKey + t) || cookieHeader.includes(legacyPreviewKey + t)))
    );

    const hasValidToken = tokenParam && validTokens.includes(tokenParam);

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
  }

  // 3. Hostname: vorschau.magnet-xs.ch (Dynamisches & Rate-sicheres Mandanten-Routing)
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
    let targetFolder = '';

    const match = url.pathname.match(/^\/([a-zA-Z0-9_-]+)(\/.*)?$/);
    if (match && !['api', 'webpilot', 'boardroom', 'partner', 'mxs-talent', 'images', 'css', 'js', 'fonts'].includes(match[1])) {
      isClientPath = true;
      activeClientSlug = match[1].toLowerCase();
      const rest = match[2];

      // Erzwinge Trailing Slash auf dem Root-Pfad eines Mandanten, damit relative Links (images/..., kontakt.html) immer stimmen
      if (!rest) {
        const slashUrl = new URL(`/${match[1]}/${url.search}`, url.origin);
        return Response.redirect(slashUrl.toString(), 302);
      }

      targetFolder = VORSCHAU_SLUG_TO_FOLDER[activeClientSlug] || `preview-${activeClientSlug}`;

      if (rest === '/onboarding' || rest === '/onboarding.html') {
        targetPath = `/${targetFolder}/onboarding`;
      } else if (rest === '/cockpit' || rest === '/cockpit/') {
        targetPath = `/${targetFolder}/cockpit.html`;
      } else {
        targetPath = `/${targetFolder}${rest}`;
      }
    }

    const rewriteUrl = new URL(targetPath, url.origin);
    rewriteUrl.search = url.search;
    let response = await context.env.ASSETS.fetch(new Request(rewriteUrl, context.request));

    // Falls Cloudflare Pages intern (z.B. wegen Pretty-URLs .html -> ohne .html) einen Redirect auslöst,
    // folgen wir ihm intern auf dem targetFolder, damit die äussere URL (z.B. /frees-vollversion/...) stabil bleibt.
    if (isClientPath && [301, 302, 307, 308].includes(response.status)) {
      const loc = response.headers.get('location');
      if (loc) {
        const directUrl = new URL(loc, url.origin);
        directUrl.search = url.search;
        response = await context.env.ASSETS.fetch(new Request(directUrl, context.request));
      }
    }

    let newHeaders = new Headers(response.headers);
    if (isClientPath) {
      const tokenParam = url.searchParams.get('token');
      if (tokenParam) {
        const baseClientSlug = activeClientSlug.replace(/-(?:vollversion|vv|v1|v2)$/, '');
        newHeaders.append('Set-Cookie', `mxs_auth_${activeClientSlug}=${tokenParam}; Path=/${activeClientSlug}/; Max-Age=86400; SameSite=Lax`);
        newHeaders.append('Set-Cookie', `mxs_auth_${baseClientSlug}=${tokenParam}; Path=/; Max-Age=86400; SameSite=Lax`);
        if (activeClientSlug === 'hiltbrand') {
          newHeaders.append('Set-Cookie', `hb_preview_token=${tokenParam}; Path=/hiltbrand/; Max-Age=86400; SameSite=Lax`);
        }
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
    const baseClientSlug = clientSlug.replace(/-(?:vollversion|vv|v1|v2)$/, '');
    const tokenParam = url.searchParams.get('token');
    const response = await context.next();
    if (tokenParam) {
      const validTokens = getValidTokens(rootSegment, clientSlug);
      if (validTokens.includes(tokenParam)) {
        const newHeaders = new Headers(response.headers);
        const cookiePath = '/' + rootSegment + '/';
        newHeaders.append('Set-Cookie', 'mxs_auth_' + clientSlug + '=' + tokenParam + '; Path=' + cookiePath + '; Max-Age=2592000; SameSite=Lax');
        newHeaders.append('Set-Cookie', 'mxs_auth_' + baseClientSlug + '=' + tokenParam + '; Path=/; Max-Age=2592000; SameSite=Lax');
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
