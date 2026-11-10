const VORSCHAU_SLUG_TO_FOLDER = {
  // MONDOCANI · Die mobile Hundeschule (Dorette Sieber, Solothurn): Zeigeversion (-v2, -v1, ohne Suffix) -> preview-mondocani-v2 | Vollversion (-vollversion, -vv) -> preview-mondocani
  'mondocani': 'preview-mondocani-v2',
  'mondocani-v1': 'preview-mondocani-v2',
  'mondocani-v2': 'preview-mondocani-v2',
  'mondocani-vollversion': 'preview-mondocani',
  'mondocani-vv': 'preview-mondocani',

  // Holz-Susi GmbH (Frick AG): Zeigeversion (-v2, -v1, ohne Suffix) -> preview-holz-susi-v2 | Vollversion (-vollversion, -vv) -> preview-holz-susi
  'holz-susi': 'preview-holz-susi-v2',
  'holz-susi-v1': 'preview-holz-susi-v2',
  'holz-susi-v2': 'preview-holz-susi-v2',
  'holz-susi-vollversion': 'preview-holz-susi',
  'holz-susi-vv': 'preview-holz-susi',

  // JOMA Solar GmbH (Wettingen): Zeigeversion (-v2, -v1, ohne Suffix) -> preview-joma-v2 | Vollversion (-vollversion, -vv) -> preview-joma
  'joma': 'preview-joma-v2',
  'joma-v1': 'preview-joma-v2',
  'joma-v2': 'preview-joma-v2',
  'joma-vollversion': 'preview-joma',
  'joma-vv': 'preview-joma',

  // IMP GmbH · Matthias Iseli (Schreinerei- & Holzbau-Marketing): Zeigeversion (-v2, -v1, ohne Suffix) -> preview-imp-marketing-v2 | Vollversion (-vollversion, -vv) -> preview-imp-marketing
  'imp-marketing': 'preview-imp-marketing-v2',
  'imp-marketing-v1': 'preview-imp-marketing-v2',
  'imp-marketing-v2': 'preview-imp-marketing-v2',
  'imp-marketing-vollversion': 'preview-imp-marketing',
  'imp-marketing-vv': 'preview-imp-marketing',

  // Herzensarbeit (Anne-Katrin Koch): Zeigeversion (-v2, -v1, ohne Suffix) -> preview-herzensarbeit-v2 | Vollversion (-vollversion, -vv) -> preview-herzensarbeit
  'herzensarbeit': 'preview-herzensarbeit-v2',
  'herzensarbeit-v1': 'preview-herzensarbeit-v2',
  'herzensarbeit-v2': 'preview-herzensarbeit-v2',
  'herzensarbeit-vollversion': 'preview-herzensarbeit',
  'herzensarbeit-vv': 'preview-herzensarbeit',

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
  'her11-vv': 'preview-her11',
  'hiltbrand-v2': 'preview-hiltbrand',
  'hiltbrand-vollversion': 'preview-hiltbrand',
  'hiltbrand-vv': 'preview-hiltbrand',
  'birchmeier-v2': 'preview-birchmeier',
  'birchmeier-vollversion': 'preview-birchmeier',
  'birchmeier-vv': 'preview-birchmeier'
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
  'frees-vv': ['frees_sec_master', 'frees2026', 'frees-v22026'],
  'herzensarbeit': ['herzensarbeit_sec_master', 'herzensarbeit2026', 'herzensarbeit-v22026'],
  'preview-herzensarbeit': ['herzensarbeit_sec_master', 'herzensarbeit2026', 'herzensarbeit-v22026'],
  'herzensarbeit-v2': ['herzensarbeit_sec_master', 'herzensarbeit2026', 'herzensarbeit-v22026'],
  'preview-herzensarbeit-v2': ['herzensarbeit_sec_master', 'herzensarbeit2026', 'herzensarbeit-v22026'],
  'herzensarbeit-vollversion': ['herzensarbeit_sec_master', 'herzensarbeit2026', 'herzensarbeit-v22026'],
  'herzensarbeit-vv': ['herzensarbeit_sec_master', 'herzensarbeit2026', 'herzensarbeit-v22026'],
  'imp-marketing': ['impmarketing_sec_master', 'impmarketing2026', 'imp-marketing2026', 'imp-marketing-v22026'],
  'preview-imp-marketing': ['impmarketing_sec_master', 'impmarketing2026', 'imp-marketing2026', 'imp-marketing-v22026'],
  'imp-marketing-v2': ['impmarketing_sec_master', 'impmarketing2026', 'imp-marketing2026', 'imp-marketing-v22026'],
  'preview-imp-marketing-v2': ['impmarketing_sec_master', 'impmarketing2026', 'imp-marketing2026', 'imp-marketing-v22026'],
  'imp-marketing-vollversion': ['impmarketing_sec_master', 'impmarketing2026', 'imp-marketing2026', 'imp-marketing-v22026'],
  'imp-marketing-vv': ['impmarketing_sec_master', 'impmarketing2026', 'imp-marketing2026', 'imp-marketing-v22026'],
  'joma': ['joma_sec_master', 'joma2026', 'jomalight2026', 'joma-v22026'],
  'preview-joma': ['joma_sec_master', 'joma2026', 'jomalight2026', 'joma-v22026'],
  'joma-v1': ['joma_sec_master', 'joma2026', 'jomalight2026', 'joma-v22026'],
  'joma-v2': ['joma_sec_master', 'joma2026', 'jomalight2026', 'joma-v22026'],
  'preview-joma-v2': ['joma_sec_master', 'joma2026', 'jomalight2026', 'joma-v22026'],
  'joma-vollversion': ['joma_sec_master', 'joma2026', 'jomalight2026', 'joma-v22026'],
  'joma-vv': ['joma_sec_master', 'joma2026', 'jomalight2026', 'joma-v22026'],
  'holz-susi': ['holzsusi_sec_master', 'holzsusi2026', 'holz-susi2026', 'holzsusi-light2026', 'holz-susi-v22026'],
  'preview-holz-susi': ['holzsusi_sec_master', 'holzsusi2026', 'holz-susi2026', 'holzsusi-light2026', 'holz-susi-v22026'],
  'holz-susi-v1': ['holzsusi_sec_master', 'holzsusi2026', 'holz-susi2026', 'holzsusi-light2026', 'holz-susi-v22026'],
  'holz-susi-v2': ['holzsusi_sec_master', 'holzsusi2026', 'holz-susi2026', 'holzsusi-light2026', 'holz-susi-v22026'],
  'preview-holz-susi-v2': ['holzsusi_sec_master', 'holzsusi2026', 'holz-susi2026', 'holzsusi-light2026', 'holz-susi-v22026'],
  'holz-susi-vollversion': ['holzsusi_sec_master', 'holzsusi2026', 'holz-susi2026', 'holzsusi-light2026', 'holz-susi-v22026'],
  'holz-susi-vv': ['holzsusi_sec_master', 'holzsusi2026', 'holz-susi2026', 'holzsusi-light2026', 'holz-susi-v22026'],
  'mondocani': ['mondocani_sec_master', 'mondocani2026', 'mondocani-light2026', 'mondocani-v22026'],
  'preview-mondocani': ['mondocani_sec_master', 'mondocani2026', 'mondocani-light2026', 'mondocani-v22026'],
  'mondocani-v1': ['mondocani_sec_master', 'mondocani2026', 'mondocani-light2026', 'mondocani-v22026'],
  'mondocani-v2': ['mondocani_sec_master', 'mondocani2026', 'mondocani-light2026', 'mondocani-v22026'],
  'preview-mondocani-v2': ['mondocani_sec_master', 'mondocani2026', 'mondocani-light2026', 'mondocani-v22026'],
  'mondocani-vollversion': ['mondocani_sec_master', 'mondocani2026', 'mondocani-light2026', 'mondocani-v22026'],
  'mondocani-vv': ['mondocani_sec_master', 'mondocani2026', 'mondocani-light2026', 'mondocani-v22026']
};

function getValidTokens(rootSegment, clientSlug) {
  const baseSlug = clientSlug.replace(/-(?:vollversion|vv|v1|v2)$/, '');
  const baseList = CLIENT_TOKENS[rootSegment] ||
         CLIENT_TOKENS[clientSlug] ||
         CLIENT_TOKENS[baseSlug] ||
         [baseSlug + '_sec_master', baseSlug + '2026', clientSlug + '2026'];
  const compactBase = baseSlug.replace(/-/g, '');
  const extended = new Set(baseList);
  extended.add(baseSlug + '2026');
  extended.add(baseSlug + 'light2026');
  extended.add(baseSlug + '-light2026');
  extended.add(compactBase + '2026');
  extended.add(compactBase + 'light2026');
  extended.add(compactBase + '-light2026');
  extended.add(clientSlug + '2026');
  extended.add(clientSlug + 'light2026');
  extended.add(clientSlug + '-light2026');
  for (const tok of baseList) {
    extended.add(tok + '-light');
    if (tok.endsWith('2026')) {
      const stem = tok.slice(0, -4);
      extended.add(stem + 'light2026');
      extended.add(stem + '-light2026');
    }
  }
  return Array.from(extended);
}

const ENTERPRISE_SECURITY_HEADERS = {
  'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload',
  'X-Content-Type-Options': 'nosniff',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy': 'camera=(self), microphone=(self), geolocation=(self)'
};

function applyEnterpriseSecurityHeaders(response) {
  if (!response) return response;
  const headers = new Headers(response.headers);
  for (const [headerName, headerValue] of Object.entries(ENTERPRISE_SECURITY_HEADERS)) {
    if (!headers.has(headerName)) {
      headers.set(headerName, headerValue);
    }
  }
  // WICHTIGE INVARIANZ: Niemals X-Frame-Options: DENY oder frame-ancestors 'none' setzen,
  // da embed.magnet-xs.ch, Kunden-Previews und Studio-Cockpits in Iframes eingebettet werden!
  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers
  });
}

export async function onRequest(context) {
  const response = await handleRequestCore(context);
  return applyEnterpriseSecurityHeaders(response);
}

async function handleRequestCore(context) {
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

  const isReservedRoot = ['api', 'webpilot', 'boardroom', 'brand-gallery', 'client-preview', 'partner', 'partner-jobs', 'reports', 'images', 'css', 'js', 'fonts', 'favicon.ico', 'robots.txt'].includes(rootSegment);

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
  if (hostname.startsWith('vorschau.') || hostname.startsWith('embed.') || hostname.endsWith('.pages.dev')) {
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

    const DIRECT_ONLY_FOLDERS = ['zurbuchen', 'cotra', 'muster-holzbau'];
    const DUAL_EMBED_AND_PREVIEW_FOLDERS = ['hiltbrand'];
    const match = url.pathname.match(/^\/([a-zA-Z0-9_-]+)(\/.*)?$/);
    if (match && !['api', 'webpilot', 'boardroom', 'brand-gallery', 'client-preview', 'partner', 'partner-jobs', 'reports', 'mxs-talent', 'images', 'css', 'js', 'fonts'].includes(match[1])) {
      isClientPath = true;
      activeClientSlug = match[1].toLowerCase();
      const rest = match[2];

      // Erzwinge Trailing Slash auf dem Root-Pfad eines Mandanten, damit relative Links (images/..., kontakt.html) immer stimmen
      if (!rest) {
        const slashUrl = new URL(`/${match[1]}/${url.search}`, url.origin);
        return Response.redirect(slashUrl.toString(), 302);
      }

      const isDirectEmbedHost = hostname.startsWith('embed.') || hostname.endsWith('.pages.dev');
      const baseSlugFolder = activeClientSlug.replace(/-(?:vollversion|vv|v1|v2)$/, '');
      if (DIRECT_ONLY_FOLDERS.includes(activeClientSlug) || (isDirectEmbedHost && DUAL_EMBED_AND_PREVIEW_FOLDERS.includes(activeClientSlug))) {
        targetFolder = activeClientSlug;
      } else {
        targetFolder = VORSCHAU_SLUG_TO_FOLDER[activeClientSlug] || ((activeClientSlug.endsWith('-vollversion') || activeClientSlug.endsWith('-vv')) ? `preview-${baseSlugFolder}` : `preview-${activeClientSlug}`);
      }

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
    const cleanReqHeaders = new Headers(context.request.headers);
    if (isClientPath) {
      cleanReqHeaders.delete('if-none-match');
      cleanReqHeaders.delete('if-modified-since');
    }
    let response = await context.env.ASSETS.fetch(new Request(rewriteUrl, {
      method: context.request.method,
      headers: cleanReqHeaders
    }));

    // Falls Cloudflare Pages intern (z.B. wegen Pretty-URLs .html -> ohne .html) einen Redirect auslöst,
    // folgen wir ihm intern auf dem targetFolder, damit die äussere URL (z.B. /frees-vollversion/...) stabil bleibt.
    if (isClientPath && [301, 302, 307, 308].includes(response.status)) {
      const loc = response.headers.get('location');
      if (loc) {
        const directUrl = new URL(loc, url.origin);
        directUrl.search = url.search;
        response = await context.env.ASSETS.fetch(new Request(directUrl, {
          method: context.request.method,
          headers: cleanReqHeaders
        }));
      }
    }

    let newHeaders = new Headers(response.headers);
    if (isClientPath) {
      const ct = (newHeaders.get('content-type') || '').toLowerCase();
      if (ct.includes('text/html')) {
        newHeaders.set('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0');
        newHeaders.delete('ETag');
      }
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
