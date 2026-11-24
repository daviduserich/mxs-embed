import { TENANT_REDIRECTS } from './lib/tenant_redirects.js';

const VORSCHAU_SLUG_TO_FOLDER = {
  // Clean Equipe GmbH · Karolina Fabic (5727 Oberkulm): Zeigeversion (-v2, -v1, ohne Suffix) -> preview-seit-v2 | Vollversion (-vollversion, -vv) -> preview-seit
  'seit': 'preview-seit-v2',
  'seit-v1': 'preview-seit-v2',
  'seit-v2': 'preview-seit-v2',
  'seit-vollversion': 'preview-seit',
  'seit-vv': 'preview-seit',
  'clean-equipe': 'preview-seit-v2',
  'clean-equipe-v2': 'preview-seit-v2',
  'clean-equipe-vollversion': 'preview-seit',

  // Good for Dogs · Martina Sidler (Baden & Birmenstorf): Zeigeversion (-v2, -v1, ohne Suffix) -> preview-die-schule-v2 | Vollversion (-vollversion, -vv) -> preview-die-schule
  'die-schule': 'preview-die-schule-v2',
  'die-schule-v1': 'preview-die-schule-v2',
  'die-schule-v2': 'preview-die-schule-v2',
  'die-schule-vollversion': 'preview-die-schule',
  'die-schule-vv': 'preview-die-schule',
  'good-for-dogs': 'preview-die-schule-v2',
  'good-for-dogs-v2': 'preview-die-schule-v2',
  'good-for-dogs-vollversion': 'preview-die-schule',

  // get.more.sales · Carmen Caselli (Zofingen): Zeigeversion (-v2, -v1, ohne Suffix) -> preview-get-more-sales-v2 | Vollversion (-vollversion, -vv) -> preview-get-more-sales
  'get-more-sales': 'preview-get-more-sales-v2',
  'get-more-sales-v1': 'preview-get-more-sales-v2',
  'get-more-sales-v2': 'preview-get-more-sales-v2',
  'get-more-sales-vollversion': 'preview-get-more-sales',
  'get-more-sales-vv': 'preview-get-more-sales',

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
  'holz-susi-original': 'preview-holz-susi-original',

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

  // Autohauser AG (Oftringen): Zeigeversion (-v2, -v1, ohne Suffix) -> preview-autohauser-v2 | Vollversion (-vollversion, -vv) -> preview-autohauser
  'autohauser': 'preview-autohauser-v2',
  'autohauser-v1': 'preview-autohauser-v2',
  'autohauser-v2': 'preview-autohauser-v2',
  'autohauser-vollversion': 'preview-autohauser',
  'autohauser-vv': 'preview-autohauser',

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

const STATIC_ASSET_EXT_RE = /\.(?:png|jpe?g|webp|gif|svg|ico|css|js|mjs|woff2?|ttf|eot|map|json|xml|txt|pdf|mp4|webm)$/i;

function wantsMarkdownNegotiation(request) {
  const accept = (request.headers.get('Accept') || '').toLowerCase();
  if (!accept.includes('text/markdown')) return false;
  const mdIdx = accept.indexOf('text/markdown');
  const htmlIdx = accept.indexOf('text/html');
  return htmlIdx === -1 || mdIdx < htmlIdx;
}

function resolveTenantRedirect(folder, relPath, url, externalPrefix = '') {
  const rules = folder && TENANT_REDIRECTS ? TENANT_REDIRECTS[folder] : null;
  if (!rules) return null;
  let normRel = (relPath || '/').replace(/\/+$/, '');
  if (!normRel) normRel = '/';
  const rule = rules[normRel] || rules[normRel.toLowerCase()];
  if (!rule || !rule.to) return null;

  let dest = rule.to;
  let targetUrl;
  if (/^https?:\/\//i.test(dest)) {
    targetUrl = new URL(dest);
  } else {
    if (!dest.startsWith('/')) dest = `/${dest}`;
    targetUrl = new URL(`${externalPrefix}${dest}`, url.origin);
  }
  if (url.search && !targetUrl.search) {
    targetUrl.search = url.search;
  }
  return new Response(null, {
    status: rule.status || 301,
    headers: {
      'Location': targetUrl.toString(),
      'Cache-Control': 'public, max-age=3600'
    }
  });
}

async function serveMarkdownTwin(context, folder, url) {
  if (!folder) return null;
  const method = context.request.method === 'HEAD' ? 'HEAD' : 'GET';
  const mdUrl = new URL(`/${folder}/llms.txt`, url.origin);
  const mdRes = await context.env.ASSETS.fetch(new Request(mdUrl, { method }));
  if (mdRes.status === 200) {
    const headers = new Headers(mdRes.headers);
    headers.set('Content-Type', 'text/markdown; charset=utf-8');
    headers.set('Vary', 'Accept');
    headers.set('Cache-Control', 'public, max-age=300');
    return new Response(method === 'HEAD' ? null : mdRes.body, {
      status: 200,
      headers
    });
  }
  return null;
}

function appendDiscoveryLinkHeader(headers, prefix = '') {
  const cleanPrefix = prefix ? `/${prefix.replace(/^\/+|\/+$/g, '')}` : '';
  headers.append(
    'Link',
    `<${cleanPrefix}/llms.txt>; rel="describedby"; type="text/markdown", <${cleanPrefix}/sitemap.xml>; rel="sitemap"; type="application/xml"`
  );
}

async function serveTenant404(context, folder, url, baseHref = '/') {
  if (STATIC_ASSET_EXT_RE.test(url.pathname)) {
    return new Response('Not Found', {
      status: 404,
      headers: {
        'Content-Type': 'text/plain; charset=utf-8',
        'Cache-Control': 'no-store'
      }
    });
  }
  const isHead = context.request.method === 'HEAD';
  let usedTenant = false;
  let errRes = null;
  if (folder) {
    const tenantErrUrl = new URL(`/${folder}/404.html`, url.origin);
    const cand = await context.env.ASSETS.fetch(new Request(tenantErrUrl, { method: 'GET' }));
    if (cand.status === 200) {
      errRes = cand;
      usedTenant = true;
    }
  }
  if (!errRes) {
    const rootErrUrl = new URL('/404.html', url.origin);
    errRes = await context.env.ASSETS.fetch(new Request(rootErrUrl, { method: 'GET' }));
  }
  if (!errRes || errRes.status !== 200) {
    return new Response('404 Not Found', {
      status: 404,
      headers: {
        'Content-Type': 'text/html; charset=utf-8',
        'Cache-Control': 'no-store'
      }
    });
  }
  let html = await errRes.text();
  if (usedTenant && baseHref && !/<base\b/i.test(html)) {
    html = html.replace(/<head\b([^>]*)>/i, `<head$1>\n  <base href="${baseHref}">`);
  }
  return new Response(isHead ? null : html, {
    status: 404,
    headers: {
      'Content-Type': 'text/html; charset=utf-8',
      'Cache-Control': 'no-store'
    }
  });
}

const WEBPILOT_EDGE_CHECK_URL = 'https://acp-plausible-tracking.acp-authentic-content-pilot.com/api/publish-career/auth/edge-check';

async function enforceWebPilotEdgeAuth(context, url, scope, siteSlug = '') {
  const checkUrl = `${WEBPILOT_EDGE_CHECK_URL}?scope=${encodeURIComponent(scope)}&site=${encodeURIComponent(siteSlug)}`;
  try {
    const authRes = await fetch(checkUrl, {
      method: 'GET',
      headers: {
        'Cookie': context.request.headers.get('Cookie') || '',
        'X-Forwarded-Host': url.hostname
      }
    });
    if (authRes.status === 200) {
      return null;
    }
    if (authRes.status === 403) {
      const html = '<!doctype html><html lang="de-CH"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kein Zugriff</title><style>body{font-family:system-ui,sans-serif;background:#0b0f17;color:#f1f5f9;display:flex;align-items:center;justify-content:center;min-height:100vh;margin:0;padding:24px}.card{max-width:480px;background:#131a26;border:1px solid #263145;border-radius:12px;padding:28px}.btn{display:inline-block;margin-top:16px;margin-right:10px;padding:10px 16px;border-radius:8px;background:#f97316;color:#fff;text-decoration:none;font-weight:600}.btn-sec{background:#1e293b;color:#cbd5e1}</style></head><body><div class="card"><h2>Kein Zugriff auf diesen Bereich</h2><p>Dein Konto ist angemeldet, besitzt aber keine Berechtigung fuer diese Website oder das Partner-Portal.</p><a class="btn" href="/partner/">Zum Dashboard</a><a class="btn btn-sec" href="/login">Konto wechseln</a></div></body></html>';
      return new Response(html, {
        status: 403,
        headers: {
          'Content-Type': 'text/html; charset=utf-8',
          'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0'
        }
      });
    }
  } catch (err) {
    // Fail-Closed bei Netzwerk- oder Backend-Fehler
  }
  const nextTarget = `${url.pathname}${url.search}`;
  const loginUrl = `${url.origin}/login?next=${encodeURIComponent(nextTarget)}`;
  return new Response(null, {
    status: 302,
    headers: {
      'Location': loginUrl,
      'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0'
    }
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
    const relPath = url.pathname.startsWith('/mxs-talent/')
      ? (url.pathname.slice('/mxs-talent'.length) || '/')
      : (url.pathname === '/mxs-talent' ? '/' : (url.pathname || '/'));

    const tenantRedir = resolveTenantRedirect('mxs-talent', relPath, url, '');
    if (tenantRedir) {
      return tenantRedir;
    }

    const isRootHtmlRoute = (relPath === '/' || relPath === '/index.html');
    if (isRootHtmlRoute && wantsMarkdownNegotiation(context.request)) {
      const mdRes = await serveMarkdownTwin(context, 'mxs-talent', url);
      if (mdRes) return mdRes;
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

    if (response.status === 404) {
      return serveTenant404(context, 'mxs-talent', url, '/');
    }

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

    if (response.status === 200 && url.pathname !== '/404.html' && !url.pathname.endsWith('/404.html')) {
      const ct = (response.headers.get('content-type') || '').toLowerCase();
      if (ct.includes('text/html')) {
        const newHeaders = new Headers(response.headers);
        appendDiscoveryLinkHeader(newHeaders, '');
        if (isRootHtmlRoute) {
          newHeaders.append('Vary', 'Accept');
        }
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
    if (targetPath === '/login' || targetPath.startsWith('/login/')) {
      return context.next();
    }
    const isCockpitSpecial = (targetPath === '/cockpit-app.html' || targetPath.includes('/cockpit'));
    if (isCockpitSpecial) {
      let edgeSite = (url.searchParams.get('site') || url.searchParams.get('client') || '').replace(/^sites\//, '').trim();
      if (!edgeSite) {
        const seg = targetPath.split('/').filter(Boolean)[0] || '';
        if (seg && seg !== 'cockpit-app.html' && seg !== 'webpilot') edgeSite = seg;
      }
      const denyRes = await enforceWebPilotEdgeAuth(context, url, 'cockpit', edgeSite);
      if (denyRes) return denyRes;
    }
    if (targetPath === '/cockpit-app.html') {
      const siteParam = (url.searchParams.get('site') || 'preview-holz-susi').replace(/^sites\//, '');
      targetPath = `/${siteParam}/cockpit.html`;
    } else if (targetPath.startsWith('/sites/preview-')) {
      targetPath = targetPath.replace(/^\/sites\//, '/');
    } else if (targetPath.startsWith('/preview-')) {
      targetPath = targetPath;
    } else if (targetPath === '/' || targetPath === '') {
      targetPath = '/webpilot/';
    } else if (!targetPath.startsWith('/webpilot')) {
      targetPath = `/webpilot${targetPath}`;
    }

    if (!isCockpitSpecial && !targetPath.startsWith('/preview-')) {
      const relPath = url.pathname.startsWith('/webpilot/')
        ? (url.pathname.slice('/webpilot'.length) || '/')
        : (url.pathname === '/webpilot' ? '/' : (url.pathname || '/'));
      const wpRedir = resolveTenantRedirect('webpilot', relPath, url, '');
      if (wpRedir) return wpRedir;
      if ((relPath === '/' || relPath === '/index.html') && wantsMarkdownNegotiation(context.request)) {
        const mdRes = await serveMarkdownTwin(context, 'webpilot', url);
        if (mdRes) return mdRes;
      }
    }

    const rewriteUrl = new URL(targetPath, url.origin);
    rewriteUrl.search = url.search;
    const response = await context.env.ASSETS.fetch(new Request(rewriteUrl, context.request));

    if (response.status === 404) {
      if (targetPath.startsWith('/preview-')) {
        const pFolder = targetPath.split('/').filter(Boolean)[0] || '';
        return serveTenant404(context, pFolder, url, pFolder ? `/${pFolder}/` : '/');
      }
      return serveTenant404(context, 'webpilot', url, '/');
    }

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

    if (response.status === 200 && !isCockpitSpecial && !targetPath.startsWith('/preview-') && url.pathname !== '/404.html' && !url.pathname.endsWith('/404.html')) {
      const ct = (response.headers.get('content-type') || '').toLowerCase();
      if (ct.includes('text/html')) {
        const newHeaders = new Headers(response.headers);
        appendDiscoveryLinkHeader(newHeaders, '');
        if (url.pathname === '/' || url.pathname === '/index.html' || url.pathname === '/webpilot' || url.pathname === '/webpilot/') {
          newHeaders.append('Vary', 'Accept');
        }
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

  // API-Routen direkt durchlassen
  if (rootSegment === 'api') {
    return context.next();
  }

  // Zentrale Login-Seite mit Clickjacking-Schutz (nur auf /login!)
  if (rootSegment === 'login') {
    const loginRes = await context.next();
    const hdrs = new Headers(loginRes.headers);
    hdrs.set('X-Frame-Options', 'DENY');
    hdrs.set('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0');
    return new Response(loginRes.body, {
      status: loginRes.status,
      statusText: loginRes.statusText,
      headers: hdrs
    });
  }

  // Default-Deny für interne Repo-/Systemdateien (Markdown, Logs, Python, Configs, Templates, Scripts)
  const lowerRoot = rootSegment.toLowerCase();
  const BLOCKED_INTERNAL_ROOTS = new Set([
    'scripts', 'templates', 'config', 'artifacts', 'leads',
    'team_submissions', 'visual-dna', 'partner-jobs', 'staging-mxs-talent',
    'functions', 'version', 'version.json', '_headers', 'bilder.json', 'stellen.json'
  ]);
  if (
    /\.(?:md|log|py|sh|bak|sql|env|toml|yaml|yml)$/i.test(url.pathname) ||
    BLOCKED_INTERNAL_ROOTS.has(lowerRoot)
  ) {
    return new Response('Not Found', {
      status: 404,
      headers: {
        'Content-Type': 'text/plain; charset=utf-8',
        'Cache-Control': 'no-store'
      }
    });
  }

  // Zero-Trust Edge Auth Guards für interne Side-Door-Tools
  if (rootSegment === 'boardroom' && !STATIC_ASSET_EXT_RE.test(url.pathname)) {
    const denyBoardroom = await enforceWebPilotEdgeAuth(context, url, 'platform', '');
    if (denyBoardroom) return denyBoardroom;
  }
  if ((rootSegment === 'brand-gallery' || rootSegment === 'client-preview') && !STATIC_ASSET_EXT_RE.test(url.pathname)) {
    const denyTool = await enforceWebPilotEdgeAuth(context, url, 'partner', '');
    if (denyTool) return denyTool;
  }

  // Zero-Trust Partner-Portal Guard (nur HTML-Dokumente)
  if (rootSegment === 'partner' && !STATIC_ASSET_EXT_RE.test(url.pathname)) {
    const denyPartner = await enforceWebPilotEdgeAuth(context, url, 'partner', '');
    if (denyPartner) return denyPartner;
  }

  // Zero-Trust /cockpit-app.html Guard auf allen Hosts
  if (url.pathname === '/cockpit-app.html') {
    const siteParam = (url.searchParams.get('site') || url.searchParams.get('client') || '').replace(/^sites\//, '').trim();
    const denyApp = await enforceWebPilotEdgeAuth(context, url, 'cockpit', siteParam);
    if (denyApp) return denyApp;
  }

  const isReservedRoot = ['api', 'login', 'webpilot', 'boardroom', 'brand-gallery', 'client-preview', 'partner', 'partner-jobs', 'reports', 'images', 'css', 'js', 'fonts', 'favicon.ico', 'robots.txt'].includes(rootSegment);

  // 2. Zero-Trust Edge Auth Guard fuer alle Cockpits (statische Read-Only-Vorschauen bleiben lesbar)
  if (rootSegment && (!isReservedRoot || rootSegment === 'webpilot')) {
    const isCockpit = url.pathname.includes('/cockpit') || url.pathname.endsWith('/cockpit.html');
    if (isCockpit) {
      const edgeSite = (rootSegment === 'webpilot')
        ? (url.searchParams.get('site') || url.searchParams.get('client') || 'webpilot').trim()
        : rootSegment;
      const denyCockpit = await enforceWebPilotEdgeAuth(context, url, 'cockpit', edgeSite);
      if (denyCockpit) return denyCockpit;
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
    let isPublicClientHtml = false;

    const DIRECT_ONLY_FOLDERS = ['zurbuchen', 'cotra', 'muster-holzbau', 'hochuli-zimmermann'];
    const DUAL_EMBED_AND_PREVIEW_FOLDERS = ['hiltbrand'];
    const match = url.pathname.match(/^\/([a-zA-Z0-9_-]+)(\/.*)?$/);
    if (match && !['api', 'login', 'webpilot', 'boardroom', 'brand-gallery', 'client-preview', 'partner', 'partner-jobs', 'reports', 'mxs-talent', 'images', 'css', 'js', 'fonts'].includes(match[1])) {
      isClientPath = true;
      activeClientSlug = match[1].toLowerCase();
      const rest = match[2];

      // Erzwinge Trailing Slash auf dem Root-Pfad eines Mandanten, damit relative Links (images/..., kontakt.html) immer stimmen
      if (!rest) {
        const slashUrl = new URL(`/${match[1]}/${url.search}`, url.origin);
        return Response.redirect(slashUrl.toString(), 302);
      }

      const lowerRest = rest.toLowerCase();
      if (activeClientSlug === 'hiltbrand' && (lowerRest === '/zurbuchen_holzbauer_november.html' || lowerRest === '/zurbuchen_holzbauer.html')) {
        const redirectUrl = new URL(`/zurbuchen/${url.search}`, url.origin);
        return Response.redirect(redirectUrl.toString(), 302);
      }

      const isDirectEmbedHost = hostname.startsWith('embed.') || hostname.endsWith('.pages.dev');
      const baseSlugFolder = activeClientSlug.replace(/-(?:vollversion|vv|v1|v2)$/, '');
      const isCockpitRoute = (rest === '/cockpit' || rest === '/cockpit/' || rest === '/cockpit.html');
      const fullVersionFolder = VORSCHAU_SLUG_TO_FOLDER[`${baseSlugFolder}-vollversion`];
      const defaultSlugFolder = VORSCHAU_SLUG_TO_FOLDER[activeClientSlug];

      // Standard-Routing für Cockpits: /<slug>/cockpit öffnet bei Dual-Varianten-Projekten
      // automatisch die 5-Seiten-Vollversion (/<slug>-vollversion/cockpit), während Besucher auf
      // /<slug>/ weiterhin die 2-Seiten-Zeigeversion sehen.
      if (!isDirectEmbedHost && isCockpitRoute && activeClientSlug === baseSlugFolder && fullVersionFolder && fullVersionFolder !== defaultSlugFolder) {
        const redirectUrl = new URL(`/${baseSlugFolder}-vollversion/cockpit${url.search}`, url.origin);
        const redirectHeaders = new Headers({
          'Location': redirectUrl.toString(),
          'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0'
        });

        return new Response(null, { status: 302, headers: redirectHeaders });
      }

      if (DIRECT_ONLY_FOLDERS.includes(activeClientSlug) || (isDirectEmbedHost && DUAL_EMBED_AND_PREVIEW_FOLDERS.includes(activeClientSlug))) {
        targetFolder = activeClientSlug;
      } else {
        targetFolder = VORSCHAU_SLUG_TO_FOLDER[activeClientSlug] || ((activeClientSlug.endsWith('-vollversion') || activeClientSlug.endsWith('-vv')) ? `preview-${baseSlugFolder}` : `preview-${activeClientSlug}`);
      }

      if (rest === '/onboarding' || rest === '/onboarding.html') {
        targetPath = `/${targetFolder}/onboarding`;
      } else if (rest === '/cockpit/') {
        const cleanCockpitUrl = new URL(`/${activeClientSlug}/cockpit${url.search}`, url.origin);
        return Response.redirect(cleanCockpitUrl.toString(), 302);
      } else if (rest === '/cockpit' || rest === '/cockpit.html') {
        targetPath = `/${targetFolder}/cockpit.html`;
      } else {
        const clientRedir = resolveTenantRedirect(targetFolder, rest, url, `/${activeClientSlug}`);
        if (clientRedir) {
          return clientRedir;
        }
        if (activeClientSlug === 'zurbuchen' && (lowerRest === '/zurbuchen_holzbauer_november.html' || lowerRest === '/zurbuchen_holzbauer.html')) {
          targetPath = '/zurbuchen/index.html';
        } else {
          targetPath = `/${targetFolder}${rest}`;
        }
        if (!DIRECT_ONLY_FOLDERS.includes(activeClientSlug)) {
          isPublicClientHtml = true;
        }
      }
    } else if (url.pathname.startsWith('/mxs-talent/')) {
      const mxsRel = url.pathname.slice('/mxs-talent'.length) || '/';
      const mxsRedir = resolveTenantRedirect('mxs-talent', mxsRel, url, '/mxs-talent');
      if (mxsRedir) return mxsRedir;
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

    if (response.status === 404) {
      if (isClientPath) {
        return serveTenant404(context, targetFolder, url, `/${activeClientSlug}/`);
      }
      if (url.pathname.startsWith('/webpilot')) {
        return serveTenant404(context, 'webpilot', url, '/webpilot/');
      }
      if (url.pathname.startsWith('/mxs-talent')) {
        return serveTenant404(context, 'mxs-talent', url, '/mxs-talent/');
      }
      return serveTenant404(context, '', url, '/');
    }

    let newHeaders = new Headers(response.headers);
    const ct = (newHeaders.get('content-type') || '').toLowerCase();
    if (isClientPath) {
      if (ct.includes('text/html')) {
        newHeaders.set('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0');
        newHeaders.delete('ETag');
        if (response.status === 200 && isPublicClientHtml && !url.pathname.endsWith('/404.html')) {
          appendDiscoveryLinkHeader(newHeaders, activeClientSlug);
        }
      }

    } else if (response.status === 200 && ct.includes('text/html') && url.pathname !== '/404.html' && !url.pathname.endsWith('/404.html')) {
      if (url.pathname.startsWith('/webpilot') && !url.pathname.includes('/cockpit')) {
        appendDiscoveryLinkHeader(newHeaders, 'webpilot');
      } else if (url.pathname.startsWith('/mxs-talent') && !url.pathname.includes('/cockpit')) {
        appendDiscoveryLinkHeader(newHeaders, 'mxs-talent');
      }
    }

    return new Response(response.body, {
      status: response.status,
      headers: newHeaders
    });
  }

  return context.next();
}
